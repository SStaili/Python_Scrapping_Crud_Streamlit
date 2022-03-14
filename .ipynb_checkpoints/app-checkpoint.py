#from flask import Flask,render_template, request, redirect, url_for,jsonify, json, Response
from flask import Flask, render_template
from flask_pymongo import PyMongo
from IPython.core.display import HTML
from pymongo import MongoClient
from pathlib import Path
import pandas as pd
from bs4 import *
import requests 
import pymongo
import os
import csv
import json
  
app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/razer"

mongo = PyMongo(app)

UPLOAD_FOLDER = "static/assets"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/razer")
def home_page():
    computer = mongo.db.computer.find({})
    return render_template("razer.html",computer=computer)

if __name__ == "__main__":
    app.run(debug=True)