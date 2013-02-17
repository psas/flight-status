import os
from flask import Flask, request, render_template, send_from_directory
import views
import psas
app = Flask(__name__)

@app.route("/")
def index():
    systems = views.show_systems()
    return render_template('index.html',
                           systems=systems)

@app.route("/manage", methods=['GET', 'POST'])
def mange():
    if request.method == 'POST':
        if request.form['key'] == "NEW":
            psas.add_system_from_form(request.form)
        else:
            psas.update_system_from_from(request.form)
    systems = views.show_systems()
    tags = views.show_tags()
    return render_template('manage.html',
                           systems=systems,
                           tags=tags)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.debug = True
    app.run()
