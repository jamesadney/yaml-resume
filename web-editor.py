import json

from flask import Flask, render_template, make_response
from flask.ext import uploads
import yaml

#Config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def resume_editor():
    return render_template('index.html')

@app.route('/_load_resume')
def load_resume():
    with open("private_resumes/mosier.yml") as f:
        resume = yaml.load(f)

    response = make_response(json.dumps(resume))
    response.mimetype = "application/json"
    return response

@app.route('/_generate_pdf')
def generate_pdf():
    pass

if __name__ == '__main__':
    app.run()
