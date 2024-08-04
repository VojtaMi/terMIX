from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, json
import os

app = Flask(__name__)

# Global dictionary to store translations
translations = {}


def load_all_translations():
    global translations
    # Load translations for all languages and store in the global dictionary
    translations['en'] = load_translations('en')
    translations['cs'] = load_translations('cs')


def load_translations(lang):
    file_path = os.path.join(app.root_path, 'translations', f'{lang}.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


# Call this function when the application starts
load_all_translations()

def get_translations(lang):
    return translations.get(lang)


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


def redirect_browser_lang():
    # czech for czech and slovak, else english
    browser_lang = request.accept_languages.best_match(['en', 'cs', 'sk'])
    if browser_lang in ['cs', 'sk']:
        return redirect(url_for("home", lang='cs'))
    return redirect(url_for("home", lang='en'))


@app.route('/')
def home():
    lang = request.args.get('lang')
    if not lang:
        return redirect_browser_lang()
    return render_template('index.html', translations=get_translations(lang), lang=lang)


@app.route('/gallery')
def gallery():
    lang = request.args.get('lang')
    return render_template('gallery.html', translations=get_translations(lang), lang=lang)


@app.route('/contacts')
def contacts():
    lang = request.args.get('lang')
    return render_template('contacts.html', translations=get_translations(lang), lang=lang)

@app.route('/drink_menu')
def drink_menu():
    lang = request.args.get('lang')
    return render_template('drink_menu.html', translations=get_translations(lang), lang=lang)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

