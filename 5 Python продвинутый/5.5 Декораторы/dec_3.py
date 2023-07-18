import requests
import datetime
import json


def cached(cache_size):
    def _decor(old_function):

        CACHE = {}
        def new_function(*args, **kwargs):
 
            key = f'{args}_{kwargs}'
            if key in CACHE:
                print('Результат из кэша:')
                return CACHE[key]
        
            result = old_function(*args, **kwargs)
            if len(CACHE) >= cache_size:
                CACHE.popitem()
            CACHE[key] = result

            return result

        return new_function
    return _decor


@cached(cache_size=100)
def get_people(people_id):
    start = datetime.datetime.now()
    response = requests.get(f'https://swapi.dev/api/people/{people_id}').json()
    end = datetime.datetime.now()
    print(f'{people_id=} время запроса {end-start}')
    return response

for n in [1, 1, 2, 3, 3]:
    print(get_people(n))
