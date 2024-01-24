from flask import Flask,render_template,redirect,request


app = Flask(__name__,static_url_path='/static/')

@app.route("/")
def main():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')    