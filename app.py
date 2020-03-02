from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Loan Calulation')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About LCS')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():

    if request.method == 'POST':
        form = request.form
        
        #take in user loan information
        #take in loan amount
        LOAN_AMT = float(form['loanAmt'])
        RATE = float(form['rate'])
        PAYMENTS = float(form['payments'])
        YEARS = float(form['years'])

        # Number periodic payments
        n = PAYMENTS * YEARS
        #Periodic interest rate
        i = RATE / n

        discFactor =  ((( 1 + i) ^ n ) - 1 ) / ( i ( 1 + i ) ^ n)

        P = LOAN_AMT / discFactor #these are monthly payments
       
        print(P)

        calculation = "The loan amount calculated is ${0:,.f}".format(P)
        return render_template('estimate.html', display=calculation, pageTitle='Calculated Monthly Payments')



    return render_template('estimate.html', pageTitle='Loan Calulator')

if __name__ == '__main__':
    app.run(debug=True)