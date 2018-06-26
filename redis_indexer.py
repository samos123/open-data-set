import os
import json
import redis
import logging
from walrus import Database

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
#redis_client = redis.StrictRedis(host=redis_host, port=redis_port)
walrus_db = Database(host=redis_host, port=redis_port)
ac = walrus_db.autocomplete()

def read_json_file(path):
    return json.loads(open(path).read())

def populate_index():
    products = read_json_file("products.json")
    for product in products:
        try:
            ac.store(obj_id=product['sku'], title=product['name'])
        except Exception as e:
            logging.exception("Issue creating index for product id: %s name: %s",
                              product['sku'], product['name'])


if __name__ == "__main__":
    populate_index()
    print(ac.search("Bat"))
