from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = OrderedDict()
    time = 0
    
    for city in cities:
        key = city.lower()
        if key in cache:
            time += 1
            cache.move_to_end(key)
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.popitem(last = False)
            cache[key] = True
            
    return time