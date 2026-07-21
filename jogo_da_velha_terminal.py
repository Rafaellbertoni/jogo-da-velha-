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

def main():
    continuar = True
    while continuar:
        print('[animais]\n[paises]\n[frutas]')
        topico = input('qual topico você deseja escolher? ').lower
        
        if topico == 'animais': 
            palavra_secreta = animais()
            qnts_letras = len(palavra_secreta)
            
            for i in range(5):
                tentativas = 7
                print('Palavra: ' + qnts_letras * '_')
                print(f'Tentativas: {tentativas - 1}')
                letra_usuario = input('digite uma letra: ')
                for letra in palavra_secreta:
                    if letra == letra_usuario:
                        
                
        
    