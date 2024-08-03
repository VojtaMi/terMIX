from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, json

app = Flask(__name__)


# url for different language variants
def get_localized_urls():
    current_url = request.full_path
    if 'lang=en' in current_url:
        cs_url = current_url.replace('lang=en', 'lang=cs')
        en_url = current_url  # Already in English
    else:
        cs_url = current_url  # Already in Czech
        en_url = current_url.replace('lang=cs', 'lang=en')
    return cs_url, en_url


@app.context_processor
def inject_localized_urls():
    cs_url, en_url = get_localized_urls()
    return dict(cs_url=cs_url, en_url=en_url)


@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}


def load_translations(lang):
    file_path = f'translations/{lang}.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def match_browser_lang():
    # czech for czech and slovak, else english
    browser_lang = request.accept_languages.best_match(['en', 'cs', 'sk'])
    if browser_lang in ['cs', 'sk']:
        return 'cs'
    return 'en'


@app.route('/')
def home():
    lang = request.args.get('lang')
    if not lang:
        lang = match_browser_lang()
    translations = load_translations(lang)
    return render_template('index.html', translations=translations)


@app.route('/gallery')
def gallery():
    lang = request.args.get('lang')

    if lang == 'cs':
        return render_template('cs/gallery.html')
    return render_template('en/gallery.html')


@app.route('/contacts')
def contacts():
    lang = request.args.get('lang')

    if lang == 'cs':
        return render_template('cs/contacts.html')
    return render_template('en/contacts.html')


if __name__ == "__main__":
    app.run(debug=True)
