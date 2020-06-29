from flask import Flask
app = Flask(__name__)

@app.route('/api/detectcard', methods=['POST'])

def detectcard():
    return "Hello World!"
