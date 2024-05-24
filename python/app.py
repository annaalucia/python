import os

def Main():
    chama_nome_app()
    lista_opcoes()

def Sair():
    os.system("cls")
    print("Finalizando seção!\n")

def chama_nome_app():
    print("TicketShow")

def lista_opcoes():
    print("1-Ver shows")
    print("2-Datas dos shows")
    print("3-Ingressos disponíveis")
    print("4-Comprar ingressos")
    print("5-Sair")

if __name__=="__main__":
    Main()
    OPCAO_DIGITADA = int(input("Selecione uma opção: "))

if (OPCAO_DIGITADA == 1):
    print("Você escolheu a opção Ver shows")
elif(OPCAO_DIGITADA == 2):
    print("Você escolheu a opção Datas dos shows")
elif(OPCAO_DIGITADA == 3):
    print("Você escolheu a opção Ingressos disponíveis")
elif(OPCAO_DIGITADA == 4):
    print("Você escolheu a opção Comprar ingressos")
elif(OPCAO_DIGITADA == 5):
    Sair()