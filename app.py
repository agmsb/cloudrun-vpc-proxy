from flask import Flask
import requests
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def landing_page():

    return "Please use the path /ip_addr/<Private-IP> to use this proxy."


@app.route("/ip_addr/<path:path>")
def proxy(path):

    r = requests.get("http://"+path)

    if r.ok:

        # by default, we are expecting JSON
        try:
            return r.json()

        except:

            # quick hack - assuming exception from non-JSON return
            print("non-JSON reply received - returning text payload")
            return r.text

    else:

        return "Error accessing endpoint {endpoint}".format(endpoint=path)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
