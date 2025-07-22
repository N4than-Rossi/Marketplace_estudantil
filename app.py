from flask import Flask, render_template, redirect, url_for, request;
import csv

#ren "C:\Users\bta\AppData\Local\Microsoft\WindowsApps\python.exe" python_disabled.exe
#set PATH=%PATH%;C:\ProgramData\anaconda3;C:\ProgramData\anaconda3\Scripts;C:\ProgramData\anaconda3\Library\bin 

app = Flask(__name__)

@app.get("/")
def index():
  return render_template("index.html")

@app.get("/add")
def show_cadastro():
  return render_template("cadastro.html")

@app.post("/add")
def add_cadastro():
  return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
