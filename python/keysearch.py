
def key_search(dict,key):
    if key in dict.keys():
        print('present')
        print('value',dict[key])

dict = {'a':'amar','b':'banty','c':'comal'}
key = 'b'
key_search(dict,key)