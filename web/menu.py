from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/menu")
def home():
    return render_template("index.html")
    
@app.route("/luis")
def luis():
    return "Hello, Luis"

@app.route('/show_data',  methods=("POST", "GET"))
def showData():
    # Convert pandas dataframe to html table flask
    fichero = open('/home/kali/Desktop/CybersecAssistant/scanner/resultado_escaneo.txt','r')
    contenido  = fichero.read()
    print(contenido)
    return render_template('prueba.html', data=contenido)

if __name__ == "__main__":
    app.run(debug=True, host = '192.168.226.131', port = 5000)