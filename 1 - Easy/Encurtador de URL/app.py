import datetime
from string import ascii_uppercase, ascii_lowercase, digits
import string
from random import choice

class UrlShortner:
    def __init__(self, url, url_random_hash, short_url, time_created):
        self.url = url
        self.url_random_hash = url_random_hash
        self.short_url = short_url
        self.time_created = time_created

def url_random_hash_generator( 
    size=6, 
    chars=ascii_uppercase + ascii_lowercase + digits):
    return ''.join(choice(chars) for _ in range(size)) # Working on validator for duplicated url_random_hash

def datetime_creation():
    return datetime.datetime.utcnow

def url_factory(url):
    url_random_hash = url_random_hash_generator()
    short_url = 'localhost:5000' + '/' + url_random_hash
    time_created = datetime.datetime.utcnow()
    #rlShortner.expiration_date = expiration_date
    return UrlShortner(url, url_random_hash, short_url, time_created)

print('URL shortner')
url1 = url_factory(input('Input your URL: '))
print(f'The short url is {url1.short_url}')