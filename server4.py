from flask import Flask, request, redirect, render_template
app = Flask(__name__)
@app.route('/')
def showSurvey():
    return render_template('survey.html')
@app.route('/result', methods=['POST'])
def getSurvey():
    return render_template('result.html',name=request.form['name'], email=request.form['email'], location=request.form ['location'], favorite_language= request.form['favorite_language'], comment=request.form ['comment'])
app.run(debug = True)