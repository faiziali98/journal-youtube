from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage for journal entries
journal_entries = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        baby_name = request.form['baby_name']
        start_date = request.form['start_date']
        return redirect(url_for('start_journaling', baby_name=baby_name, start_date=start_date))
    return render_template('index.html')

@app.route('/start_journaling', methods=['GET', 'POST'])
def start_journaling():
    if request.method == 'POST':
        events = request.form['events']
        time = request.form['time']
        amount = request.form['amount']
        journal_entries.append({
            'events': events,
            'time': time,
            'amount': amount
        })
    start_date = request.args.get('start_date') or request.form.get('start_date')
    baby_name = request.args.get('baby_name') or  request.form.get('baby_name')
    start_date = request.args.get('start_date')
    return render_template('start_journaling.html', baby_name=baby_name, start_date=start_date, journal_entries=journal_entries)

if __name__ == '__main__':
    app.run(debug=True)
