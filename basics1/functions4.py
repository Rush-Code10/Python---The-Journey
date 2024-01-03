"""
def greet(lang):
    if lang == 'es':
        print("HOLA")
    elif lang == 'fr':
        print("BONJOUR")
    else:
        print("HELLO")

greet("es")
greet("es")
greet("wdfg")
greet("wefgnb")
"""
def greet(lang):
    if lang == 'es':
        return 'HOLA'
    elif lang == 'fr':
        return 'BONJOUR'
    else:
        return 'HELLO'
    
print(f"{greet('es')} SPAIN")
print(f"{greet('fr')} FRANCE")
print(f"{greet('english')} ENGLAND")