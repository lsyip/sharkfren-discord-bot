from flask import Flask
from threading import Thread

# Code from freeCodeCamp
# We're making this a Flask app so that we have a URL "anchor" point to keep the bot running through UptimeRobot.com
app = Flask("")

# Returns text on the home page of our app.
@app.route('/')
def home():
  return "Hey, I'm awake!"


# Specifies host and port running points 
def run():
  app.run(host='0.0.0.0', port=8080)


# Keeps the app/bot running 24/7
def stay_awake():
  t = Thread(target=run)
  t.start()
