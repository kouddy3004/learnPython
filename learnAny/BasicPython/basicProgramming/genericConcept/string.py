person = {'name': 'Koushik', 'age': 30}

#Format
sentence = "My name is {name} and my age is {age}".format(**person)
print(sentence)

print(['The numbers are {0}'.format(i) for i in range(1,6)])