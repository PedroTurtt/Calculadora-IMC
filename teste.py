altura = input('Defina a altura: ')
peso = float(input('Defina o peso: '))
inferno = ','

if inferno in altura:
    altura_float = float(altura.replace(",","."))
    imc = (peso / (altura_float * altura_float))
    
else: 
    float_altura = float(altura) 
    imc = (peso / (float_altura * float_altura))

if imc < 18.5: 
    print ("Seu IMC é: ",round(imc, 2))
    print ("Você está abaixo do peso :(")
if imc > 18.5 and imc < 24.9 : 
    print ("Seu IMC é: ",round(imc, 2))
    print ("Você está no peso ideal!!")
if imc > 25 and imc < 29.9 : 
    print ("Seu IMC é: ",round(imc, 2))
    print ("Você está no sobrepeso")
if imc > 30 and imc < 39.9 : 
    print ("Seu IMC é: ",round(imc, 2))
    print ("Você está no OBESOOOOO")
if imc > 35 : 
    print ("Seu IMC é: ",round(imc, 2))
    print ("Você está no OBESOOOOO pra caralho")    
