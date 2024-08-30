
# Weather App

This project is a simple weather application built with Python and Tkinter. It fetches weather data from an external API and displays it in a graphical user interface (GUI). The app customizes the interface based on the current weather conditions.

## Features

- **Real-Time Weather Information**: Fetches and displays current weather details like temperature, weather condition, and city name.
- **Dynamic Background**: Changes the background color of the app based on the weather condition (e.g., Clear, Clouds, Rain).
- **Weather Icons**: Displays appropriate icons for different weather conditions.
- **Simple and Intuitive GUI**: Built using Tkinter, the app has an easy-to-use interface.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `requests` library for making API calls
- `PIL` (Pillow) for handling images

You can install the required libraries using:

```bash
pip install requests Pillow
```

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/VSkrishnaa/python-project.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd python-project
   ```

3. **Run the application**:

   ```bash
   python weather_report.py
   ```

4. **Enter a city name** into the input field and press enter. The application will fetch the current weather data for the city and display it in the interface.

## API Setup

This application fetches weather data from an external API. Make sure to set up your API key in the script:

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Replace `YOUR_API_KEY` in the script with your actual API key:

   ```python
   api_key = "fad5927473caec47a8bbb594cdde46a9"
   ```

## File Structure

- **`weather_report.py`**: The main Python script that contains the code for the application.
- **Icons**: The directory where weather condition icons are stored (e.g., `sun.png`, `cloud.png`).

## Screenshots

<img width="401" alt="Screenshot 2024-08-31 at 1 38 39 AM" src="https://github.com/user-attachments/assets/2fd4eeb5-df0f-4f92-9efd-fd383d25f2f4">




## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/).

