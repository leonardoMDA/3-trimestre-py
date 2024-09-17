minutos = int(input("Digite a quantidade de minutos."))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")