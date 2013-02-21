import config
import os
import redis

REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
r = redis.StrictRedis.from_url(REDIS_URL)

TAXONOMY = {
    "types": {
        "launch":   {"contains": ["system"]},
        "system":   {"contains": ["module"]},
        "module":   {"contains": ["part", "software"]},
        "part":     {"contains": []},
        "software": {"contains": []},
    },
    "top": "launch",
}

def gen_key(name):
    return name.replace(' ', '-').lower()


def get_fields(typ):
    fields = [
        {
            'key':  "name",
            'name': "Name",
            'type': "text",
        },
        {
            'key':  "desc",
            'name': "Description",
            'type': "textarea",
        },
    ]
    if typ == TAXONOMY['top']:
        fields.append({
            'key': "date",
            'name': "Date/Time",
            'type': "date",
        })
    return fields


def add_new(typ, form):
    #TODO: sanitize
    name = form['name']
    desc = form['desc']
    key  = gen_key(name)
    key  = config.ORG.lower()+'-'+typ+'-'+key

    set_key = config.ORG.lower()+'-'+typ+'-list'

    r.hset(key, 'name', name)
    r.hset(key, 'desc', desc)
    r.sadd(set_key, key)

def delete(typ, key):
    set_key = config.ORG.lower()+'-'+typ+'-list'

    r.srem(set_key, key)
    r.delete(key)

def update(typ, form):
    key = form['key']
    set_key = config.ORG.lower()+'-'+typ+'-list'
    for field in get_fields(typ):
        r.hset(key, field['key'], form[field['key']])
    r.sadd(set_key, key)

def get_all_of_type(typ):
    set_key = config.ORG.lower()+'-'+typ+'-list'
    keys = r.smembers(set_key)
    fields = get_fields(typ)
    l = []
    for key in keys:
        p = {}
        p['key']  = key
        for field in get_fields(typ):
            p[field['key']] = r.hget(key, field['key'])
        mem = []
        nmem = 0
        for member_type in TAXONOMY['types'][typ]['contains']:
            m = {}
            m['name'] = member_type
            member_list_key = config.ORG.lower()+'-'+typ+'-children-'+member_type
            member_list = []
            for member_key in r.smembers(member_list_key):
                c = {}
                c['name'] = r.hget(member_key, 'name')
                c['desc'] = r.hget(member_key, 'desc')
                member_list.append(c)
                nmem += 1
            m['members'] = member_list
            mem.append(m)
        p['members'] = mem
        p['n_members'] = nmem
        l.append(p)
    return l
