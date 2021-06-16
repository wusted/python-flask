from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return HELLO_HTML

HELLO_HTML = """
    <html><body>
        <h1>Hello, world!</h1>
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



