from flask import Flask, render_template, request
from .models.usuarios import usuario, vuelos
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/', methods=['Post'])
def index():
    search = request.args.get('search')
    if search:
        print("search parameter: " + search)
        usuarios = vuelos.get_all(search)
    else:
        usuarios = vuelos.get_all()
    return render_template("index.html", productos=usuarios, search=search)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
