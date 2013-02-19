import models

def traverse(key, view):
    view += "<li>"+key.replace('_',' ').title()
    view += "<ul>"
    for k in models.TAXONOMY['types'][key]['contains']:
        view = traverse(k, view)
    view += "</ul></li>"
    return view

def build_taxonomy():
    top = models.TAXONOMY['top']

    view =  "<ul>"
    view += traverse(top, "")
    view += "</ul>"

    return view

def list_types():
    types = []
    for key in models.TAXONOMY['types']:
        print key
        types.append(key.replace('_',' ').title())
    return types

def top_site_list():
    return ["bangarang"]

