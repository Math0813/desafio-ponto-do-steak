# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)

#Solicitar a entrada da temperatura
temperatura = float(input("digite a temperatura do Steak em Celsius:"))






'''

# Erros: Se caso o usuario digite uma temperarua em palavras (strimg).

try:
  #Pergunta se o usuário que digitar em Celsius ou Fahrenheit
  unidade = input("Você deseja inserir a temperatura em Celsius (C) ou Fahrenheit (F)?").strip().upper()
#solicita a entrada da temperatura 
  if unidade == "C":
      temperatura = float (input("Digite a temperatura do steak em Celsius: "))
  elif unidade == "F":
      fahrenheit = float(input("Digite a temperatura do steak em Fahrenheit:"))

  #Converte Fahrenheit para Celsius
      temperatura = (fahrenheit - 32) * 5/9
  else:
    raise ValueError("Unidade inválida. Por favor, escolha 'C' para Celsius ou 'F' para Fahrenheit.")
  
#estrutura da decisão
  if temperatura in range(0, 49): #primeiro bloco - De 0 a 48C  
      print("Rare (selada)")
  elif temperatura in range(49, 55):# bloco intermediario
        print("Medium (Ao ponto)")
  elif temperatura in range(55, 61):# bloco intermediario
        print("Medium (Ao ponto para o mal)")
  elif temperatura in range(61, 66): # bloco intermediario
        print("Medium well (Ao ponto para o bem)")
  else: # bloco final
        print("Well done (Bem passada)")

except ValueError as e:
  # Mensagem de erro se a entrada não for um número
  print(f"Erro: {e}")
    