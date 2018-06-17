# Imports the Google Cloud client library
import json

from google.cloud import datastore
from google.appengine.api import search

# Instantiates a client
ds = datastore.Client.from_service_account_json("service-account.json")


# Batch job resulted in 504 Deadline exceeded so using single puts
# looks like I should have decreased batch size

def read_json_file(path):
    return json.loads(open(path).read())


def store_categories_datastore():
    categories = read_json_file("categories.json")
    for cat in categories:
        key = ds.key("Category", cat['id'])
        c = datastore.Entity(key=key)
        c.update(cat)
        ds.put(c)
        print('Saved category {}: {}'.format(c['id'], c['name']))


def store_stores_datastore():
    stores = read_json_file("stores.json")
    for store in stores:
        key = ds.key("Store", store['id'])
        s = datastore.Entity(key=key)
        s.update(store)
        ds.put(s)
        print('Saved store {}: {}'.format(s['id'], s['name']))


def store_products_datastore():
    products = read_json_file("products.json")
    for product in products:
        key = ds.key("Product", product['sku'])
        p = datastore.Entity(key=key)
        p.update(product)
        ds.put(p)
        print('Saved product {}: {}'.format(p['sku'], p['name']))

