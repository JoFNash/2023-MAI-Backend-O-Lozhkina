from cache import LRUCache

def main():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')

    cache.get('Jesse')  # вернёт 'James'
    print(cache.get('Jesse'))

    cache.rem('Walter')
    cache.get('Walter')  # вернёт ''

    cache.set('Tuko', 'Salamanka')
    print(cache.get('Tuko'))

if __name__ == "__main__":
	main()