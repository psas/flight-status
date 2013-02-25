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
    entries = models.get_all_of_type(key)
    return entries

def traverse_tree(typ, key, tree):
    ctypes = []
    for child_type in models.TAXONOMY['types'][typ]['contains']:
        c = {}
        c['key'] = child_type
        c['name'] = key2name(child_type)
        children = models.get_children(child_type, key)
        if len(children) < 1:
            break
        c['list'] = children
        for child in children:
            traverse_tree(child_type, child['key'], child)
        ctypes.append(c)
    tree['children'] = ctypes

def get_tree(typ, key):
    tree = {}
    traverse_tree(typ, key, tree)
    return tree['children']

def get_current_tree():
    tree = get_tree('launch', 'psas-launch-l-10')
    return tree

def top_site_list():
    tops = []
    for entry in models.get_all_of_type(models.TAXONOMY['top']):
        tops.append(entry['name']+'  ('+entry['desc']+')')
    return tops

