
import vt

class VTHandler():
    """ This class contains every method for handler the VT API.
    Gets the API-key from the HTML form and perfom a scan for a url o a file """
    def __init__(self,apikey):
        """ contructor method. Gets an apikey from form and instanciates the class"""
        self.apikey = apikey
        self.client = vt.Client(self.apikey)
    
    def scan_file(self,file):
        """ input: file to scan; output: analysis """
        self.file = file
        try:
            with open(self.file, "rb") as f:
                file_analysis = self.client.scan_file(f, wait_for_completion=True)
            return(file_analysis)
        except Exception as scan_file_error:
            print("Error while file scanning: ",scan_file_error)
            return(None)
    
    def scan_url(self,url):
        """ input: url to scan ; output: url analysis """
        self.url = url
        try:
            url_analysis = self.client.scan_url(self.url)
            return(url_analysis)
        except Exception as scan_url_error:
            print("Error while url scanning: ",scan_url_error)
            return(None)
    
    def get_file_info(self,file):
        """ input: file name; output: quick file info """
        self.file = self.client.get_object(file)
        return (self.file.last_analysis_stats)
    
    def get_url_info(self,url):
        """input: url for retrieving info; output: quick url info """
        self.target = url
        self.url_id = vt.client.url_id(self.target)
        self.url = self.client.get_object("/urls/{}", self.url_id)
        return (self.url)

if __name__ == "__main__":
    apikey = "15fed46525daffa3df161004c53b7746082b16e73fc05387eac5833b74e4d6c7"
    virust = VTHandler(apikey)
    url_info = virust.get_url_info("https://www.lavozdehorus.com/")
    print(url_info)
