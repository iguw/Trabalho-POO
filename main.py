import re
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


def salvar_objeto(obj, arquivo):   #Salva um objeto em um arquivo usando o módulo pickle.  Parâmetros: obj: qualquer objeto Python serializável
    
    with open(arquivo, "wb") as f:
        pickle.dump(obj, f)

def carregar_objeto(arquivo, fallback): # Carrega um objeto de um arquivo pickle, ou retorna um valor padrão se o arquivo não existir, arquivo: nome do arquivo a ser carregado, fallback: valor padrão a ser retornado se o arquivo não existir
    if not os.path.exists(arquivo):
        return fallback #Retor objeto carregado do arquivo ou fallback
    with open(arquivo, "rb") as f:
        return pickle.load(f)


autenticador = carregar_objeto("autenticador.pkl", Autenticador())
todos_os_pedidos = carregar_objeto("pedidos.pkl", [])

vendedor1 = vendedor("SuperCell Celulares", "Rua A", "1111-1111", "11111111111111", "x@email.com")
vendedor2 = vendedor("Loja MagInformática", "Rua B", "2222-2222", "22222222222222", "y@email.com")
vendedor3 = vendedor("Loja MercadoMercantil", "Rua C", "3333-3333", "33333333333333", "z@email.com")

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



print("="*50)
print("Bem-vindo à SpeedBox — sua facilitadora em entregas!")
print("="*50)

def menu_cliente(cliente): # Exibe o menu de opções para clientes, cliente: instância da classe Cliente autenticada
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

            vendedor_escolhido = None #Escolhe a loja desejada
            while vendedor_escolhido is None:
                nome_loja = input("Digite o nome da loja desejada: ").strip().lower()
                if nome_loja == "supercell celulares":
                    vendedor_escolhido = vendedor1
                elif nome_loja == "loja maginformática":
                    vendedor_escolhido = vendedor2
                elif nome_loja == "loja mercadomercantil":
                    vendedor_escolhido = vendedor3
                else:
                    print("Loja não encontrada. Tente novamente.") #Se nenhuma loja for encontrada, pede para o usuário tentar novamente

            print("\nProdutos da loja selecionada:") #Exibe os produtos disponíveis na loja escolhida
            for i, produto in enumerate(vendedor_escolhido.produtos, 1):
                print(f"{i}. {produto.nome} - R${produto.preco:.2f}")

            indices = [int(i.strip()) - 1 for i in input("Produtos desejados (ex: 1,3): ").split(",")] #Pede para o usuário escolher os produtos desejados
            produtos_escolhidos = [vendedor_escolhido.produtos[i] for i in indices] #Cria uma lista com os produtos escolhidos
            valor_produtos = sum(p.preco for p in produtos_escolhidos) #Calcula o valor total dos produtos escolhidos

            destino = input("Endereço de entrega: ") #Pede o endereço de entrega
            tipo = input("Tipo de transporte (carro/moto/bike): ") #Pede o tipo de transporte desejado
            distancia = 5.0 #Pede a distância da entrega (aqui está fixa, mas poderia ser calculada com base em um serviço de mapas)
            transporte = Transporte(tipo, taxa_km=2.0, tempo_estimado=20, distancia=distancia)# #Cria uma instância de transporte com os dados fornecidos
            taxa_entrega = transporte.calcular_custo() #Calcula o custo da entrega com base na distância e taxa por km

            pedido = cliente.solicitar_pedido( #Cria um novo pedido com os dados fornecidos
                id_pedido=str(random.randint(1000, 9999)), # ID gerado aleatoriamente
                entrega_prevista=date.today(), # Data de entrega prevista
                transporte=transporte, # Transporte escolhido
                valor_total=valor_produtos, # Valor total dos produtos
                endereco_destino=destino # Endereço de entrega
            )
            pedido.produtos = produtos_escolhidos # Adiciona os produtos escolhidos ao pedido
            todos_os_pedidos.append(pedido) # Adiciona o pedido à lista de pedidos
            vendedor_escolhido.adicionar_pedido(pedido) # Adiciona o pedido à lista de pedidos do vendedor
            salvar_objeto(autenticador, "autenticador.pkl") # Salva o autenticador atualizado
            salvar_objeto(todos_os_pedidos, "pedidos.pkl") # Salva a lista de pedidos atualizada

            print(f"Pedido criado com sucesso! ID do pedido: {pedido.id_pedido}")
            print(f"Produtos: {[p.nome for p in produtos_escolhidos]}") # Lista de produtos escolhidos
            print(f"Total: R${valor_produtos:.2f} + Entrega: R${taxa_entrega:.2f} = R${valor_produtos + taxa_entrega:.2f}") # Valor total com entrega

        elif opcao == "2":
            for pedido in cliente.visualizar_historico_pedidos(): 
                print(f"ID: {pedido.id_pedido} | Status: {pedido.status} | Valor: R${pedido.valor_total}") # Exibe o histórico de pedidos do cliente

        elif opcao == "3":
            id_pedido = input("ID do pedido a avaliar: ") #Pede o ID do pedido a ser avaliado
            for pedido in cliente.historico_pedidos:
                if pedido.id_pedido == id_pedido:
                    nota = int(input("Nota (0 a 5): "))# Pede a nota da avaliação
                    comentario = input("Comentário: ")
                    cliente.avaliar_entrega(pedido, nota, comentario) # Avalia a entrega
                    salvar_objeto(autenticador, "autenticador.pkl")
                    print("Avaliação registrada!")
                    break # Sai do loop após encontrar o pedido
                print("Pedido não encontrado.")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


