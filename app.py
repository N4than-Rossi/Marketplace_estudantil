from flask import Flask, render_template, redirect, url_for, request;
import csv

app = Flask(__name__)

app.get("/add")
def index():
  return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
