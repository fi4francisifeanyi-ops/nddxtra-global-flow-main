from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return """
    <h1>Website works!</h1>
    <p>Your vercel deployment is successful.</p>
    """