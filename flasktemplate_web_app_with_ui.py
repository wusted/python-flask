from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return HOME_HTML

HOME_HTML = """
    <html><body>
        <h2> Welcome to this Website </h2>
        <form action="/greet">
            What's your name? <input type="text" name="username"><br>
            What's your favorite color? <input type="text" name="favcolor"><br>
            <input type="submit" value="Continue">
        </form>
    </body></html>
    """

@app.route("/greet")
def greet():
    username = request.args.get("username", "")
    favcolor = request.args.get("favcolor", "")
    if username == "":
        username = "World"
    if favcolor == "":
        msg = "You did not tell me your favorite color"
    else:
        msg = "I like " + favcolor + ", too"

    return GREET_HTML.format(username, msg)

GREET_HTML = """
    <html><body>
        <h2>Hello, {0}</2>
        {1}
    </body></html>
    """

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
