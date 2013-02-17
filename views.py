import psas

def show_systems():
    systems = psas.get_all_systems()
    l = []
    for system in systems:
        system['status'] = "75%"
        l.append(system)

    return l

def show_tags():
    tags = [{"name": "Critical", "color": "Red"}]
    return tags
