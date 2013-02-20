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

    print key, set_key
    r.srem(set_key, key)
    r.delete(key)

def get_all_type(typ):
    set_key = config.ORG.lower()+'-'+typ+'-list'
    keys = r.smembers(set_key)
    l = []
    for key in keys:
        p = {}
        p['key']  = key
        p['name'] = r.hget(key, 'name')
        p['desc'] = r.hget(key, 'desc')
        l.append(p)
    return l
