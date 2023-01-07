from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/menu")
def home():
    return render_template("index.html")
    
@app.route("/luis")
def luis():
    return "Hello, Luis"
    
if __name__ == "__main__":
    app.run(debug=True)