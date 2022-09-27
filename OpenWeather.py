# NAME Hung Nguyen
# EMAIL hunghn4@uci.edu
# STUDENT ID 26441523

from WebAPI import WebAPI

class OpenWeather(WebAPI):
    '''
    OpenWeather: get weather information from OpenWeather API
    - Data attributes:
        zipcode: Zipcode (Default value: 92697 - Irvine)
        country code: Country code (Default value: US)
        temperature: The current temperature (Default value: None)
        high_temperature: The maximum temperature (Default value: None)
        low_temperature: The minimum temperature (Default value: None)
        longtitude: The longtitude (Default value: None)
        latitude: The latitude (Default value: None)
        description: The description of weather condition (Default value: None)
        humidty: % of humidty (Default value: None)
        city: City (Default value: None)
        Sunset: The Sunset time, unix, UTC (Default value: None)
    - Methods:
        set_apikey(self, apikey:str)
        _download_url(self, url_to_download: str)
        load_data(self)
        transclude(self, message:str)
    '''
    def __init__(self, zipcode:int=92697, ccode:str="US"):
        self.zipcode = zipcode
        self.ccode = ccode
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = ''
        self.sunset = None
              
                
    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        try:
            # URL to call the API
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.api_key}&units=imperial"
            rsp_obj = self._download_url(url)
        except:
            print('ERROR!! Something went wrong or invalid API Key\n')
        else:        
            # Assign the weather data to the class's attributes
            if rsp_obj is not None:
                self.temperature = rsp_obj['main']['temp']
                self.high_temperature = rsp_obj['main']['temp_max']
                self.low_temperature = rsp_obj['main']['temp_min']
                self.longitude = rsp_obj['coord']['lon']
                self.latitude = rsp_obj['coord']['lat']
                self.description = rsp_obj['weather'][0]['description']
                self.humidity = rsp_obj['main']['humidity']
                self.city = rsp_obj['name']
                self.sunset = rsp_obj['sys']['sunset']
 

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data: current temperature in Fahrenheit
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        keyword = "@weather"
        # Check if type of input message is string
        try:
            if type(message) != str:
                message = "Please make sure the type of message is string"
            else:
            # Replace the keyword with the current temperature
                if keyword in message:
                    message = message.replace(keyword, str(self.temperature))
        except:
            print('ERROR!! Invalid input message or unable to get the current temperature')
                                  
        return message