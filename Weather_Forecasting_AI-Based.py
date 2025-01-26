import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from datetime import datetime, timedelta
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from termcolor import colored  # Import termcolor for colored output


class WeatherService:
    API_KEY = 'Your API Key'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/'

    @staticmethod
    def get_current_weather(city):
        try:
            url = f"{WeatherService.BASE_URL}weather?q={city}&appid={WeatherService.API_KEY}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                'city': data['name'],
                'current_temp': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'temp_min': round(data['main']['temp_min']),
                'temp_max': round(data['main']['temp_max']),
                'humidity': round(data['main']['humidity']),
                'description': data['weather'][0]['description'],
                'country': data['sys']['country'],
                'wind_gust_dir': data['wind']['deg'],
                'pressure': data['main']['pressure'],
                'wind_Gust_Speed': data['wind']['speed']
            }
        except requests.exceptions.RequestException as e:
            print(colored(f"❌ Error while fetching current weather: {e}", "red"))
            return None


class DataPreprocessor:
    @staticmethod
    def read_historical_data(filename):
        try:
            df = pd.read_csv(filename)
            df = df.dropna().drop_duplicates()
            return df
        except Exception as e:
            print(colored(f"❌ Error reading historical data: {e}", "red"))
            return None

    @staticmethod
    def prepare_data(data):
        try:
            le = LabelEncoder()
            data['WindGustDir'] = le.fit_transform(data['WindGustDir'])
            data['RainTomorrow'] = le.fit_transform(data['RainTomorrow'])
            x = data[['MinTemp', 'MaxTemp', 'WindGustDir', 'WindGustSpeed', 'Humidity', 'Pressure', 'Temp']]
            y = data['RainTomorrow']
            return x, y, le
        except Exception as e:
            print(colored(f"❌ Error preparing data: {e}", "red"))
            return None, None, None

    @staticmethod
    def prepare_regression_data(data, feature):
        try:
            x, y = [], []
            for i in range(len(data) - 1):
                x.append(data[feature].iloc[i])
                y.append(data[feature].iloc[i + 1])
            x = np.array(x).reshape(-1, 1)
            y = np.array(y)
            return x, y
        except Exception as e:
            print(colored(f"❌ Error preparing regression data for {feature}: {e}", "red"))
            return None, None


class RainPredictor:
    @staticmethod
    def train_model(x, y):
        try:
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(x_train, y_train)
            return model
        except Exception as e:
            print(colored(f"❌ Error training rain model: {e}", "red"))
            return None

    @staticmethod
    def predict_rain(model, data):
        return model.predict(data)[0] if model else None


class TemperaturePredictor:
    @staticmethod
    def train_model(x, y):
        try:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(x, y)
            return model
        except Exception as e:
            print(colored(f"❌ Error training temperature model: {e}", "red"))
            return None

    @staticmethod
    def predict_future(model, current_value):
        try:
            predictions = [current_value]
            for _ in range(5):
                next_value = model.predict(np.array([[predictions[-1]]]))
                predictions.append(next_value[0])
            return predictions[1:]
        except Exception as e:
            print(colored(f"❌ Error predicting future temperature: {e}", "red"))
            return []


class HumidityPredictor:
    @staticmethod
    def train_model(x, y):
        try:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(x, y)
            return model
        except Exception as e:
            print(colored(f"❌ Error training humidity model: {e}", "red"))
            return None

    @staticmethod
    def predict_future(model, current_value):
        try:
            predictions = [current_value]
            for _ in range(5):
                next_value = model.predict(np.array([[predictions[-1]]]))
                predictions.append(next_value[0])
            return predictions[1:]
        except Exception as e:
            print(colored(f"❌ Error predicting future humidity: {e}", "red"))
            return []


class TwitterPoster:
    @staticmethod
    def post_to_twitter(username, password, tweet_content):
        try:
            driver = webdriver.Chrome()
            driver.get("https://twitter.com/login")
            time.sleep(5)

            username_field = driver.find_element(By.NAME, "text")
            username_field.send_keys(username)
            username_field.send_keys(Keys.RETURN)
            time.sleep(5)

            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            time.sleep(8)

            if "home" not in driver.current_url:
                print(colored("❌ Login failed", "red"))
                return False

            driver.get("https://twitter.com/compose/tweet")
            time.sleep(8)

            tweet_input = driver.switch_to.active_element
            tweet_input.send_keys(tweet_content)
            time.sleep(3)

            tweet_input.send_keys(Keys.CONTROL + Keys.RETURN)
            time.sleep(5)

            print(colored("✅ Tweet posted successfully.", "green"))
            return True
        except Exception as e:
            print(colored(f"❌ Error while posting tweet: {e}", "red"))
            return False
        finally:
            driver.quit()


