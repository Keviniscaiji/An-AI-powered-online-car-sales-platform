from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder='static')
app.debug = True


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/cars')
def cars():
    return render_template('car.html')


if __name__ == '__main__':
    app.run(debug=True)
