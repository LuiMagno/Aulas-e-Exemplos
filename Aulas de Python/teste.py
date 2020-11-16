def filter_words(lista, letra):

    return filter(lambda a: a[0] == letra, lista)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']

print(filter_words(l,'h'))