# *** JOGO ***

# Início do programa
print("\n"*100)
print("Neste jogo você deve convencer Deus a não destruir Sodoma e Gomorra.")
print("No prompt 'Eu' Digite:")
print("--> Senhor, e se houver xyz justos na cidade?")
print("(Onde 'xyz' corresponde a um número entre 0 e 999)")
print("BOA SORTE!!!")

input("Tecle <ENTER> ")

# Início do jogo
print("\n"*100)
numjust = 50
while numjust >= 10:
    justos = input("Eu: ")
    try:
        if int(justos[20:23]) == numjust:
            print("Deus: Não destruirei a cidade por amor dos {} justos".format(numjust))
            if numjust < 45:
                numjust -= 5
            numjust -= 5
    # Jogo do tipo "quente ou frio".
        elif int(justos[20:23]) > numjust:
            print("Deus: Você não deveria pedir por menos justos?")
        elif int(justos[20:23]) < numjust:
            print("Deus: Você não gostaria de pedir por mais justos?")
    # Se digitar errado, começa tudo de novo.
    except ValueError:
        print("Deus: Acaso vou destruir as cidades sem consultar Abraao?")
        numjust = 50
input("Tecle <ENTER> ")

# Fim do jogo
print("\n"*100)
print("\nDeus: Anjos, tirem Ló e sua família de lá...")
print("\nAnjos: Sim, Senhor!")
print("\n*** GAME OVER ***\n")
input("\nTecle <ENTER> ")
