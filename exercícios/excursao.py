while(True):
    try:
        num_turmas = int(input("Quantas turmas vão participar? "))
        if num_turmas <= 0:
            print("Erro: o número de turmas deve ser maior que zero.")
            continue
        break
    except ValueError:
        print("Erro: digite um número inteiro maior que 0.")

total_alunos = 0 #0 - Para garantir que a soma inicial seja 0.
max_inscritos = -1 #Para garantir que qualquer turma com alunos será maior.

for i in range(num_turmas): #For i in range - Para percorrer o número de turmas.
    print(f"Turma: {i+1}" ) # i+1 - Para garantir que a contagem de turmas comece em 1.
    nome_turma = input("Digite o nome da turma: ")

    while(True):
        try:
            num_alunos = int(input(f"Digite o número de alunos na turma {i+1}: "))
            if num_alunos < 0:
                print("Erro: o número de alunos não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Erro: digite um número inteiro não negativo.")

    total_alunos += num_alunos
    print(f"Total de alunos: {total_alunos}")

    if num_alunos > max_inscritos:
        max_inscritos = num_alunos
        turma_mais_inscritos = nome_turma
        print(f"Turma com mais alunos inscritos: {turma_mais_inscritos}, com {max_inscritos} alunos.") 

if total_alunos > 0:
    professores_necessarios = total_alunos / 15
    if professores_necessarios == float(professores_necessarios):
        professores_necessarios = int(professores_necessarios)

    print(f"Professores necessários: {professores_necessarios}")

    total_pessoas = total_alunos + professores_necessarios
    print(f"Total de pessoas na excursão: {total_pessoas}")

    quant_onibus = total_pessoas / 44
    if quant_onibus == float(quant_onibus):
        quant_onibus = int(quant_onibus)
    print(f"Quantidade de ônibus: {quant_onibus}")

    lugares_sobrando = (quant_onibus * 44) - total_pessoas
    print(f"Lugares sobrando:{lugares_sobrando}")

    custo_total = quant_onibus * 1800
    print(f"Custo total da excursão: R${custo_total:.2f}")

    valor_por_aluno = custo_total / total_alunos
    print(f"Valor por aluno: R${valor_por_aluno:.2f}")

    encerrar = input("Digite 'FIM' para encerrar o programa ou dê enter para continuar: ")
    if encerrar.upper() == 'FIM':
            print("Encerrando o programa...")
            break