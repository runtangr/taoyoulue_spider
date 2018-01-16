import redis
from mongoengine import connect


# init mongodb, redis
connect(host='10.3.131.137', port=27037, db='mc', connect=False)

pool_auMessage724 = redis.ConnectionPool(host='redis', port=6379, db=3)
r_auMessage724 = redis.StrictRedis(connection_pool=pool_auMessage724)

pool_A_DxtInformation = redis.ConnectionPool(host='redis', port=6379, db=4)
r_A_DxtInformation = redis.StrictRedis(connection_pool=pool_A_DxtInformation)