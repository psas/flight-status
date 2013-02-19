import os
from flask import Flask, request, render_template, send_from_directory
import views
import models
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',  page="home")

@app.route('/login')
def login():
    return render_template('login.html',  page="login")

@app.route('/api')
def api():
    types = views.list_types()
    tree  = views.build_taxonomy()
    return render_template('api.html', page="api", api=tree, typelist=types)

@app.route('/admin')
def admin():
    toplist = views.top_site_list()
    return render_template('admin.html', toplist=toplist)

@app.route('/manage/<taxonomy>')
def manage(taxonomy):
    if taxonomy not in models.TAXONOMY['types']:
        return render_template("404.html"), 404
    name = views.key2name(taxonomy)
    collection = views.get_all(taxonomy)
    return render_template('manage.html', name=name, collection=collection)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0') # Enable local network access
