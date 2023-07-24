from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    return '|||'.join([f'{k}: {v}' if v else f'{k}: {None}' for k, v in dict(request.form).items()])


if __name__ == '__main__':
    app.run(debug=True)

