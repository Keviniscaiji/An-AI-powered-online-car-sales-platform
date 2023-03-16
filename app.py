from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder='static')
app.debug = True


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/cars')
def cars():
    return render_template('car.html')


@app.route('/car-single')
def car_single():
    return render_template('car-single.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/blog-single')
def blog_single():
    return render_template('blog-single.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True)
