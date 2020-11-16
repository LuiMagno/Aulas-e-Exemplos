'''
Expressões regulares são padrões de correspondência de texto descritos com uma sintaxe formal. Muitas vezes você ouvirá expressões regulares referidas como 'regex' ou 
'regexp' na conversa. As expressões regulares podem incluir uma variedade de regras, a busca de repetição, a correspondência de texto e muito mais. Ao avançar no Python, 
você verá que muitos dos seus problemas de análise podem ser resolvidos com expressões regulares (eles também são uma pergunta de entrevista comum!).
'''
import re
patterns = ['term1', 'term2']

text = 'This is a string with term1. This is another with term2.'

print(re.search(patterns[0], text))

# Texto para analisar
text = 'This is a string with term1, but it does not have the other term2.'

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text))
    
    # Checa por correspondencia
    if re.search(pattern, text):
        print('\n')
        print('Match was found. \n')
    else:
        print('\n')
        print('No Match was found.\n')

match = re.search(patterns[0], text)
print(match.end())

# Pra mim é um tópico meio desnecessário de ver se eu não sei se vou usar exatamente, não faz parte dos básicos.