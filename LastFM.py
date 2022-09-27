# NAME Hung Nguyen
# EMAIL hunghn4@uci.edu
# STUDENT ID 26441523

from WebAPI import WebAPI

class LastFM(WebAPI):
    '''
    LastFM: use album.getinfo() from Last.FM API
    - Data attributes:
        artist: Name of artist (Default value: None)
        album: Name of album (Default value: None)
        release_date: Album's release date (Default value: None)
        tracks: Number of tracks in the album (Default value: None)
        api_key: API key (Default value: "d4abd7ee98b4ef5a3496de4abb539a12")
    - Methods:
        set_apikey(self, apikey:str)
        _download_url(self, url_to_download: str)
        load_data(self)
        transclude(self, message:str)
    '''
    def __init__(self, artist:str="BLACKPINK", album:str="THE+ALBUM"):
        self.artist = artist
        self.album = album
        self.release_date = None
        self.tracks = None
        
        
    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        # URL to call the API
        try:
            url = f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={self.api_key}&artist={self.artist}&album={self.album}&format=json"
            rsp_obj = self._download_url(url)
        except:
            print('ERROR!! Something went wrong or invalid API Key\n')
        else:
            # Assign the weather data to the class's attributes
            if rsp_obj is not None:
                if rsp_obj['album']['mbid'] == '':
                    print('Artist or album is not correct')
                else:
                    self.release_date = rsp_obj['album']['wiki']['published']
                    self.tracks = len(rsp_obj['album']['tracks']['track'])

                    
    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data: the release date of the album
        :param message: The message to transclude
        :returns: The transcluded message
        '''
        keyword = "@lastfm"
        # Check if type of input message is string
        try:
            if type(message) != str:
                message = "Please make sure the type of message is string"
            else:
            # Replace the keyword with the name of artist
                if keyword in message:
                    message = message.replace(keyword,self.release_date)
        except:
            print('ERROR!! Invalid input message or unable to get the release date of the album')
                                  
        return message