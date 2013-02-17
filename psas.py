import redis
import os

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
        s['parts'] = ["parts"]
        s['software'] = ["software"]
        systems.append(s)
    return systems

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
