from pokemon import *
import random

nomes_inimigos = [
    "Dr. Malvado",
    "Equipe Obscura",
    "Espectro Sombrio",
    "Sombra Sinistra",
    "Equipe Nefasta",
    "Imperador do Caos",
    "Lady Veneno",
    "Mestre da Discórdia",
    "Capitão Venenoso",
    "Açougueiro Abominável",
    "Senhora das Trevas",
    "Lorde do Trovão",
    "General Caótico",
    "Conde Obsidiano",
    "Comandante Abissal"
]


nomes_pokemons = [
    PokemonFogo("Charizard"),
    PokemonFogo("Arcanine"),
    PokemonFogo("Ninetales"),
    PokemonFogo("Flareon"),
    PokemonFogo("Magmar"),
    PokemonFogo("Charmander"),
    PokemonFogo("Cyndaquil"),
    PokemonFogo("Torchic"),
    PokemonFogo("Chimchar"),
    PokemonFogo("Infernape"),
    PokemonFogo("Emboar"),
    PokemonFogo("Litten"),
    PokemonFogo("Braixen"),
    PokemonFogo("Torracat"),
    PokemonFogo("Cinderace"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonEletrico("Jolteon"),
    PokemonEletrico("Ampharos"),
    PokemonEletrico("Electabuzz"),
    PokemonEletrico("Mareep"),
    PokemonEletrico("Elekid"),
    PokemonEletrico("Shinx"),
    PokemonEletrico("Luxio"),
    PokemonEletrico("Luxray"),
    PokemonEletrico("Pachirisu"),
    PokemonEletrico("Zeraora"),
    PokemonEletrico("Joltik"),
    PokemonEletrico("Galvantula"),
    PokemonEletrico("Toxel")
]




class Pessoa:
    

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(nomes_inimigos)

        self.pokemons = pokemons
        self.dinheiro = dinheiro 
        
    

    def __str__(self):
        return self.nome
    


    def mostrar_pokemons(self):
        if self.pokemons:
            print(f"Pokemons de {self}:")
            
            for index, pokemon in enumerate(self.pokemons):
                print(index, "-", pokemon)
        else:
            print(f"{self} não possui nenhum pokemon")

 
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokemon_escolhido} ")
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido!")



    def mostrar_dinheiro(self):
        print(f"Voce possui ${self.dinheiro}")



    def ganhar_dinheiro(self, qtd_dinheiro):
        self.dinheiro += qtd_dinheiro
        print(f"Você ganhou ${qtd_dinheiro}")
        self.mostrar_dinheiro()


    
    def batalhar(self, pessoa):
        print(f"{self} iniciou uma batalha com {pessoa}")

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()


        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} ganhou a batalha")
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                        
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f"{pessoa} ganhou a batalha")
                    break
                
        else:
            print("Essa batalha não pode ocorrer!")
        
            
            




class Player(Pessoa):
    tipo = "player"


    def capturar_pokemonSelvagem(self, pokemon):
        if pokemon.level < 15:
            chance = random.choice(["S", "N"])
        else:
            chance = random.choice(["S", "N", "B", "T"])

        if chance == "S":
            self.pokemons.append(pokemon)
            print(f"{self} capturou {pokemon}")
        else:
            print(f"O pokemon {pokemon} fugiu")




    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}")



    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha o seu Pokemon: ")
                try:
                    int_escolha = int(escolha)
                    Pokemon_escolhido = self.pokemons[int_escolha]
                    print(f"{Pokemon_escolhido} eu escolho você!")
                    return Pokemon_escolhido
                except:
                    print("Escolha invalida!")
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido!")    



    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(nomes_pokemons)
            print(f"Um pokemon selvagem apareceu {pokemon}")
        
            escolha = input("Deseja capturar este pokemon? (S/N): ")

            if escolha in "Ss":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f"{pokemon} fugiu!")
            else:
                print("O pokemon fugiu")

        else:
            print("Não surgiu nenhum pokemon selvagem nessa exploração!")
            
            



class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(nomes_pokemons))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)

        else:
            super().__init__(nome=nome, pokemons=pokemons)

        
        

    

        

    
        

#eu = Player("Andre")

# pokemon_selvagem = PokemonFogo("Charmander", level=56)

# eu.capturar(pokemon_selvagem)
# eu.mostrar_pokemons()


# meu_pokemon = PokemonFogo("Charmander")
# #print(meu_pokemon)

# meu_inimigo = Inimigo()

# print(meu_inimigo)
# meu_inimigo.mostrar_pokemons()