import json
import os
from datetime import datetime

def cadastrar_produto():
    print("\n=== CADASTRO DE PRODUTO ===")
    # Recolhe os dados básicos limpando espaços extras nas pontas
    codigo_rp = input("Código RP: ").strip()
    loja = input("Número da Loja: ").strip()
    produto = input("Nome do Produto: ").strip()
    cliente = input("Nome do Cliente: ").strip()
    cpf = input("CPF do Cliente: ").strip()
    
    # Validação simples para evitar cadastros vazios que geram furos no estoque
    if not cpf or not cliente or not produto:
        print("\nErro: Os campos CPF, Cliente e Produto são obrigatórios!")
        return

    localizacao = input("Localização física (Ex: Galpão A, Prateleira 4): ").strip()
    numero_pedido = input("Número do Pedido: ").strip()
    nota_fiscal = input("Nota fiscal do fornecedor: ").strip()
    
    # Registra a data e hora exata da chegada do item na loja
    data_chegada = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    produto_cadastrado = {
        "codigo_rp": codigo_rp,
        "loja": loja,
        "produto": produto,
        "cliente": cliente,
        "cpf": cpf,
        "localizacao": localizacao,
        "numero_pedido": numero_pedido,
        "nota_fiscal": nota_fiscal,
        "data_chegada": data_chegada,
        "retirado": False  # Todo item novo começa pendente na loja
    }
    
    # Carrega o JSON existente ou cria uma lista nova se o arquivo ainda não existir
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)
    else:
        estoque = []
        
    estoque.append(produto_cadastrado)
    
    # Salva a lista atualizada de volta no arquivo JSON para não perder nada ao fechar
    with open("estoque.json", "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=False, indent=4)
        
    print(f"\nSucesso! Produto cadastrado. Total geral no estoque: {len(estoque)} produto(s).")


def buscar_produto():
    print("\n=== BUSCA DE PRODUTO ===")
    # .strip() evita que um espaço sem querer na digitação impeça de achar o cliente
    cpf = input("Digite o CPF do Cliente: ").strip()
    
    # Validação para não buscar campos vazios
    if not cpf:
        print("Erro: O CPF não pode estar vazio.")
        return

    if os.path.exists("estoque.json"):
        with open("estoque.json", "r", encoding="utf-8") as arquivo:
            estoque = json.load(arquivo)
    else:
        estoque = []

    encontrado = False
    for produto in estoque:
        # .strip() aqui garante que o CPF do JSON bata com o digitado mesmo se houver espaços
        if produto["cpf"].strip() == cpf:
            encontrado = True
            # Traduz o booleano para um status claro de leitura rápida na operação
            status = "SIM" if produto.get("retirado") else "NÃO (Pendente)"
            
            print("\n----------------------------------------")
            print("Produto encontrado!")
            print(f"Cliente: {produto['cliente']}")
            print(f"CPF: {produto['cpf']}")
            print(f"Produto: {produto['produto']}")
            print(f"Localização: {produto['localizacao']}")
            print(f"Pedido nº: {produto['numero_pedido']}")
            print(f"Nota fiscal: {produto['nota_fiscal']}")
            print(f"Data de chegada: {produto['data_chegada']}")
            print(f"Retirado: {status}")
            print("----------------------------------------")

    # Feedback visual para o operador saber que a busca rodou mas não achou nada
    if not encontrado:
        print(f"\nNenhum produto cadastrado para o CPF: {cpf}")


def marcar_retirado():
    print("\n=== MARCAR COMO RETIRADO ===")
    # Remove espaços extras para evitar erro na hora de dar baixa
    cpf = input("Digite o CPF do Cliente: ").strip()

    if not os.path.exists("estoque.json"):
        print("Nenhum registro encontrado (banco de dados vazio).")
        return

    with open("estoque.json", "r", encoding="utf-8") as arquivo:
        estoque = json.load(arquivo)

    encontrado = False
    for produto in estoque:
        if produto["cpf"].strip() == cpf:
            # Atualiza o status para sinalizar que o cliente já levou o item
            produto["retirado"] = True
            encontrado = True
            print(f"\nSucesso: O produto '{produto['produto']}' do cliente {produto['cliente']} foi marcado como RETIRADO!")

    # Salva as alterações no JSON apenas se encontrou e atualizou o item
    if encontrado:
        with open("estoque.json", "w", encoding="utf-8") as arquivo:
            json.dump(estoque, arquivo, ensure_ascii=False, indent=4)
    else:
        print(f"\nNenhum produto pendente encontrado para o CPF: {cpf}")


# Loop principal do sistema de atendimento na loja
while True:
    print("\n== CONTROLE DE RETIRADAS ==")
    print("1 - Cadastrar Produto")
    print("2 - Buscar Produto")
    print("3 - Marcar como Retirado")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        buscar_produto()
    elif opcao == "3":
        marcar_retirado()
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")