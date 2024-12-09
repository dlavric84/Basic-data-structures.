calls = 0
def count_calls ():
    global calls
    calls+=1
def string_info (str):
    count_calls()
    return (len(str), str.upper(), str.lower())
def is_contains (str, list_to_search):
    count_calls()
    return str.upper() in [s.upper() for s in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('cycle', ['recycle', 'cyclic'])) 
print(calls)
