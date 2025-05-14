

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

vendedor1 = vendedor("SuperCell Celulares", "Rua A", "1111-1111", "11111111111111", "x@email.com")
vendedor2 = vendedor("Loja MagInformática", "Rua B", "2222-2222", "22222222222222", "y@email.com")
vendedor3 = vendedor("Loja MercadoMercantil", "Rua C", "3333-3333", "33333333333333", "z@email.com")

vendedor1._pedidos_recebidos = []
vendedor2._pedidos_recebidos = []
vendedor3._pedidos_recebidos = []

vendedor1.produtos = [
    Produto("Smartphone Galaxy", 2500.0),
    Produto("Cabo USB-C", 50.0),
    Produto("Fone Bluetooth", 300.0),
    Produto("Carregador Turbo", 120.0),
    Produto("Película de Vidro", 25.0)
]

vendedor2.produtos = [
    Produto("Notebook Dell", 4200.0),
    Produto("Mouse Gamer", 200.0),
    Produto("Teclado Mecânico", 350.0),
    Produto("Monitor 24\"", 800.0),
    Produto("Webcam HD", 150.0)
]

vendedor3.produtos = [
    Produto("Feijão", 10.0),
    Produto("Arroz", 8.0),
    Produto("Açúcar", 5.0),
    Produto("Café", 15.0),
    Produto("Macarrão", 6.0)
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
            print("\nLojas disponíveis:")
            print("- SuperCell Celulares")
            print("- Loja MagInformática")
            print("- Loja MercadoMercantil")

            vendedor_escolhido = None
            while vendedor_escolhido is None:
                nome_loja = input("Digite o nome da loja desejada: ").strip().lower()
                if nome_loja == "supercell celulares":
                    vendedor_escolhido = vendedor1
                elif nome_loja == "loja maginformática":
                    vendedor_escolhido = vendedor2
                elif nome_loja == "loja mercadomercantil":
                    vendedor_escolhido = vendedor3
                else:
                    print("Loja não encontrada. Tente novamente.")

            print("\nProdutos da loja selecionada:")
            for i, produto in enumerate(vendedor_escolhido.produtos, 1):
                print(f"{i}. {produto.nome} - R${produto.preco:.2f}")

            indices = [int(i.strip()) - 1 for i in input("Produtos desejados (ex: 1,3): ").split(",")]
            produtos_escolhidos = [vendedor_escolhido.produtos[i] for i in indices]
            valor_produtos = sum(p.preco for p in produtos_escolhidos)

            destino = input("Endereço de entrega: ")
            tipo = input("Tipo de transporte (carro/moto/bike): ")
            distancia = 5.0  
            transporte = Transporte(tipo, taxa_km=2.0, tempo_estimado=20, distancia=distancia)
            taxa_entrega = transporte.calcular_custo()

            pedido = cliente.solicitar_pedido(
                id_pedido=str(random.randint(1000, 9999)),
                entrega_prevista=date.today(),
                transporte=transporte,
                valor_total=valor_produtos,
                endereco_destino=destino
            )
            pedido.produtos = produtos_escolhidos
            vendedor_escolhido.adicionar_pedido(pedido)

            salvar_objeto(autenticador, "autenticador.pkl")

            print(f"Pedido criado com sucesso! ID do pedido: {pedido.id_pedido}")
            print(f"Produtos: {[p.nome for p in produtos_escolhidos]}")
            print(f"Total: R${valor_produtos:.2f} + Entrega: R${taxa_entrega:.2f} = R${valor_produtos + taxa_entrega:.2f}")

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
            for vendedor in [vendedor1, vendedor2, vendedor3]:
                for pedido in vendedor.visualizar_pedidos_recebidos():
                    if pedido.status == "Criado":
                        print(f"ID: {pedido.id_pedido} | Valor: R${pedido.valor_total:.2f} | Status: {pedido.status}")

        elif opcao == "2":
            id_escolhido = input("Digite o ID do pedido que deseja aceitar: ")
            for vendedor in [vendedor1, vendedor2, vendedor3]:
                for pedido in vendedor.visualizar_pedidos_recebidos():
                    if pedido.id_pedido == id_escolhido and pedido.status == "Criado":
                        entregador.aceitar_entrega(pedido)
                        salvar_objeto(autenticador, "autenticador.pkl")
                        break
            else:
                print("Pedido não encontrado ou já aceito.")

        elif opcao == "3":
            id_finalizar = input("Digite o ID do pedido a finalizar: ")
            for vendedor in [vendedor1, vendedor2, vendedor3]:
                for pedido in vendedor.visualizar_pedidos_recebidos():
                    if pedido.id_pedido == id_finalizar and pedido.status == "Em andamento":
                        entregador.finalizar_entrega(pedido)
                        salvar_objeto(autenticador, "autenticador.pkl")
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
    while True:
        print("\n--- Menu Vendedor ---")
        print("1. Ver pedidos recebidos")
        print("2. Ver produtos disponíveis")
        print("3. Adicionar novo produto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pedidos = vendedor.visualizar_pedidos_recebidos()
            if pedidos:
                for pedido in pedidos:
                    print(f"ID: {pedido.id_pedido} | Status: {pedido.status} | Valor: R${pedido.valor_total:.2f}")
            else:
                print("Nenhum pedido recebido ainda.")

        elif opcao == "2":
            print("\nProdutos da loja:")
            for produto in vendedor.produtos:
                print(f"- {produto.nome}: R${produto.preco:.2f}")

        elif opcao == "3":
            nome_produto = input("Nome do novo produto: ")
            preco_produto = float(input("Preço do produto (R$): "))
            novo_produto = Produto(nome_produto, preco_produto)
            vendedor.produtos.append(novo_produto)
            print(f"Produto '{nome_produto}' adicionado com sucesso!")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


print("Você deseja logar ou se cadastrar? (login/cadastro): ", end="")
modo = input().strip().lower()

if modo == "login":
    tipo = input("Você quer logar como (cliente / entregador / vendedor)? ").strip().lower()
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    conta_logada = autenticador.autenticar(email, senha)
    if conta_logada and conta_logada.tipo_usuario == tipo:
        usuario = conta_logada.usuario
        if tipo == "cliente":
            menu_cliente(usuario)
        elif tipo == "entregador":
            menu_entregador(usuario)
        elif tipo == "vendedor":
            menu_vendedor(usuario)
    else:
        print("Login inválido ou tipo incorreto.")
        exit()

elif modo == "cadastro":
    tipo_usuario = input("Você é (cliente / entregador / vendedor)? ").lower()
    nome = input("Nome completo: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    while True:
        senha = input("Senha (mín. 8 caracteres): ")
        try:
            nova_conta = Conta(
                id_conta=str(random.randint(1000, 9999)),
                nome_cliente=nome,
                email=email,
                telefone=telefone,
                endereco=endereco,
                tipo_usuario=tipo_usuario
            )
            nova_conta.senha = senha
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

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

    print(f"Cadastro realizado com sucesso! Bem-vindo(a), {nome}.")

    if tipo_usuario == "cliente":
        menu_cliente(nova_conta.usuario)
    elif tipo_usuario == "entregador":
        menu_entregador(nova_conta.usuario)
    elif tipo_usuario == "vendedor":
        menu_vendedor(nova_conta.usuario)


else:
    print("Opção inválida. Encerrando o sistema.")
