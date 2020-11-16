'''
Vamos saber o que está deixando nosso código rápido ou lento com o Timeit
'''
import timeit # criar string de 0 a 99

string = '-'.join(str(n) for n in range(100))
print(string)

timeit.timeit('string = '-'.join(str(n) for n in range(100))')