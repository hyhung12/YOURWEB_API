# NAME Hung Nguyen
# EMAIL hunghn4@uci.edu
# STUDENT ID 26441523

from abc import ABC, abstractmethod
import urllib, json
from urllib import request,error

class WebAPI(ABC):

    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        self.api_key = apikey

        
    def _download_url(self, url_to_download: str) -> dict:
        '''
        Open the url and save the content of the url to an object
        Then convert it to a dictionary to easily process
        '''
        response = None
        rsp_obj = None       
        try:
            # Open the url
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            # Conver to a dictionary
            rsp_obj = json.loads(json_results)
            
        # if the user is gettting HTTP Error(401, 404, 503, etc)
        except urllib.error.HTTPError as e:
            print('ERROR!! One of the field in your API call is not correct or your API call is not in a correct format\n')

        # if the URL is incorrect or loss of connection
        except urllib.error.URLError:
            print('ERROR!! Your URL is not correct or Your Internect connection is disrupted\n')

        # other errors
        except:
            print('ERROR!! Your API call is not in a correct format. Please visit the weather page to check if there are any changes\n')

        finally:
            if response != None:
                response.close()
                
        return rsp_obj 

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transclude(self) -> str:
        pass