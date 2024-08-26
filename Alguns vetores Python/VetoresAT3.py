vogais = ['a','e','i','o','u']
vetor = ['a','b','c','d','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
vogais_localizadas = []
for cárater in vetor:
    if cárater in vogais:
        vogais_localizadas.append(cárater)
        print("As vogais encontradas são: ", vogais_localizadas)
        

