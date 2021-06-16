# In the URL after: http/s://<server>:port/path type ?name=<name_string> if not added it will default to World

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return HELLO_HTML.format(name)

HELLO_HTML = """
    <html><body>
        <h1>Hello {0}!</h1>
        Click <a href="/time">here</a> for the time.
    </body></html>
    """

@app.route("/time")
def time():
    return f" {TIME_HTML} {datetime.now()}"

TIME_HTML = """
    <html><body>
        The Date and Time are
    </body></html>
    """

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)



