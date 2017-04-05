# TODO: print weather for all day, hour by hour

import pyowm

# API key and type of subscription from http://openweathermap.org/
api_data = pyowm.OWM(API_key='3680a47900fb30de7d81ef3cb1a7d9fb',
                     subscription_type='free')

# Check API
is_api_online = api_data.is_API_online()


def print_weather():
    if is_api_online == True:
        print('API is online...')

        # Choose city
        city_input = input("Type your City and country symbol"
                           "\nf.ex. Warsaw, pl"
                           "\n-->:")

        # Set city for weather search in ('City, country symbol')
        observation = api_data.weather_at_place(city_input)
        weather = observation.get_weather()

        # Weather details
        clouds = weather.get_clouds()
        rain = weather.get_rain()
        wind = weather.get_wind()
        wind_speed = wind['speed']
        wind_deg = wind['deg']
        humidity = weather.get_humidity()
        temperature = weather.get_temperature('celsius')
        temperature_temp = temperature['temp']
        temperature_max = temperature['temp_max']
        temperature_min = temperature['temp_min']
        status = weather.get_detailed_status()

        # Print weather data from details
        print(f'Weather now in {city_input} \n'
              '\n'
              f'Clouds\t\t\t:\t{clouds} %\n'
              f'Rain\t\t\t:\t{rain} %\n'
              f'Wind speed\t\t:\t{wind_speed}\n'
              f'Wind degree\t\t:\t{wind_deg}\n'
              f'Humidity\t\t:\t{humidity} %\n'
              f'Temperature\t\t:\t{temperature_temp} celsius\n'
              f'Max temperature\t:\t{temperature_max} celsius\n'
              f'Min temperature\t:\t{temperature_min} celsius\n'
              f'Weather status\t:\t{status}')

    else:
        print('API is offline...')


# print_weather()

def print_weather_warsaw():

    # if is_api_online == True
    if is_api_online:
        print('API is online...')

        city_input = 'Warsaw, pl'

        # Set city for weather search
        observation = api_data.weather_at_place(city_input)
        weather = observation.get_weather()

        # Weather details
        clouds = weather.get_clouds()
        rain = weather.get_rain()
        wind = weather.get_wind()
        wind_speed = wind['speed']
        humidity = weather.get_humidity()
        temperature = weather.get_temperature('celsius')
        temperature_temp = temperature['temp']
        temperature_max = temperature['temp_max']
        temperature_min = temperature['temp_min']
        status = weather.get_detailed_status()

        # Print weather data from details
        try:
            with open('weatherdata.txt', mode='w',
                      encoding='utf-8') as weather_file:

                # weather data saved in text file in new line
                weather_file.write(
                    f'Weather now in {city_input} \n'
                    '\n'
                    f'Clouds: {clouds} %\n'
                    f'Rain: {rain} %\n'
                    f'Wind speed: {wind_speed}\n'
                    f'Humidity: {humidity} %\n'
                    f'Temperature: {temperature_temp} celsius\n'
                    f'Max temperature: {temperature_max} celsius\n'
                    f'Min temperature: {temperature_min} celsius\n'
                    f'Weather status: {status}')
                weather_file.close()
                # if weather_file.closed == True
                if weather_file.closed:
                    print('weather data saved in text file')
        except:
            print('Error with text file')
            pass

    else:
        result = 'API is offline...'
        return result


print_weather_warsaw()
