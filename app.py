from flask import Flask, render_template, request
app = Flask(__name__)
def conv1(grade):
    if grade == 'A':
        return 20
    elif grade == 'B':
        return 17.5
    elif grade == 'C':
        return 15
    elif grade == 'D':
        return 12.5
    elif grade == 'E':
        return 10
    elif grade == 'S':
        return 5
    elif grade == 'U':
        return 0
def conv2(grade):
    if grade == 'A':
        return 10
    elif grade == 'B':
        return 8.75
    elif grade == 'C':
        return 7.5
    elif grade == 'D':
        return 6.25
    elif grade == 'E':
        return 5.0
    elif grade == 'S':
        return 2.5
    elif grade == 'U':
        return 0

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/cal/")
def cal():
    return render_template("cal.html")

@app.route("/form/", methods = ['POST','GET'])
def form():
    if request.method == 'POST':
        return render_template("rp_cal.html", \
        pw = request.form['pw'], \
        MT = request.form['MT'])
    else:
        return render_template('cal.html')
   
@app.route("/result/", methods = ['POST','GET'])

def result():
    if request.method == 'POST':
        H21M = request.form['H2 Subject 1']
        H22M = request.form['H2 Subject 2']
        H23M = request.form['H2 Subject 3']
        H1M = request.form['H1 Subject']
        GPM = request.form['General Paper']
        data = dict(H21 = [H21M, conv1(H21M)],
        H22 = [H22M, conv1(H22M)],
        H23 = [H23M, conv1(H23M)],
        H1 = [H1M, conv2(H1M)],
        GP = [GPM, conv2(GPM)])
        total = conv1(H21M) + conv1(H22M) + conv1(H23M) + conv2(H1M) + conv2(GPM)
        if request.form['pw'] == 'Yes' and request.form['mt'] == 'Yes':
            total += conv2(request.form['project work']) +  conv2(request.form['Mother Tongue'])
            total = total * 0.9
            PWM = request.form['project work']
            MTM = request.form['Mother Tongue']
            data['total'] = total
            data['PW'] = [PWM,conv2(PWM)]
            data['MT'] = [MTM,conv2(MTM)]
            return render_template("result.html", data = data, tt = 90, status = 'both')
        elif request.form['pw'] == 'No' and request.form['mt'] == 'No':
            data['total'] = total
            return render_template("result.html", data = data, tt = 80, status = 'neither')
        elif request.form['pw'] == 'Yes' and request.form['mt'] == 'No':
            total += conv2(request.form['project work'])
            data['total'] = total
            PWM = request.form['project work']
            data['PW'] = [PWM,conv2(PWM)]
            return render_template("result.html",data = data, tt = 90, status = 'pw')
        else:
            total += conv2(request.form['Mother Tongue'])
            data['total'] = total
            MTM = request.form['Mother Tongue']
            data['MT'] = [MTM,conv2(MTM)]
            return render_template("result.html", data = data, tt = 90, status = 'mt')
    else:
        return render_template('rp_cal.html')

if __name__ == '__main__':
    app.run(debug = True)





