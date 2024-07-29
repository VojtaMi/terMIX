from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    lang = request.args.get('lang', 'en')
    if lang == 'en':
        return render_template('en/index.html')
    return render_template('cz/index.html')

if __name__ == "__main__":

    app.run(debug=True)