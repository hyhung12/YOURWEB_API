# NAME Hung Nguyen
# EMAIL hunghn4@uci.edu
# STUDENT ID 26441523

from OpenWeather import OpenWeather
from LastFM import LastFM
from ExtraCreditAPI import ExtraCreditAPI

OWAPIKEY = "2e21bd7084278c87f8f25643dd0d7896"
LMAPIKEY = "34decff5852689a8ac70131a48089c10"
EXTRACREDITAPIKEY = ""

def activate_api(apikey:str, web_api):
    """
    Set the apikey required to make requests to a web API
    Store the response in class data attributes
    """
    web_api.set_apikey(apikey)
    web_api.load_data()
    return web_api
    
    
def run_a4():
    """
    Ask for input and transclude the keywords (@weather, @lastfm) into data from the API classes
    """
    # Call the web api for later transclusion
    ow = activate_api(OWAPIKEY, OpenWeather())
    fm = activate_api(LMAPIKEY, LastFM())
    extracreditAPI = activate_api(EXTRACREDITAPIKEY, ExtraCreditAPI())
       
    try:
        input_msg = input('Please enter your message(Enter Q to quit the program): ')
        
        if input_msg == 'Q':
            return
        
        #Output the result
        output_msg = extracreditAPI.transclude(fm.transclude(ow.transclude(input_msg)))
        print(f"\nYour message: {output_msg}")
        
    except:
        print('Oops. Program exits.')
        
    else:
        run_a4()
        
if __name__ == '__main__':
    # hi @weather and @lastfm and @extracredit
    # Temp is @weather and the artist is @lastfm and BTC price is @extracredit
    run_a4()