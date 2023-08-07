import pickle

from pokemon import *
from Pessoa import *



def escolher_pokemon_inicial(player):
    print(f"Olá {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("voce possui 3 escolhas:")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)

    while True:
        escolha = input("Escolha o seu Pokemon: ")

        if escolha  ==  "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha invalida!")

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar o jogo")
        print(error)
             



def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso!")
            return player
    except Exception as error:
        print("Save não encontrado")
        
             
        




if __name__ == "__main__":
    print("-"* 45)
    print("Bem-vindo ao game Pokemon feito em Python via terminal :)")
    print("-"* 45)

    player = carregar_jogo()
    if not player:
        nome = input("Olá, qual é o seu nome: ")
        player = Player(nome)
        print(f"{player}, esse mundo é habitado por pokemons, a partir de agora sua missão é se tornar um mestre dos pokemons")
        print("Capture o maximo de pokemons que conseguir e lute com seus inimigos")
        player.mostrar_dinheiro()
        
        if player.pokemons:
            print("Já vi que você tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            print("-"* 45)
            print("Você não tem nenhum pokemon, escolha seu pokemon inicial: ")
            print("-"* 45)
            escolher_pokemon_inicial(player)
        

        print("Pronto, agora que você ja possui um pokemon, enfrente seu arqui-rival Gary:")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)

        salvar_jogo(player)


    while True:
        print("-"* 20)
        print("O que deseja fazer?: ")

        print("0 - sair do jogo")
        print("1 - explorar pelo mundo")
        print("2 - lutar com um inimigo")
        print("3 - Ver pokedex")
        
        print("-"* 20)
        escolha = input("Sua escolha: ")

        if escolha == "0":
            print("Fechando o jogo...")
            break

        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        
        elif escolha == "3":
            player.mostrar_pokemons()
        else:
            print("Escolha invalida")




    

