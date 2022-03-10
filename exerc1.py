data = list()

while True:
    input_data = int(input())
    data.append(input_data)

    if input_data == -1:
        break
    else:
        pass


print(f'Qtd. de valores inseridos: {len(data)}')
print('----------------------------------------')

print(f'Valores um ao lado do outro: {data}')
print('----------------------------------------')


data_inverse = [num for num in reversed(data)]
print(f'Ordem inversa dos valores: {data_inverse}')
print('----------------------------------------')

print(f'Soma dos valores: {sum(data)}')
print('----------------------------------------')

mean_data = sum(data)/len(data)
print(f'Valor da média: {round(mean_data,2)}')
print('----------------------------------------')

for i in data:
    if i > mean_data:
        print(f'Valores acima da média: {i}')
print('----------------------------------------')

for i in data:
    if i < 7:
        print(f'Valores abaixo de sete: {i}')

print('----------')
print('Obrigado')
