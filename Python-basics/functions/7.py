def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

print(greet('en'))         
print(greet('fr'))         
print(greet('pt'))         
print(greet('de'))         
print(greet('sv'))         
print(greet('af'))         