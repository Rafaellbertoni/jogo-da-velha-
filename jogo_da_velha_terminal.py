import random

def animais() -> str:
    animais = ["cachorro", "gato", "elefante", "girafa", "leao", "tigre", "macaco", "cavalo", "coelho", "urso", "lobo", "raposa", "zebra", "canguru", "pinguim", "golfinho", "tartaruga", "crocodilo", "hipopotamo", "rinoceronte", "jacare", "tucano", "arara", "onca", "preguica", "morcego", "esquilo", "camelo", "avestruz", "gorila"]
    palavra_secreta = random.choice(animais)
    
    return palavra_secreta

def paises() -> str:
    paises = ["brasil", "argentina", "chile", "peru", "colombia", "uruguai", "paraguai", "bolivia", "equador", "venezuela", "mexico", "canada", "portugal", "espanha", "franca", "italia", "alemanha", "inglaterra", "russia", "china", "japao", "coreia", "india", "australia", "egito", "marrocos", "africa", "canada", "grecia", "suecia"]
    palavra_secreta = random.choice(paises)
    
    return palavra_secreta

def frutas() -> str:
    frutas = ["banana", "morango", "abacaxi", "melancia", "uva", "maca", "laranja", "manga", "abacate", "mamao", "pera", "kiwi", "limao", "goiaba", "caju", "acerola", "maracuja", "ameixa", "pessego", "coco", "figo", "framboesa", "amora", "jaca", "tangerina", "melao", "carambola", "graviola", "pitaya", "romã"]
    palavra_secreta = random.choice(frutas)
    
    return palavra_secreta

def main():
    continuar = True
    while continuar:
        print('[animais]\n[paises]\n[frutas]')
        topico = input('qual topico você deseja escolher? ').lower()
        
        if topico == 'animais': 
            palavra_secreta = animais()
            qnts_letras = len(palavra_secreta)
            mostrar = ['_'] * qnts_letras
            tentativas = 7
            
            for i in range(6):
                print('Palavra: ' + " ".join(mostrar))
                print(f'Tentativas: {tentativas - 1}')
                letra_usuario = input('digite uma letra: ')
                for i, letra in enumerate(palavra_secreta):
                    if letra_usuario == letra:
                        mostrar[i] = letra_usuario
                tentativas -= 1
                
            print(f'a palavra era: {palavra_secreta}')
                                 
            continuar2 = input('deseja jogar denovo? S/N ')
            if continuar2 == 'N':
                continuar = False
            elif continuar != 'S':
                print('Erro: digitação incorreta')
                continuar = False
                        
                        
        elif topico == 'paises':
            palavra_secreta = paises()
            qnts_letras = len(palavra_secreta)
            mostrar = ['_'] * qnts_letras
            tentativas = 7
            
            for i in range(6):
                print('Palavra: ' + ' '.join(mostrar))
                print(f'Tentativas: {tentativas - 1}')
                letra_usuario = input('digite uma letra: ')
                for i, letra in enumerate(palavra_secreta):
                    if letra_usuario == letra:
                        mostrar[i] = letra_usuario
                tentativas -= 1
            
            print(f'a palavra era: {palavra_secreta}')
                        
            continuar2 = input('deseja jogar denovo? S/N ')
            if continuar2 == 'N':
                continuar = False
            elif continuar != 'S':
                print('Erro: digitação incorreta')
                        
        
        
        elif topico == 'frutas':
            palavra_secreta = frutas()
            qnts_letras = len(palavra_secreta)
            mostrar = ['_'] * qnts_letras
            tentativas = 7
            
            for i in range(6):
                print('Palavra: ' + ' '.join(mostrar))
                print(f'Tentativas: {tentativas - 1}')
                letra_usuario = input('digite uma letra: ')
                for i, letra in enumerate(palavra_secreta):
                    if letra_usuario == letra:
                        mostrar[i] = letra_usuario
                tentativas -= 1
                
            print(f'a palavra era: {palavra_secreta}')
                        
            continuar2 = input('deseja jogar denovo? S/N ')
            if continuar2 == 'N':
                continuar = False
            elif continuar != 'S':
                print('Erro: digitação incorreta')
                continuar = False
                        
            
        else:
            print('Erro: topico não encontrado')
                        
print(main())
                
        
    