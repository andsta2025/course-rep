from flask import Flask, render_template, request

app = Flask(__name__)

# This will hold submitted user data temporarily
users = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        # Store data in the dictionary using name as key
        users[name] = email

        return render_template('result.html', name=name, email=email)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)