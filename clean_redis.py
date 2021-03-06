import sys
import os
import models
import config
import redis

REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
r = redis.StrictRedis.from_url(REDIS_URL)

# Check to see if user asked to delete only one taxonomy type
if len(sys.argv) == 2:
    typ = sys.argv[1]
    delete_type(typ)
    exit()

def delete_type(typ):
    '''Deletes everything related to a single taxonomy type'''
    for obj in models.get_all_of_type(typ):
        for child_type in models.TAXONOMY['types'][typ]['contains']:
            child_obj_key = obj['key']+'-'+child_type+'-children'
            r.delete(child_obj_key)
            print "   - removing", child_obj_key
        r.delete(obj['key'])
        print "   - removing", obj['key']

    list_key = config.ORG.lower()+'-'+typ+'-list'
    r.delete(list_key)
    print " - removing", list_key

# If no arguments delete everything:
print "deleting database..."
for typ in models.TAXONOMY['types']:
    delete_type(typ)
