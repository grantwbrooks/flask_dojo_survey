from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_name():
    print "Name Below"
    name = request.form['yourname']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print name
    print location
    print language
    print comment
    return render_template('result.html', name=name, location=location, language=language, comment=comment )


app.run(debug=True)