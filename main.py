from attach_time import *
import requests
from threading import Thread
import time
from test_connection import test_connection


class City(Thread):
    api_key = "278ffd3cf4152e12b1b13598895aad84"

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.complete_link = "https://api.openweathermap.org/data/2.5/weather?q=" + name + "&appid=" + self.api_key
        self.file_name = None
        self.file_ready = False

    def set_up_file(self,time_then):
        print('\nBeginning file preparation for {}...'.format(self.name))

        self.file_name = self.name + ' ' + time_then + '.txt'

        with open(self.file_name,'w') as f:
            f.write('\n\nAs of ' + time_then)

        time.sleep(2)
        print('\nFile prepared for {}'.format(self.name))

        self.file_ready = True

        

    def run(self):
        if test_connection():
            print('\nProceeding to retrieve weather data for {}...\n'.format(self.name))

            api_data = requests.get(self.complete_link)
            json_data = api_data.json()
            # print(json_data)

            if json_data['cod'] == '404':
                print('City name invalid...Please check again the city name you entered for {}'.format(self.name))
            else:
                print('\nWeather data successfully fetched for {}...\nCreating weather report...\n\n'.format(self.name))

                weather_element = json_data['weather'][0]['main']
                description = json_data['weather'][0]['description']
                temp = (json_data['main']['temp']) - 273 # Deg. Celcius
                humid = json_data['main']['humidity'] # Percentage
                wind_speed = json_data['wind']['speed'] #kph
                wind_direction = json_data['wind']['deg'] # Direction
                cloudiness = json_data['clouds']['all'] # Percentage

                # Output to file
                
                while True:

                    if self.file_ready:
                        with open(self.file_name,'a') as f:
                            f. write('\n\n' + self.name + ' Current Weather Report\n\n')
                            f.write('=========================\n\n')
                            f.write('1. Current dominant element: ' + weather_element)
                            f.write('\n2. Description: ' + description)
                            f.write('\n3. Current Temperature: %.2f Degrees Celcius' %(temp))
                            f.write('\n4. Relative Humidity: ' + str(humid) + ' %')
                            f.write('\n5. Current Wind Speed: ' + str(wind_speed) + ' kph')
                            f.write('\n6. Current Wind Direction: ' + str(wind_direction) + ' Degrees')
                            f.write('\n7. Cloudiness: ' + str(cloudiness) + ' %')

                        print('\n\n{}...Done!\n'.format(self.name))

                        break

                    else:
                        pass

        
        else:
            print('\n\nNo internet connection, sorry :-(')




if __name__ == "__main__":

    print(r'''
    ================================================
    %                                              %
    %             WEATHER APPLICATION              %
    %                                              %
    %  Compare location weather data on the go!    %
    %                                              $
    %                 UPTO 3 CITIES!               %
    %                                              %
    ================================================''')

    if test_connection():
        lst = list()
        num = int(input('\n\nNumber of Cities for comparison:\n\n>>>  '))

        for i in range(num):
            city = input("\nCity " + str(i+1) + " name: ")
            lst.append(city)
        
        # Instantiate objects with the threads
        city1 = City(lst[0]); time1 = TimeDetails(city1)
        city2 = City(lst[1]); time2 = TimeDetails(city2)
        city3 = City(lst[2]); time3 = TimeDetails(city3)

        # Start the threads
        city1.start() 
        time1.start()

        city2.start() 
        time2.start()

        city3.start()
        time3.start()

        # Let the threads finish their tasks before the main thread can exit
        city1.join()
        city2.join()
        city3.join()

        
        print('\n\nDone! You can now view the reports for comparison!')
    else:
        print('\n\nSorry... Connection currently not available :-(\n\nTry again later...')