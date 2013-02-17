import redis
import os

FLIGHT_READY = 100

REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
r = redis.StrictRedis.from_url(REDIS_URL)

def make_key(s):
    return s.strip().replace(" ", '_').lower()

def get_all_systems():

    keys = r.smembers('psas_systems')
    systems = []
    for key in keys:
        s = {}
        s['key']   = key
        s['name']  = r.hget(key, 'name')
        s['desc']  = r.hget(key, 'desc')
        s['parts'] = get_parts(key)
        s['software'] = ["software"]
        systems.append(s)
    return systems

def get_system(key):
    s = {}
    s['key']    = key
    s['name']   = r.hget(key, 'name')
    s['desc']   = r.hget(key, 'desc')
    return s

def get_parts(system):
    keys = r.smembers(system+'_parts')
    parts = []
    for key in keys:
        p = {}
        p['key'] = key
        p['name'] = r.hget(key, 'name')
        parts.append(p)
    return parts

def get_all_parts():
    keys = r.smembers('psas_parts')
    parts = []
    for key in keys:
        p = {}
        p['key'] = key
        p['name'] = r.hget(key, 'name')
        parts.append(p)
    return parts
    

def add_part_from_form(form, system=None):
    #TODO: sanitize
    key = 'psas_part_'+make_key(form['name'])
    r.hset(key, 'name', form['name'])
    r.sadd('psas_parts', key)
    if system:
        r.sadd(system+'_parts', key)

def remove_part(system, key):
    r.srem(system+'_parts', key)

def update_system_from_from(form):
    #TODO: sanitize
    key = form['key']
    r.hset(key, 'name', form['name'])
    r.hset(key, 'desc', form['desc'])

def add_system_from_form(form):
    #TODO: sanitize
    key = 'psas_system_'+make_key(form['name'])
    r.hset(key, 'name', form['name'])
    r.hset(key, 'desc', form['desc'])
    r.sadd('psas_systems', key)

def delete_system(key):
    r.delete(key)
    r.srem('psas_systems', key)
