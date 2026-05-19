from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🏠 Home Page</h1>
    <p>Welcome to your site</p>
    <a href="/about">Go to About Page</a>
    """

@app.route("/about")
def about():
    return """
    <h1>ℹ️ About Page</h1>
    <p>This is your second route working on Vercel.</p>
    <a href="/">Back to Home</a>
    """
