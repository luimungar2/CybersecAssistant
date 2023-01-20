from hashlib import md5
import json
from virus_total_apis import PublicApi


class VTHandler():
    """ This class contains every method for handler the VT API.
    Gets the API-key from the HTML form and perfom a scan for a url o a file """
    def __init__(self,apikey):
        """ contructor method. Gets an apikey from form and instanciates the class"""
        self.apikey = PublicApi(apikey)
        
    def scan_file(self,file):
        """ input: file to scan; output: analysis """
        self.file = file
        try:
            with open(self.file, "rb") as f:
                self.file_hash = md5(f.read()).hexdigest()
            self.response = self.apikey.get_file_report(self.file_hash)
            if self.response["response_code"] == 200:
                if self.response["results"]["positives"] > 0:
                    print("Malware detected:",self.file)
                    return "Malware detected: "+self.file
                else:
                    print("The following file is clean:",self.file)
                    return "clean file: "+self.file
            else:
                print("Could not performance an analysis from file",self.file)
        except Exception as scan_file_error:
            print("Error while file scanning: ",scan_file_error)
    
    def scan_url(self,url):
        """ input: url to scan ; output: url analysis """
        self.url = url
        try:
            self.response = self.apikey.get_url_report(self.url)
            if self.response["response_code"] == 200:
                if self.response["results"]["positives"] > 0:
                    positives = self.response["results"]["positives"]
                    total = self.response["results"]["total"]
                    print(str(positives)+'/'+str(total)+" search engines detected the following URL as Malicious:",self.url)
                    print("Those engines are: ")
                    for engine in self.response["results"]["scans"]:
                        if self.response["results"]["scans"][engine]["detected"] == True:
                            print(engine)
                    return "Result: Malicious URL"
                    #with open("response.json", "w") as f:
                        #json.dump(self.response, f, indent=4)
                    #return self.response
                else:
                    print("The following URL is clean:",self.url)
                    #return "clean URL: "+self.url
                    return(self.response)
            else:
                print("Could not performance an analysis from URL",self.url)
        except Exception as scan_url_error:
            print("Error while url scanning:",scan_url_error)
            return(None)
    

if __name__ == "__main__":
    apikey = "15fed46525daffa3df161004c53b7746082b16e73fc05387eac5833b74e4d6c7"
    virust = VTHandler(apikey)
    analysis = virust.scan_url("adsports.in")
    print(analysis)
