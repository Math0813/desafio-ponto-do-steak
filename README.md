# **Desafio com If, Elif, Else - Temperatura do Steak**

Este programa foi desenvolvido para calcular o ponto de cozimento de um **steak** com base na temperatura informada pelo usuário. O programa permite que o usuário insira a temperatura em **Celsius** ou **Fahrenheit**, e retorna o ponto de cozimento correspondente em português.

## **Objetivo**

O objetivo do programa é receber a temperatura do steak e determinar o ponto de cozimento, com base nas seguintes faixas de temperatura:

| Temperatura (°C) | Ponto de Cozimento |
|------------------|--------------------|
| 48°C ou 120°F    | Rare (Selada)      |
| 54°C ou 130°F    | Medium rare (Ao ponto para o mal) |
| 60°C ou 140°F    | Medium (Ao ponto) |
| 65°C ou 150°F    | Medium well (Ao ponto para o bem) |
| 71°C ou 160°F    | Well done (Bem passada) |

## **Funcionalidades**

- O usuário pode escolher se deseja inserir a temperatura em **Celsius (C)** ou **Fahrenheit (F)**.
- O programa realiza a conversão de Fahrenheit para Celsius, caso necessário.
- O código verifica se a temperatura inserida está dentro dos limites esperados e retorna o ponto de cozimento correspondente.
- Caso a entrada seja inválida (como texto em vez de número), o programa exibirá uma mensagem de erro explicativa.

## **Como Usar**

1. Ao rodar o programa, será perguntado ao usuário se deseja inserir a temperatura em **Celsius (C)** ou **Fahrenheit (F)**.
2. Após escolher a unidade de medida, o usuário deve inserir a temperatura do steak.
3. O programa, então, retorna o ponto de cozimento do steak em português.
   
## **Exemplo de Execução**

Você deseja inserir a temperatura em Celsius (C) ou Fahrenheit (F)? C
Digite a temperatura do steak em Celsius: 60
Medium (Ao ponto)

## **Estrutura de Decisão**

O programa utiliza a estrutura de decisão `if`, `elif`, e `else` para determinar o ponto de cozimento do steak com base na temperatura informada:

- Se a temperatura estiver na faixa de 0 a 48°C, o ponto será "Rare (selada)".
- Se a temperatura estiver na faixa de 49 a 54°C, o ponto será "Medium rare (Ao ponto para o mal)".
- Se a temperatura estiver na faixa de 55 a 60°C, o ponto será "Medium (Ao ponto)".
- Se a temperatura estiver na faixa de 61 a 65°C, o ponto será "Medium well (Ao ponto para o bem)".
- Se a temperatura for superior a 65°C, o ponto será "Well done (Bem passada)".

## **Erros Tratados**

- O programa verifica se o usuário escolheu a unidade correta (Celsius ou Fahrenheit).
- Caso o usuário insira uma unidade inválida ou texto, o programa exibe uma mensagem de erro.
- Caso a entrada de temperatura seja um valor não numérico (como uma string), o programa captura o erro e avisa o usuário.

## **Como Rodar**

1. Baixe o código.
2. Execute em um ambiente Python (recomendado o uso de Python 3).
3. Siga as instruções para inserir a temperatura e a unidade.