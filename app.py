peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc >= 18.5 and imc <= 24.9:
    print("Você está no peso ideal.")
elif imc < 18.5:
    print("Abaixo do peso normal.")
    peso_ideal = 18.5 * (altura ** 2)
    peso_perder = peso - peso_ideal
    print("Para alcançar o IMC ideal (18.5), você precisa ganhar {:.1f}kg.".format(-peso_perder))
elif imc >= 25.0 and imc <= 29.9:
    print("Excesso de peso.")
    peso_maximo = 24.9 * (altura ** 2)
    peso_perder = peso - peso_maximo
    print("Para ter um IMC menor que 24.9, você precisa perder {:.1f}kg.".format(peso_perder))
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade classe 1.")
    peso_maximo = 24.9 * (altura ** 2)
    peso_perder = peso - peso_maximo
    print("Para ter um IMC menor que 24.9, você precisa perder {:.1f}kg.".format(peso_perder))
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade classe 2.")
    peso_maximo = 24.9 * (altura ** 2)
    peso_perder = peso - peso_maximo
    print("Para ter um IMC menor que 24.9, você precisa perder {:.1f}kg.".format(peso_perder))
else:
    print("Obesidade classe 3.")
    peso_maximo = 24.9 * (altura ** 2)
    peso_perder = peso - peso_maximo
    print("Para ter um IMC menor que 24.9, você precisa perder {:.1f}kg.".format(peso_perder))
    
    