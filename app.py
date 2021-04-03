from pytube import YouTube
from flask import Flask, redirect, url_for, render_template, request, session, flash, send_file
import time
import os
app = Flask(__name__)
app.secret_key = "hello"

def verificar():
    diretorio = os.listdir()
    for i in diretorio:
        if i[-3:] == "mp4":
            os.remove(i)

@app.route("/",  methods=["POST", "GET"])
def home():
    if request.method == "POST":
        verificar()
        
        url = request.form["urlpoura"]

        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()

        path = f"{stream.default_filename}"
        return send_file(path, as_attachment=True)
    else:
        verificar()
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)