# 🌦️ **Weather Prediction & Tweeting Bot** 🌦️

This is a weather forecasting bot that predicts rain, temperature, and humidity, and posts the weather updates to Twitter! 🌍💬

## 🔥 **Features** 🔥
- 🏙️ **Real-time Weather Data**: Fetches current weather for any city using the OpenWeatherMap API.
- 🌧️ **Rain Prediction**: Trains a machine learning model to predict if it will rain tomorrow based on historical weather data.
- 🌡️ **Temperature & Humidity Prediction**: Predicts future temperatures and humidity using Random Forest Regressor.
- 🐦 **Twitter Integration**: Automatically posts the weather forecast to Twitter!

## 🛠️ **Technologies Used** 🛠️
- 📦 `requests`: Fetches weather data from OpenWeatherMap API.
- 📊 `pandas`, `numpy`: Handles and processes historical weather data.
- 🧠 `sklearn`: Trains models to predict rain, temperature, and humidity.
- 🌐 `selenium`: Automates Twitter login and tweet posting.
- 🖥️ `termcolor`: Adds color to error messages for better visibility.

## 🚀 **Getting Started** 🚀

1. **Install Dependencies**: 
   ```bash
   pip install requests pandas numpy scikit-learn selenium termcolor
   ```

2. **API Key**:
   Replace `API_KEY` with your own [OpenWeatherMap API key](https://openweathermap.org/api).

3. **Run the Bot**:
   ```bash
   python weather_bot.py
   ```

4. **Watch it Work**:
   The bot fetches current weather data, trains the models, and predicts future weather. Then, it automatically posts the weather forecast on Twitter! 🎉

## 🧑‍💻 **Code Structure** 🧑‍💻

### `WeatherService` 🌧️
- Fetches real-time weather data from OpenWeatherMap API.
- Handles errors gracefully and provides detailed feedback.

### `DataPreprocessor` 📊
- Cleans and prepares historical weather data for machine learning models.
- Encodes categorical data for machine learning compatibility.

### `RainPredictor` 🌧️
- Trains a model to predict whether it will rain tomorrow.
- Uses a Random Forest Classifier to make predictions.

### `TemperaturePredictor` 🌡️
- Predicts future temperatures based on historical data using a Random Forest Regressor.

### `HumidityPredictor` 💧
- Predicts future humidity levels based on past data using Random Forest Regressor.

### `TwitterPoster` 🐦
- Automates Twitter login and posts a tweet with the weather forecast.

### `WeatherView` 🌞
- Coordinates all classes, fetches weather data, predicts future conditions, and posts to Twitter.

## 📅 **Future Enhancements** 📅
- 🌍 Add support for more weather APIs.
- 🖋️ Add a feature to customize tweet formats.
- 🔧 Improve error handling for edge cases.

## ⚠️ **Important Notes** ⚠️
- Ensure your Twitter credentials are correct.
- The bot runs in the Cairo timezone by default. Modify it if needed. ⏰
- Always keep your API keys safe and never share them publicly! 🔑

## 💬 **Have Questions?** 💬
Feel free to open an issue or create a pull request if you'd like to contribute! 😊
