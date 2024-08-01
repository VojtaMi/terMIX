from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    lang = request.args.get('lang')
    if not lang:
        browser_lang = request.accept_languages.best_match(['en', 'cs', 'sk'])
        if browser_lang in ['cs', 'sk']:
            return redirect(url_for('home', lang='cs'))
        return redirect(url_for('home', lang='en'))

    if lang == 'cs':
        return render_template('cs/index.html')
    return render_template('en/index.html')

@app.route('/gallery')
def gallery():
    lang = request.args.get('lang')

    if lang == 'cs':
        return render_template('cs/gallery.html')
    return render_template('en/gallery.html')

if __name__ == "__main__":

    app.run(debug=True)