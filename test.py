#pergunta para usuario e anexo de valor.
name = input("Qual seu nome? " )
idade = input("Quantos anos voce tem? ")
cidade = input("Em qual cidade voce mora? ")

#retirar os espaços da str
name = name.strip()
idade = idade.strip()
cidade = cidade.strip()
"""
ISSO TAMBEM E UM COMENTARIO
"""
#saida final
#sep= o que vai acontecer entre os parametros.
#end= o que vai acontecer ao final.
print ("ola",name,"vimos que tens",idade,'anos e mora na cidade de',cidade, sep=(" "), end=("\n"))
#outro meio de colocar variaveis, é necessario colocar {} e "f" no inicio da linha. (não se pode usar sep and end.)
print (f"ola {name} vimos que tens {idade} anos e mora na cidade de {cidade}")