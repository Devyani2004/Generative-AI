##bulding urls Dynamically
## variable rules and url building
##integrate html with flask
##http verb get and post

##jinja2 template
###integrating css and js with flask
'''
{%...%} for statements
{{ }} expressions to print output
{#....#} this is for comment
'''
from flask import Flask, redirect, url_for, render_template, request

app= Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    if score >= 33:
        res = "pass"
    else:
        res = "fail"

    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and has scored " +str(score)

# Result Checker
@app.route('/results/<int:score>')
def results(score):
    result=""
    if score<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=score))

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0

    if request.method=='POST':
        science= float(request.form['science'])
        maths= float(request.form['maths'])
        c= float(request.form['c'])
        datascience= float(request.form['datascience'])
        genai= float(request.form['genai'])
        total_score=(science+maths+c+datascience+genai)/5

    res=""

   
    return redirect(url_for('success', score= total_score))


    



if __name__=='__main__':
    app.run(debug=True)

