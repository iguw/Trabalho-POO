import random
import os
import pickle
from datetime import date 

from cliente import Cliente
from conta import Conta, Autenticador
from entregador import Entregador
from notificacao import Notificacao
from pagamento import Pagamento
from pedido import Pedido
from transporte import Transporte
from vendedor import vendedor
from produto import Produto


def salvar_objeto(obj, arquivo):
    with open(arquivo, "wb") as f:
        pickle.dump(obj, f)

def carregar_objeto(arquivo, fallback):
    if not os.path.exists(arquivo):
        return fallback
    with open(arquivo, "rb") as f:
        return pickle.load(f)


autenticador = carregar_objeto("autenticador.pkl", Autenticador())
vendedor1 = vendedor("Loja X", "Rua Z", "8888-8888", "12345678000101", "vendedor@email.com")
vendedor1._pedidos_recebidos = carregar_objeto("pedidos.pkl", [])

produtos_disponiveis = [
    Produto("Notebook", 3000.0),
    Produto("Smartphone", 1500.0),
    Produto("Tablet", 800.0),
    Produto("Fone de Ouvido", 200.0),
]

def menu_cliente(cliente):
    while True:
        print("\n--- Menu Cliente ---")
        print("1. Fazer novo pedido")
        print("2. Ver histórico de pedidos")
        print("3. Avaliar entrega")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nProdutos disponíveis:")
            for i, produto in enumerate(produtos_disponiveis):
                print(f"{i+1}. {produto.nome} - R${produto.preco}")

            escolhas = input("Digite os números dos produtos desejados separados por vírgula (ex: 1,3): ")
            indices = [int(i.strip()) - 1 for i in escolhas.split(",")]
            produtos_escolhidos = [produtos_disponiveis[i] for i in indices]
            valor_total = sum(produto.preco for produto in produtos_escolhidos)

            destino = input("Endereço de entrega: ")
            tipo_transporte = input("Digite o tipo de transporte (ex: carro, moto, bicicleta): ")
            transporte = Transporte(tipo_transporte, taxa_km=2.0, tempo_estimado=20, distancia=5)

            pedido = cliente.solicitar_pedido(
                id_pedido=str(random.randint(1000, 9999)),
                entrega_prevista=date.today(),
                transporte=transporte,
                valor_total=valor_total,
                endereco_destino=destino
            )
            pedido.produtos = produtos_escolhidos
            vendedor1.adicionar_pedido(pedido)
            salvar_objeto(autenticador, "autenticador.pkl")
            salvar_objeto(vendedor1._pedidos_recebidos, "pedidos.pkl")
            print("Pedido criado com sucesso!")

        elif opcao == "2":
            for pedido in cliente.visualizar_historico_pedidos():
                print(f"ID: {pedido.id_pedido} | Status: {pedido.status} | Valor: R${pedido.valor_total}")

        elif opcao == "3":
            id_pedido = input("ID do pedido a avaliar: ")
            for pedido in cliente.historico_pedidos:
                if pedido.id_pedido == id_pedido:
                    nota = int(input("Nota (0 a 5): "))
                    comentario = input("Comentário: ")
                    cliente.avaliar_entrega(pedido, nota, comentario)
                    salvar_objeto(autenticador, "autenticador.pkl")
                    salvar_objeto(vendedor1._pedidos_recebidos, "pedidos.pkl")
                    print("Avaliação registrada!")
                    break
            else:
                print("Pedido não encontrado.")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

