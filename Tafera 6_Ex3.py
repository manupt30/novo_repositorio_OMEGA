nomefich = input("Nome do ficheiro: ").lower()
nomefich = nomefich + ".txt"
max_nota = 0
nome_melhor_aluno = ""
soma = 0
contar = 0
aprovados = []
reprovados = []

try:
    lerFicheiro = open(nomefich, "r+", encoding="utf-8")
except FileNotFoundError:
    print("Ficheiro não existe ou a localização está errada!")
else:
    while True:
        linha = lerFicheiro.readline()
        if not linha:
            break
        if linha.strip() == "":
            continue
        
        aluno = linha.split(",")
        nome_aluno = aluno[0].strip()
        nota = int(aluno[1].strip())
        
        if nota > max_nota:
            max_nota = nota
            nome_melhor_aluno = nome_aluno
        
        soma += nota
        contar += 1
        
        if nota > 9:
            aprovados.append(f"{nome_aluno:.<25} {nota} Aprovado")
        else:
            reprovados.append(f"{nome_aluno:.<25} {nota} Reprovado")

    lerFicheiro.close()

    print("\nAlunos aprovados:")
    for aprovado in aprovados:
        print(aprovado)
    
    print("\nAlunos reprovados:")
    for reprovado in reprovados:
        print(reprovado)
    
    media = soma / contar if contar != 0 else 0
    print("\n" + "-" * 40)
    print(f"Média das notas: {media:.2f}")
    print(f"Melhor nota: {nome_melhor_aluno:.<12} {max_nota}")
    print("-" * 40)
