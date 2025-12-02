from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages


# Home page
@app.route('/')
def index():
    return render_template('index.html')
 # Register page
@app.route('/register')
def register():
    return render_template('register.html')


# Display stored registrations
@app.route('/view')
def view_registrations():
    # opens json file in read mode
    with open('registrations.json', 'r') as file:
        #loads the data
        data = json.load(file)

    return render_template('view.html', registrations=data)

@app.route('/submit', methods=['POST'])
def submit_form():
   #recives submitted data and stores in a vairable.
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']
    gender = request.form['gender']
    date_of_birth = request.form['date_of_birth']
    phone_number = request.form['phone_number']
    family_size = request.form['family_size']
    medical_con = request.form['Medical_con']

    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    # Add the new registration
    data.append({'name': name, 'country': country, 'age': age, 'gender': gender, 'date_of_birth': date_of_birth, 'phone_number': phone_number, 'family_size': family_size, 'medical_con': medical_con})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

