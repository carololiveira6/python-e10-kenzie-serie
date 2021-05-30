from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/series', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        pass

pass