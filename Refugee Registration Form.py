from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')


# Display stored registrations (students will add JSON reading code here)
@app.route('/view')
def view_registrations():
    with open('registrations.json', 'r') as file:
        data = json.load(file)
    return render_template('view.html', registrations=data)

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']
    gender = request.form['male_gender']



    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    # Add the new registration
    data.append({'name': name, 'country': country, 'age': age, 'gender': gender})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

