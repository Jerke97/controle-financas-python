import json
import os

ARQUIVO_DADOS = "gastos.json"
ARQUIVO_FUNDOS = "fundos.json"

def carregar_gastos():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            return json.load(f)
    return []

def salvar_gastos(gastos):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump(gastos, f, indent=4)

def carregar_fundos():
    if os.path.exists(ARQUIVO_FUNDOS):
        with open(ARQUIVO_FUNDOS, "r") as f:
            return json.load(f)
    return {"fundos": 0.0}

def salvar_fundos(valor):
    with open(ARQUIVO_FUNDOS, "w") as f:
        json.dump({"fundos": valor}, f)

def adicionar_gasto(gastos, fundos):
    try:
        valor = float(input("Valor (R$): "))
        print("Categoria: ")
        print("1. Gasto único")
        print("2. Gasto regular")
        categoria_opcao = input("Escolha a categoria (1 ou 2): ")
        categoria = "Gasto único" if categoria_opcao == "1" else "Gasto regular"
        descricao = input("Descrição: ")

        if valor > fundos["fundos"]:
            print("Saldo insuficiente para adicionar este gasto.")
            return

        gastos.append({
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao
        })
        fundos["fundos"] -= valor
        salvar_gastos(gastos)
        salvar_fundos(fundos["fundos"])
        print("✅ Gasto adicionado com sucesso!")
    except ValueError:
        print("Valor inválido.")

def listar_gastos(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado.")
        return
    for i, g in enumerate(gastos):
        print(f"{i+1}. R$ {g['valor']:.2f} - {g['categoria']} - {g['descricao']}")

def excluir_gasto(gastos, fundos):
    listar_gastos(gastos)
    try:
        i = int(input("Digite o número do gasto que deseja excluir: ")) - 1
        if 0 <= i < len(gastos):
            valor_recuperado = gastos[i]["valor"]
            gastos.pop(i)
            fundos["fundos"] += valor_recuperado
            salvar_gastos(gastos)
            salvar_fundos(fundos["fundos"])
            print("🗑️ Gasto removido e valor devolvido aos fundos.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def calcular_total(gastos):
    total = sum(g["valor"] for g in gastos)
    print(f"💰 Total de gastos: R$ {total:.2f}")

def mostrar_saldo(fundos):
    print(f"🧾 Saldo atual: R$ {fundos['fundos']:.2f}")

def adicionar_fundos(fundos):
    try:
        valor = float(input("Digite o valor a adicionar aos fundos: "))
        fundos["fundos"] += valor
        salvar_fundos(fundos["fundos"])
        print("💸 Fundos adicionados com sucesso.")
    except ValueError:
        print("Valor inválido.")

def menu():
    gastos = carregar_gastos()
    fundos = carregar_fundos()

    while True:
        print("\n=== Controle de Gastos ===")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Total gasto")
        print("4. Excluir gasto")
        print("5. Adicionar fundos")
        print("6. Ver saldo atual")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto(gastos, fundos)
        elif opcao == "2":
            listar_gastos(gastos)
        elif opcao == "3":
            calcular_total(gastos)
        elif opcao == "4":
            excluir_gasto(gastos, fundos)
        elif opcao == "5":
            adicionar_fundos(fundos)
        elif opcao == "6":
            mostrar_saldo(fundos)
        elif opcao == "7":
            print("Até a próxima!")
            break
        else:
            print("Opção inválida.")

menu()
