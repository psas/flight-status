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

def get_all_base():
    bases = []
    for key in models.TAXONOMY['types']:
        if len(models.TAXONOMY['types'][key]['contains']) == 0:
            items = []
            for item in models.get_all_of_type(key):
                i = {}
                i['name'] = item['name']
                i['desc'] = item['desc']
                try:
                    i['status'] = float(item['status'])
                except:
                    i['status'] = 0
                if i['status'] < 100:
                    items.append(i)
            items = sorted(items, key=lambda item: item['status'])
            bases.append({'key': key, 'name': key2name(key), 'list': items})
    return bases

def traverse_tree(typ, key, tree):
    ctypes = []
    total_status = 0
    n_members = 0
    for child_type in models.TAXONOMY['types'][typ]['contains']:
        c = {}
        c['key'] = child_type
        c['name'] = key2name(child_type)
        children = models.get_children(child_type, key)
        if len(children) < 1:
            break
        c['list'] = children
        for child in children:
            if "status" in child:
                total_status += child['status']
            n_members += 1
            traverse_tree(child_type, child['key'], child)
        ctypes.append(c)
    if n_members > 0:
        tree['status'] = total_status / float(n_members)
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

