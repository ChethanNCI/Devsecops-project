from flask import Flask,render_template
from flask import Flask, render_template, request, redirect, url_for
import os
import json
app = Flask(__name__)
@app.route("/")
def hello_world():
  return render_template('home.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
