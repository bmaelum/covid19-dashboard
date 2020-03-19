from wtforms import SubmitField, TextField, TextAreaField, RadioField, BooleanField
import json
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import pandas as pd
from flask import Flask, render_template, send_file, make_response, url_for
import pickle
import base64
import numpy as np
import requests
import os


app = Flask(__name__)


COVID19_DASHBOARD_LINK = os.environ["COVID19_DASHBOARD_LINK"]


@app.route("/", methods=["GET", "POST"])
def init():

    print(COVID19_DASHBOARD_LINK)

    return render_template("index.html", dashboard_link=COVID19_DASHBOARD_LINK)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
