import models

def traverse(key, view):
    view += "<li>"+key2name(key)
    view += "<ul>"
    for k in models.TAXONOMY['types'][key]['contains']:
        view = traverse(k, view)
    if len(models.TAXONOMY['types'][key]['contains']) < 1:
        view += "<li>[Issue]</li>"
    view += "</ul></li>"
    return view

def build_taxonomy():
    top = models.TAXONOMY['top']

    view =  "<ul>"
    view += traverse(top, "")
    view += "</ul>"

    return view

def key2name(key):
    return key.replace('_',' ').title()

def list_types():
    types = []
    for key in models.TAXONOMY['types']:
        types.append({'key': key, 'name': key2name(key)})
    return types

def get_all(key):
    return []

def top_site_list():
    return ["bangarang"]

