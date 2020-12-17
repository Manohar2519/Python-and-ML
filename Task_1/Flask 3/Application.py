from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def info():
    return render_template('info.html')

@app.route('/educationqualification')
def educationqualification():
    return render_template('educationqualification.html')

@app.route('/Technical_Skills')
def Technical_Skills():
    return render_template('Technical_Skills.html')

@app.route('/Certifications')
def Certifications():
    return render_template('Certifications.html')

@app.route('/Languages_Known')
def Languages_Known():
    return render_template('Languages_Known.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')





if(__name__ == '__main__'):
    app.run(debug = True)
