import datetime
from string import ascii_uppercase, ascii_lowercase, digits
import string
from random import choice

class UrlShortner:
    def __init__(self, url):
        self.url = url

def url_random_hash_generator( 
    size=6, 
    chars=ascii_uppercase + ascii_lowercase + digits):
    return ''.join(choice(chars) for _ in range(size)) # Working on validator for duplicated url_random_hash

def datetime_creation():
    return datetime.datetime.utcnow

def url_factory(url):
    UrlShortner.url = url
    UrlShortner.url_random_hash = url_random_hash_generator()
    UrlShortner.short_url = 'localhost:5000' + '/' + UrlShortner.url_random_hash
    UrlShortner.time_created = datetime.datetime.utcnow()
    #rlShortner.expiration_date = expiration_date
    return UrlShortner(url)

# url1 = url_factory('google.com/')

# print (f'''
# {url1.url}, 
# {url1.url_random_hash}, 
# {url1.short_url}, 
# {url1.time_created}''')

print('URL shortner')
url1 = url_factory(input('Input your URL: '))
print(f'The short url is {url1.short_url}')