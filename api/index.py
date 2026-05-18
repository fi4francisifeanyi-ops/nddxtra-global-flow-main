from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Website</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: #1e293b;
                padding: 40px;
                border-radius: 12px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 My Website is Live</h1>
            <p>Deployed successfully on Vercel</p>
        </div>
    </body>
    </html>
    """
    """
    
