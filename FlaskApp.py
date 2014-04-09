import os

from flask import Flask
import jinja2


app = Flask(__name__)

path = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path),
    autoescape=True)


def render(path, **kwargs):
    template = JINJA_ENVIRONMENT.get_template(path)
    return template.render(**kwargs)


@app.route('/')
def hello_world():
    return render('/index.html')


if __name__ == '__main__':
    app.run()
