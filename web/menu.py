import sys
from flask import Flask, render_template, request
from pathlib import Path
abspath = str(Path.cwd())
abspath = abspath.replace('/web','')
sys.path.insert(0, abspath+'/scanner/') 
print (abspath+'/scanner/')
from nmap import Scanner

app = Flask(__name__)

@app.route("/menu")
def home():
    return render_template("index.html")
    
@app.route("/luis")
def luis():
    return "Hello, Luis"

@app.route('/show_data',  methods=("POST", "GET"))
def showData():
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
        fichero = open(filename,'r')
        contenido  = fichero.read()
        print(contenido)
        return render_template('prueba.html', data=contenido)
    else:
        return render_template('404.html')



if __name__ == "__main__":
    app.run(debug=True, host = '192.168.226.131', port = 5000)