def menu_entregador(entregador):
    while True:
        print("\n--- Menu Entregador ---")
        print("1. Ver pedidos disponíveis")
        print("2. Aceitar entrega")
        print("3. Finalizar entrega")
        print("4. Ver entregas finalizadas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nPedidos disponíveis:")
            for pedido in vendedor1.visualizar_pedidos_recebidos():
                if pedido.status == "Criado":
                    print(f"ID: {pedido.id_pedido} | Destino: {pedido.transporte.distancia}km | Status: {pedido.status}")

        elif opcao == "2":
            id_escolhido = input("Digite o ID do pedido que deseja aceitar: ")
            for pedido in vendedor1.visualizar_pedidos_recebidos():
                if pedido.id_pedido == id_escolhido and pedido.status == "Criado":
                    entregador.aceitar_entrega(pedido)
                    salvar_objeto(autenticador, "autenticador.pkl")
                    salvar_objeto(vendedor1._pedidos_recebidos, "pedidos.pkl")
                    break
            else:
                print("Pedido não encontrado ou já aceito.")

        elif opcao == "3":
            id_finalizar = input("Digite o ID do pedido a finalizar: ")
            for pedido in vendedor1.visualizar_pedidos_recebidos():
                if pedido.id_pedido == id_finalizar and pedido.status == "Em andamento":
                    entregador.finalizar_entrega(pedido)
                    salvar_objeto(autenticador, "autenticador.pkl")
                    salvar_objeto(vendedor1._pedidos_recebidos, "pedidos.pkl")
                    break
            else:
                print("Pedido não encontrado ou ainda não aceito.")

        elif opcao == "4":
            print("\nEntregas finalizadas:")
            for pedido in entregador.listar_entregas_finalizadas():
                print(f"ID: {pedido.id_pedido} | Status: {pedido.status}")

        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def menu_vendedor(vendedor):
    print("\n--- Menu Vendedor ---")
    print("Funções para vendedor ainda podem ser implementadas aqui.")

# BLOCO PRINCIPAL - após os menus
opcao = input("Você já possui cadastro? (s/n): ").lower()

if opcao == "s":
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    conta_logada = autenticador.autenticar(email, senha)
    if conta_logada:
        usuario = conta_logada.usuario
        if conta_logada.tipo_usuario == "cliente":
            menu_cliente(usuario)
        elif conta_logada.tipo_usuario == "entregador":
            menu_entregador(usuario)
        elif conta_logada.tipo_usuario == "vendedor":
            menu_vendedor(usuario)
    else:
        print("Login inválido.")
        exit()

elif opcao == "n":
    tipo_usuario = input("Você é (cliente / entregador / vendedor)? ").lower()

    nome = input("Nome completo: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    senha = input("Senha (mín. 8 caracteres): ")

    nova_conta = Conta(
        id_conta=str(random.randint(1000, 9999)),
        nome_cliente=nome,
        email=email,
        telefone=telefone,
        endereco=endereco,
        tipo_usuario=tipo_usuario
    )
    nova_conta.senha = senha

    if tipo_usuario == "cliente":
        nova_conta.usuario = Cliente(nome, endereco, telefone, email, senha)
    elif tipo_usuario == "entregador":
        transporte_tipo = input("Tipo de transporte (ex: moto, carro): ")
        capacidade = float(input("Capacidade de carga: "))
        nova_conta.usuario = Entregador(nome, transporte_tipo, capacidade)
    elif tipo_usuario == "vendedor":
        cnpj = input("CNPJ: ")
        nova_conta.usuario = vendedor(nome, endereco, telefone, cnpj, email)
    else:
        print("Tipo de usuário inválido.")
        exit()

    autenticador.cadastrar_conta(nova_conta)
    salvar_objeto(autenticador, "autenticador.pkl")
   

   
   
print("Cadastro realizado com sucesso! Faça login abaixo:\n")

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

conta_logada = autenticador.autenticar(email, senha)
if conta_logada:
    usuario = conta_logada.usuario
    if conta_logada.tipo_usuario == "cliente":
        menu_cliente(usuario)
    elif conta_logada.tipo_usuario == "entregador":
        menu_entregador(usuario)
    elif conta_logada.tipo_usuario == "vendedor":
        menu_vendedor(usuario)
else:
    print("Login inválido.")
