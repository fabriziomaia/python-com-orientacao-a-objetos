# If
media = 7
if media > 6.9:
    print("Você foi aprovado")

# Else
media = 5
if media < 4.9:
    print("Você foi reprovado")
else:
    print("Você foi aprovado")

# If, elif e else
media = 6
if media < 5:
    print("Você foi reprovado")
elif media > 5 and media < 7:
    print("Você fará a recuperação")
else:
    print("Você foi aprovado")

# Estrutura Match
media = 6

match media:
    case media if media < 5:
        print("Você foi reprovado")
    case media if 5 <= media < 7:
        print("Você fará a recuperação")
    case media if media >= 7:
        print("Você foi aprovado")