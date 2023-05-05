from cache import LRUCache

def main():
    cache = LRUCache(2)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')

    print(cache.get("Jesse")) # James
    print(cache.get("Walter")) # White

    cache.rem('Walter')
    # print(cache.get('Walter')) #

    cache.set('Saul', 'Goodman')
    # print(cache.get('Saul'))

    # cache.set('Saul', 'Goodman')
    # cache.set('Saul1', 'Goodman1')
    # cache.set('Saul2', 'Goodman2')
    # cache.set('Saul3', 'Goodman3')
    # print(cache.get('Saul'))
    # print(cache.get('Saul1'))
    # print(cache.get('Saul2'))
    # print(cache.get('Saul3'))

if __name__ == "__main__":
	main()