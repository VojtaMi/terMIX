from flask import render_template, request, redirect, url_for, Response, abort, send_from_directory
from datetime import date
import os

def configure_routes(app):
    supported_languages = {'cs', 'en'}

    def get_translations(lang):
        return app.config['TRANSLATIONS'].get(lang)

    def get_localized_urls(external=False):
        endpoint = request.endpoint
        if not endpoint:
            return (
                url_for('home', lang='cs', _external=external),
                url_for('home', lang='en', _external=external)
            )

        view_args = dict(request.view_args or {})
        if 'lang' not in view_args:
            return (
                url_for('home', lang='cs', _external=external),
                url_for('home', lang='en', _external=external)
            )

        cs_args = dict(view_args)
        en_args = dict(view_args)
        cs_args['lang'] = 'cs'
        en_args['lang'] = 'en'
        cs_url = url_for(endpoint, _external=external, **cs_args)
        en_url = url_for(endpoint, _external=external, **en_args)
        return cs_url, en_url

    @app.url_value_preprocessor
    def validate_lang_in_url(endpoint, values):
        if not values:
            return
        lang = values.get('lang')
        if lang and lang not in supported_languages:
            abort(404)

    @app.context_processor
    def inject_localized_urls():
        cs_url, en_url = get_localized_urls()
        cs_abs_url, en_abs_url = get_localized_urls(external=True)
        return dict(
            cs_url=cs_url,
            en_url=en_url,
            cs_abs_url=cs_abs_url,
            en_abs_url=en_abs_url,
            x_default_abs_url=url_for('home_without_lang', _external=True)
        )

    @app.context_processor
    def inject_current_year():
        return {'current_year': date.today().year}

    @app.route('/')
    def home_without_lang():
        # Czech for Czech and Slovak, else English
        browser_lang = request.accept_languages.best_match(['en', 'cs', 'sk'])
        target_lang = 'cs' if browser_lang in ['cs', 'sk'] else 'en'
        response = redirect(url_for("home", lang=target_lang))
        response.headers['Vary'] = 'Accept-Language'
        return response

    @app.route('/favicon.ico')
    def favicon_ico():
        return send_from_directory(
            app.static_folder,
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )

    @app.route('/favicon.png')
    def favicon_png():
        return send_from_directory(
            app.static_folder,
            'favicon.png',
            mimetype='image/png'
        )

    @app.route('/<lang>/')
    def home(lang):
        mainpage_posters_folder = os.path.join(app.static_folder, "assets/mainpage_posters")
        posters = []

        for fn in sorted(os.listdir(mainpage_posters_folder)):
            if fn.lower().endswith(".avif"):
                posters.append(
                url_for("static", filename=f"assets/mainpage_posters/{fn}")
                )
        return render_template(
            'index.html',
            translations=get_translations(lang),
            lang=lang,
            posters=posters
        )

    @app.route('/<lang>/gallery')
    def gallery(lang):
        return render_template('gallery.html', translations=get_translations(lang), lang=lang)

    @app.route('/<lang>/information')
    def information(lang):
        return render_template('information.html', translations=get_translations(lang), lang=lang)

    @app.route('/<lang>/drink_menu')
    def drink_menu(lang):
        return render_template('drink_menu.html', translations=get_translations(lang), lang=lang)

    @app.route('/<lang>/about')
    def about(lang):
        return render_template('about.html', translations=get_translations(lang), lang=lang)

    @app.route('/<lang>/events')
    def events(lang):
        return render_template('events.html', translations=get_translations(lang), lang=lang)

    @app.route('/robots.txt')
    def robots_txt():
        lines = [
            "User-agent: *",
            "Allow: /",
            "Sitemap: https://club-termix.cz/sitemap.xml"
        ]
        return Response("\n".join(lines), mimetype="text/plain")

    @app.route('/sitemap.xml')
    def sitemap():
        pages = [
            ('home', {'lang': 'cs'}),
            ('home', {'lang': 'en'}),
            ('about', {'lang': 'cs'}),
            ('about', {'lang': 'en'}),
            ('events', {'lang': 'cs'}),
            ('events', {'lang': 'en'}),
            ('information', {'lang': 'cs'}),
            ('information', {'lang': 'en'}),
            ('drink_menu', {'lang': 'cs'}),
            ('drink_menu', {'lang': 'en'}),
            ('gallery', {'lang': 'cs'}),
            ('gallery', {'lang': 'en'}),
        ]

        lastmod = date.today().isoformat()
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]
        for endpoint, kwargs in pages:
            xml_lines.extend([
                '  <url>',
                f'    <loc>{url_for(endpoint, _external=True, **kwargs)}</loc>',
                f'    <lastmod>{lastmod}</lastmod>',
                '  </url>'
            ])
        xml_lines.append('</urlset>')
        return Response('\n'.join(xml_lines), mimetype='application/xml')
