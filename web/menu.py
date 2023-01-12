import sys
import html
from flask import Flask, render_template, request
from pathlib import Path
abspath = str(Path.cwd())
abspath = abspath.replace('/web','')
sys.path.insert(0, abspath+'/scanner/') 
print (abspath+'/scanner/')
from nmap import Scanner
from netdiscover import Discover

app = Flask(__name__)

@app.route("/menu")
def home():
    return render_template("index.html")
    
@app.route("/luis")
def luis():
    return "Hello, Luis"

@app.route('/scan',  methods=("POST", "GET"))
def show_scan():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        ip = request.form.get("IP")
        print(ip)
        # getting input with name = lname in HTML form
        filename = request.form.get("FILENAME")
        print(filename)
        scanner = Scanner(ip, filename)
        print("escaner creado")
        scanner.scan_services()
        #fichero = open(filename,'r')
        #contenido  = fichero.read()
        return render_template('nmap.html')
    else:
        return render_template('404.html')

@app.route('/discover',  methods=("POST", "GET"))
def show_discover():
    if request.method == "POST":
        # getting input with ip = IP and mask = MASK in HTML form
        ip = request.form.get("IP")
        mask = request.form.get("MASK")
        # getting input with filename = FILENAME in HTML form
        filename = request.form.get("FILENAME")
        discover = Discover(ip, mask, filename)
        discover.discover()
        fichero = open(filename,'r')
        contenido  = fichero.read()
        contenido = contenido.replace("_","")
        contenido = contenido.replace("-","")
        contenido = contenido.split()
        for first_items in range(0,10):
            contenido.pop(0)
        contenido = [contenido[i:i+6] for i in range(0, len(contenido), 6)]
        return render_template('discover.html', data=contenido)
    else:
        return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True, host = '192.168.226.131', port = 5000)