class WeatherView:
    def __init__(self, city):
        self.city = city
        self.weather_service = WeatherService()
        self.data_preprocessor = DataPreprocessor()
        self.rain_predictor = RainPredictor()
        self.temp_predictor = TemperaturePredictor()
        self.humidity_predictor = HumidityPredictor()
        self.twitter_poster = TwitterPoster()

    def display_weather_data(self):
        current_weather = self.weather_service.get_current_weather(self.city)
        if not current_weather:
            print(colored("❌ Could not fetch current weather data.", "red"))
            return

        historical_data = self.data_preprocessor.read_historical_data('weather.csv')
        if historical_data is None:
            print(colored("❌ Could not read historical data.", "red"))
            return

        x, y, le = self.data_preprocessor.prepare_data(historical_data)
        if x is None or y is None or le is None:
            print(colored("❌ Error preparing the dataset.", "red"))
            return

        rain_model = self.rain_predictor.train_model(x, y)
        if rain_model is None:
            print(colored("❌ Error training the rain prediction model.", "red"))
            return

        wind_deg = current_weather['wind_gust_dir'] % 360
        compass_points = [
            ("N", 0, 11.25), ("NNE", 11.25, 33.75), ("NE", 33.75, 56.25),
            ("ENE", 56.25, 78.75), ("E", 78.75, 101.25), ("ESE", 101.25, 123.75),
            ("SE", 123.75, 146.25), ("SSE", 146.25, 168.75), ("S", 168.75, 191.25),
            ("SSW", 191.25, 213.75), ("SW", 213.75, 236.25), ("WSW", 236.25, 258.75),
            ("W", 258.75, 281.25), ("WNW", 281.25, 303.75), ("NW", 303.75, 326.25),
            ("NNW", 326.25, 348.75)
        ]
        compass_direction = next((point for point, start, end in compass_points if start <= wind_deg < end), None)

        if compass_direction:
            compass_direction_encoded = le.transform([compass_direction])[0] if compass_direction in le.classes_ else -1
        else:
            compass_direction_encoded = -1

        current_data = {
            'MinTemp': current_weather['temp_min'],
            'MaxTemp': current_weather['temp_max'],
            'WindGustDir': compass_direction_encoded,
            'WindGustSpeed': current_weather['wind_Gust_Speed'],
            'Humidity': current_weather['humidity'],
            'Pressure': current_weather['pressure'],
            'Temp': current_weather['current_temp'],
        }

        current_df = pd.DataFrame([current_data])
        rain_prediction = self.rain_predictor.predict_rain(rain_model, current_df)

        x_temp, y_temp = self.data_preprocessor.prepare_regression_data(historical_data, 'Temp')
        x_hum, y_hum = self.data_preprocessor.prepare_regression_data(historical_data, 'Humidity')

        temp_model = self.temp_predictor.train_model(x_temp, y_temp)
        hum_model = self.humidity_predictor.train_model(x_hum, y_hum)

        future_temp = self.temp_predictor.predict_future(temp_model, current_weather['temp_min'])
        future_humidity = self.humidity_predictor.predict_future(hum_model, current_weather['humidity'])

        timezone = pytz.timezone('Africa/Cairo')
        now = datetime.now(timezone)
        next_hour = now + timedelta(hours=1)
        next_hour = next_hour.replace(minute=0, second=0, microsecond=0)
        future_times = [(next_hour + timedelta(hours=i)).strftime("%H:00") for i in range(5)]

        message = (
            f"City: {self.city}, {current_weather['country']}\n" +
            f"Current Temperature: {current_weather['current_temp']}°C\n" +
            f"Feels Like: {current_weather['feels_like']}°C\n" +
            f"Min Temperature: {current_weather['temp_min']}°C\n" +
            f"Max Temperature: {current_weather['temp_max']}°C\n" +
            f"Humidity: {current_weather['humidity']}%\n" +
            f"Weather Prediction: {current_weather['description']}\n" +
            f"Rain Prediction: {'Yes' if rain_prediction else 'No'}\n\n" +
            "Future Temperature Predictions:\n"
        )

        for time, temp in zip(future_times, future_temp):
            message += f"{time}: {round(temp, 1)}°C\n"

        # Post the tweet
        if not self.twitter_poster.post_to_twitter("weather_bot813g", "weather_bot813g", message):
            print(colored("❌ Tweet posting failed.", "red"))

        input("Press Enter to exit...")
        

# Example usage
weather_view = WeatherView(city="Cairo")
weather_view.display_weather_data()
