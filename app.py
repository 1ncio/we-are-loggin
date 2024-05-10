from flask import Flask, send_from_directory, render_template, request
import requests
from settings import *

app = Flask(__name__)

@app.get("/jammin.mp4")
def jammin():
  return send_from_directory(app.static_folder, "jammin.mp4")

@app.get("/")
def root():
  return render_template("index.html")

def sanatize(text):
  escaped_text = ""
  for char in text:
    if char in "<@":
      escaped_text += '\\' + char
    else:
      escaped_text += char
  return escaped_text

@app.post("/troll")
def track():
  requests.post(WEBHOOK, json={"content": sanatize("\n".join(request.json["memes"]))})
  return ""

if __name__ == "__main__":
  app.run(host=HOST, port=PORT, debug=DEBUG)