import os
from flask import Flask, request, render_template, send_from_directory
import views
import psas
app = Flask(__name__)

@app.route('/')
def index():
    systems = views.show_systems()
    return render_template('index.html',
                           systems=systems)

@app.route('/manage', methods=['GET', 'POST'])
def mange():
    if request.method == 'POST':
        if request.form['key'] == "NEW":
            psas.add_system_from_form(request.form)
        elif "DELETE" in request.form['key']:
            key = request.form['key'][6:]
            psas.delete_system(key)
        else:
            psas.update_system_from_from(request.form)
    systems = views.show_systems()
    tags = views.show_tags()
    return render_template('manage.html',
                           systems=systems,
                           tags=tags)

@app.route('/manage/<system_key>', methods=['GET', 'POST'])
def manage_system(system_key):
    if request.method == 'POST':
        if request.form['key'] == "NEW":
            psas.add_part_from_form(request.form, system_key)
        elif "REM" in request.form['key']:
            key = request.form['key'][3:]
            psas.remove_part(system_key, key)
        elif request.form['key'] == "ADD":
            psas.add_part_from_form(request.form, system_key)
        else:
            psas.update_part_from_form(request.form)

    system = views.show_system(system_key)
    parts = views.show_parts(system_key)
    all_parts = views.list_all_parts()
    return  render_template('system_manage.html',
                            system=system,
                            parts=parts,
                            allparts=all_parts)

@app.route('/parts', methods=['GET', 'POST'])
def parts():
    parts = views.show_all_parts()
    return render_template('part_manage.html',
                            parts=parts)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0') # Enable local network access
