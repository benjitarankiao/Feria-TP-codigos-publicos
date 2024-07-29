from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/gato2', methods=['GET'])
def gato2():
    return render_template("pagina.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