def menu_entregador(entregador): # Exibe o menu de opções para entregadores, entregador: instância da classe Entregador autenticada
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
            for pedido in todos_os_pedidos:
                if pedido.status == "Criado":
                    print(f"ID: {pedido.id_pedido} | Valor: R${pedido.valor_total:.2f} | Status: {pedido.status}")

        elif opcao == "2":
            id_escolhido = input("Digite o ID do pedido que deseja aceitar: ")
            for pedido in todos_os_pedidos:
                if pedido.id_pedido == id_escolhido and pedido.status == "Criado": #Verifica se o pedido está disponível com esse if o pedido é criado
                    entregador.aceitar_entrega(pedido) #Aceita o pedido
                    salvar_objeto(autenticador, "autenticador.pkl")
                    salvar_objeto(todos_os_pedidos, "pedidos.pkl")
                    break
            else:
                print("Pedido não encontrado ou já aceito.") #Se o pedido não for encontrado ou já tiver sido aceito, exibe mensagem de erro

        elif opcao == "3":
            id_finalizar = input("Digite o ID do pedido a finalizar: ") #Pede o ID do pedido a ser finalizado
            for pedido in todos_os_pedidos:
                if pedido.id_pedido == id_finalizar and pedido.status == "Em andamento": #Verifica se o pedido está em andamento
                    entregador.finalizar_entrega(pedido) #Finaliza o pedido
                    salvar_objeto(autenticador, "autenticador.pkl")
                    salvar_objeto(todos_os_pedidos, "pedidos.pkl")
                    break
            else:
                print("Pedido não encontrado ou ainda não aceito.")

        elif opcao == "4":
            print("\nEntregas finalizadas:")
            for pedido in entregador.listar_entregas_finalizadas():
                print(f"ID: {pedido.id_pedido} | Status: {pedido.status}") #Exibe as entregas finalizadas pelo entregador
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")


