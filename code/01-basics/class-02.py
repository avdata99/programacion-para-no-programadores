
class Person:
    names = []
    other = 'NO'
 
jorge = Person()
jorge.names.append('Jorge')
jorge.other = 'YES'

luis = Person()
print(luis.names)
# Shows ['Jorge']
print(luis.other)
# Shows NO
