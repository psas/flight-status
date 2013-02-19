import models

def traverse(key, view):
    view += "<li>"+key.replace('_',' ').title()
    if 'fields' in models.TAXONOMY['types'][key]:
        for field in models.TAXONOMY['types'][key]['fields']:
            view += " (" + field["name"] + ")"
    view += "<ul>"
    for k in models.TAXONOMY['types'][key]['contains']:
        view = traverse(k, view)
    view += "</ul></li>"
    return view

def build_taxonomy():
    top = models.TAXONOMY['top']['site']

    view =  "<ul>"
    view += traverse(top, "")
    view += "</ul>"

    return view

def top_site_list():
    return ["bangarang"]

