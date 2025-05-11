from datetime import date, datetime
from cliente import Cliente
from vendedor import vendedor
from entregador import Entregador
from transporte import Transporte
from pedido import Pedido
from pagament import Pagamento
from notificacao import Notificacao
from conta import Conta


cliente1 = Cliente("João Pedro", "Rua Michel Thomé, 903", "67 981686580", "borgesjpbd@gmail.com", "12345689")

pedidos = []

def menu():
    while True:
        print("\n SPEEDBOX Sua facilitadora em entregas")
        print("=====================================")
        print("1. Fazer novo pedido")
        print("2. Ver histórico de pedidos")
        print("3. Avaliar entrega")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fazer_pedido()
        elif opcao == "2":
            ver_historico()
        elif opcao == "3":
            avaliar_pedido()
        elif opcao == "4":
            print("Obrigado por usar a Speedbox! Até mais.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def fazer_pedido():
    destino = input("Endereço de entrega: ")
    valor = float(input("Valor dos produtos: "))
    tipo_transporte = input("Tipo de transporte (moto/bicicleta/carro): ")
    
    
menu()