def menu_vendedor(vendedor): #Exibe o menu de opções para vendedores, vendedor: instância da classe vendedor autenticada
    while True:
        print("\n--- Menu Vendedor ---")
        print("1. Ver pedidos recebidos")
        print("2. Ver produtos disponíveis")
        print("3. Adicionar novo produto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if todos_os_pedidos:
                for pedido in todos_os_pedidos: #Verifica se há pedidos recebidos
                    print(f"ID: {pedido.id_pedido} | Status: {pedido.status} | Valor: R${pedido.valor_total:.2f}") # Exibe os pedidos recebidos
            else:
                print("Nenhum pedido recebido ainda.")

        elif opcao == "2":
            print("\nProdutos da loja:")
            for produto in vendedor.produtos:
                print(f"- {produto.nome}: R${produto.preco:.2f}") # Exibe os produtos disponíveis na loja do vendedor

        elif opcao == "3": 
            nome_produto = input("Nome do novo produto: ")
            preco_produto = float(input("Preço do produto (R$): "))
            novo_produto = Produto(nome_produto, preco_produto) # Cria um novo produto com os dados fornecidos
            vendedor.produtos.append(novo_produto) # Adiciona o novo produto à lista de produtos do vendedor
            print(f"Produto '{nome_produto}' adicionado com sucesso!")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


print("Você deseja logar ou se cadastrar? (login/cadastro): ", end="") #Pede para o usuário escolher entre logar ou se cadastrar
modo = input().strip().lower()

if modo == "login":
    tipo = input("Você quer logar como (cliente / entregador / vendedor)? ").strip().lower()
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    conta_logada = autenticador.autenticar(email, senha)
    if conta_logada and conta_logada.tipo_usuario.strip().lower() == tipo.strip().lower(): #Verifica se a conta logada corresponde ao tipo de usuário
        usuario = conta_logada.usuario
        if tipo == "cliente": # Verifica o tipo de usuário e chama a função correspondente
            menu_cliente(usuario) 
        elif tipo == "entregador": # 
            menu_entregador(usuario)
        elif tipo == "vendedor":
            menu_vendedor(usuario)
    else:
        print("Login inválido ou tipo incorreto.")
        exit()

elif modo == "cadastro":  #Pede para o usuário se cadastrar
    tipo_usuario = input("Você é (cliente / entregador / vendedor)? ").lower() 
    nome = input("Nome completo: ")
    rua = input("Nome da rua: ")
    numero = input("Número: ")
    endereco = f"{rua}, Nº {numero}"

    while True:
        telefone = input("Telefone: ")
        if telefone.isdigit():
            break
        else:
            print("Telefone inválido! Digite apenas números.")

    email = input("Email: ")

    while True:
        senha = input("Senha (mín. 8 caracteres, 1 maiúscula, 1 símbolo como #@$%): ")
        if (
            len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and # Verifica se há pelo menos uma letra maiúscula
            re.search(r"[#@\$%]", senha) # Verifica se há pelo menos um símbolo
        ):
            break
        else:
            print("Senha inválida! A senha deve ter:")
            print("- Pelo menos 8 caracteres")
            print("- Pelo menos uma letra maiúscula")
            print("- Pelo menos um símbolo como # @ $ %")

    
    while True:
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
        except ValueError as e: # Verifica se a senha atende aos requisitos 
            print(f"Erro: {e}. Tente novamente.") # Se a senha não atender aos requisitos, exibe mensagem de erro


    if tipo_usuario == "cliente": # Verifica o tipo de usuário e cria a conta correspondente
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

    autenticador.cadastrar_conta(nova_conta) # Adiciona a nova conta ao autenticador
    salvar_objeto(autenticador, "autenticador.pkl") # Salva o autenticador atualizado 
    print(f"Cadastro realizado com sucesso! Bem-vindo(a), {nome}.") # Exibe mensagem de boas-vindas

    if tipo_usuario == "cliente": # Se o tipo de usuário for cliente, chama a função correspondente
        menu_cliente(nova_conta.usuario)
    elif tipo_usuario == "entregador": # Se o tipo de usuário for entregador, chama a função correspondente
        menu_entregador(nova_conta.usuario)
    elif tipo_usuario == "vendedor": # Se o tipo de usuário for vendedor, chama a função correspondente
        menu_vendedor(nova_conta.usuario)

    else:
        print("Opção inválida. Encerrando o sistema.") # Se a opção for inválida, encerra o sistema
