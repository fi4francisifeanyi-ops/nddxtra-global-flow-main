from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
  return"<h1>vercel Flask deployment works!</h1>"
    
