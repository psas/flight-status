import psas

def show_systems():
    systems = psas.get_all_systems()
    l = []
    for system in systems:
        system['status'] = "75%"
        for part in system['parts']:
            part['status'] = 'Go'
            part['badge'] = "success"
            #if part['status'] == psas.FLIGHT_READY:
            #    part['status'] = 'Go'
            #    part['badge'] = "success"
        l.append(system)

    return l

def show_system(key):
    s = psas.get_system(key)
    return s

def show_parts(key):
    parts = psas.get_parts(key)
    return parts

def show_all_parts():
    parts = psas.get_all_parts()
    return parts

def show_tags():
    tags = [{"name": "Critical", "color": "Red"}]
    return tags

def list_all_parts():
    parts = psas.get_all_parts()
    names = []
    for part in parts:
        names.append(part['name'])
    return names
