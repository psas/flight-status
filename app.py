import os
from flask import Flask, render_template, send_from_directory
import views
app = Flask(__name__)

@app.route("/")
def index():
    systems = views.show_systems()
    return render_template('index.html',
                           systems=systems)

@app.route("/manage")
def mange():
    systems = views.show_systems()
    return render_template('manage.html',
                           systems=systems)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.debug = True
    app.run()
