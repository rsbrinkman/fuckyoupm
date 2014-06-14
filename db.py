import redis

db = redis.StrictRedis(host='localhost', port=6379)

def test():
    db.set('test_key', 'test_successful')
    result = db.get('test_key')
    db.delete('test_key')
    return result

def set_vote(vote, user):
    db.hset('user>%s' % user, 'votes', vote)

def get_votes(user):
    return db.hget('user>%s' % user, 'votes')

def add_user(user):
    db.sadd('users', user)

def get_users():
    return db.smembers('users')
