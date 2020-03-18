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
app.secret_key = "Må byttes ut før GO-live"


COVID19_DASHBOARD_LINK = "https://eu1.ca.analytics.ibm.com/bi/?perspective=dashboard&amp;pathRef=.public_folders%2FCOVID19%2FCOVID-19%2BTest&amp;ui_appbar=false&amp;ui_navbar=false&amp;shareMode=embedded&amp;action=view&amp;mode=dashboard&amp;subView=model00000170ef703302_00000000"
# os.environ["COVID19_DASHBOARD_LINK"]


@app.route("/", methods=["GET", "POST"])
def init():

    return render_template("index.html", dashboard_link=COVID19_DASHBOARD_LINK)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
