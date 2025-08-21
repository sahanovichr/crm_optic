from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# временное хранилище (для теста)
clients = []

@app.route('/')
def index():
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        client = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'birthday': request.form['birthday']
        }
        clients.append(client)
        return redirect(url_for('index'))
    return render_template('add_client.html')

if __name__ == '__main__':
    app.run(debug=True)# Flask app will be here
