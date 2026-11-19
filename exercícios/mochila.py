itens = []
total_peso = 0.0

while(True):
    nome = input("Digite o nome do item (ou 'FIM' para encerrar): ")
    if nome.upper() == 'FIM':
        print("Encerrando programa...")
        break

    try:
        peso = float(input("Digite o peso (em kg) do item: ").replace(",", "."))
        
    except ValueError:
        print("Erro: peso inválido. Por favor, digite um valor positivo.")
        continue

    itens.append({'nome': nome, 'peso': peso})

    if len(itens) > 0: #Para verificar que a lista não está vazia.
        print("-- RESUMO --")
        for item in itens:
            print(f"Item: {item['nome']}| Peso: {item['peso']} kg")
            total_peso += item['peso']

        print(f"Peso total:  {total_peso:.2f} kg")

        if total_peso > 15:
            print(f"O peso da mochila excedeu o limite de 15 kg.")
            print(f"Remova {(total_peso - 15):.2f} kg para ficar dentro do limite.")

            #sum = soma os elementos
            #len = conta os elementos
            total_itens = len(itens)
            print(f"Total de itens na mochila: {total_itens}")

            media_peso = total_peso/total_itens
            print(f"Média de peso: {media_peso:.2f} kg")
            #:.2f - Para formatar casas decimais, use :.2f dentro das chaves.

            maior_peso = max({item['peso'] for item in itens})
            print(f"Item mais pesado: {maior_peso:.2f} kg")

    else:
        print(f"Não há itens na mochila.")



        



