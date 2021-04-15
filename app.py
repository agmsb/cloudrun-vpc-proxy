from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def landing_page():
    return "Please use the path /ip_addr/<Private-IP> to use this proxy."

@app.route("/ip_addr/<string:ip>")
def proxy(ip):
    return requests.get("http://"+ip).content
