# 🌦️ **Weather Prediction & Climate Insights** 🌦️

This project is a weather forecasting system that predicts rain, temperature, and humidity while offering climate insights to raise awareness about environmental changes. The bot initially posted weather updates to Twitter but is being upgraded into a real-time web application! 🌍💬

## 🔥 **Features** 🔥
- 🏙️ **Real-time Weather Data**: Fetches current weather for any city using the OpenWeatherMap API.
- 🌧️ **Rain Prediction**: Uses machine learning to predict the likelihood of rain tomorrow based on historical weather data.
- 🌡️ **Temperature & Humidity Forecasting**: Predicts future temperature and humidity trends using Random Forest Regressor.
- 📊 **Climate Insights**: Analyzes long-term weather trends for better understanding of climate changes.
- 🚀 **Web Application (Upcoming)**: A user-friendly platform to display real-time weather data and predictions interactively.

## 🛠️ **Technologies Used** 🛠️
- 📦 `requests`: Fetches weather data from OpenWeatherMap API.
- 📊 `pandas`, `numpy`: Processes and analyzes historical weather data.
- 🧠 `scikit-learn`: Trains machine learning models for weather and climate predictions.
- 🌐 `selenium` (Legacy): Automated Twitter posting (to be replaced by a web application).
- 🖥️ `termcolor`: Enhances error message visibility.

## 🚀 **Getting Started** 🚀

1. **Install Dependencies**: 
   ```bash
   pip install requests pandas numpy scikit-learn selenium termcolor
2. API Key: Replace API_KEY in the code with your own OpenWeatherMap API key.

3. Run the Bot:
python Model.py

4.Watch It Work: The system fetches current weather, trains predictive models, and forecasts future conditions.

## 🧑‍💻 Code Structure 🧑‍💻

### `WeatherService` 🌧️
- Fetches real-time weather data from OpenWeatherMap API.
- Handles API responses and errors effectively.

### `DataPreprocessor` 📊
- Cleans and prepares historical weather data for machine learning.
- Encodes categorical variables for compatibility with ML models.

### `RainPredictor` 🌧️
- Predicts whether it will rain tomorrow using a Random Forest Classifier.

### `TemperaturePredictor` 🌡️
- Predicts future temperatures using a Random Forest Regressor.

### `HumidityPredictor` 💧
- Predicts future humidity levels using historical data.

### `TwitterPoster` 🐦 *(Legacy)*  
- Automates Twitter login and posts a tweet with the weather forecast. (This feature will be replaced by a web-based dashboard.)

### `WeatherView` 🌞
- Orchestrates all components: fetching data, running predictions, and displaying results.

---

## 📅 Future Enhancements 📅
- 🌍 Transition to a web application with an interactive dashboard.
- 📊 Add visualizations for climate insights (e.g., graphs, heatmaps).
- 🔍 Introduce advanced ML models like LSTM for long-term climate trend analysis.
- 🖋️ Allow users to input custom cities for localized forecasts.

---

## ⚠️ Important Notes ⚠️
- Ensure API keys are correctly configured and secured. 🔑
- The bot assumes Cairo timezone by default. Update if necessary. ⏰
- The upcoming version will focus on real-time data visualization through a web interface.

---

## 💬 Have Questions? 💬
Feel free to open an issue or create a pull request. Contributions are always welcome! 😊
