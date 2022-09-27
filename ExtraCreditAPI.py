# NAME Hung Nguyen
# EMAIL hunghn4@uci.edu
# STUDENT ID 26441523

from WebAPI import WebAPI
EXTRACREDITAPIKEY = ""

class ExtraCreditAPI(WebAPI):
    '''
    ExtraCreditAPI: collect the bitcoin price from the 3rd API
    - Data attributes:
        btc_price: bitcoin price in USD (Default value: '')
    - Methods:
        set_apikey(self, apikey:str)
        _download_url(self, url_to_download: str)
        load_data(self)
        transclude(self, message:str)
    '''
    def __init__(self):
        self.btc_price = ''   
        
        
    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        # URL to call the API
        try:
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            rsp_obj = self._download_url(url)
        except:
            print('ERROR!! Something went wrong or invalid API Key\n')
        else:
            # Assign the weather data to the class's attributes
            if rsp_obj is not None:
                self.btc_price = '$' + rsp_obj['bpi']['USD']['rate'][:-2]

                    
    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data: name of artist
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        keyword = "@extracredit"
        # Check if type of input message is string
        try:
            if type(message) != str:
                message = "Please make sure the type of message is string"
            else:
            # Replace the keyword with the bitcoin price
                if keyword in message:
                    message = message.replace(keyword, self.btc_price)
        except:
            print('ERROR!! Invalid input message or unable to get the bitcoin price')
                                  
        return message