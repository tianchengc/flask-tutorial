from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/user/<name>/mark/<int:mark>', methods=['GET'])
def get_user_mark(name, mark):
    return render_template('mark.html', name=name, mark=mark)