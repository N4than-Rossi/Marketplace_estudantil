from flask import Flask, render_template, redirect, url_for, request;
import csv

#ren "C:\Users\bta\AppData\Local\Microsoft\WindowsApps\python.exe" python_disabled.exe
#set PATH=%PATH%;C:\ProgramData\anaconda3;C:\ProgramData\anaconda3\Scripts;C:\ProgramData\anaconda3\Library\bin 

app = Flask(__name__)

@app.get("/")
def index():
  return render_template("home.html")

@app.get("/add")
def show_cadastro():
  return render_template("cadastro.html")

@app.post("/add")
def add_cadastro():

  with open("armazenamento.csv", mode="r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        last_id = 0

        if (len(reader) > 1):
            last_row = reader[-1]
            if last_row:
                last_id = int(last_row[0])
        
        next_id = last_id + 1

        new_data = [
          next_id,
          request.form.get("name"),
          request.form.get("email"),
          request.form.get("password"),
        ]

  with open("armazenamento.csv", mode="a", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_data)

  return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
