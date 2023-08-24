from flask import Flask
#creating object
app=Flask(__name__)# app is the application
@app.route('/')
def home():
    return('Server hosted by Mojesh')
if(__name__)=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)