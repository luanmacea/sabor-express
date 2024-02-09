import os

restaurantes = [{"id":1, "nome":"pizza", "ativo":True},
                {"id":2, "nome":"arroz", "ativo":False},
                {"id":3, "nome":"sushi", "ativo":True}]

def retorno():
  input("\nPressione ENTER para continuar\n")
  main()

def entrada(titulo):
  os.system("cls")
  linha = "*" * (len(titulo) + 4)
  print(f"{linha}\n* {titulo} *\n{linha}\n")

def lista_restaurante():
  for restaurante in restaurantes:
    id_restaurante = str(restaurante["id"])
    nome_restaurante = restaurante["nome"]
    ativo = "ativo" if restaurante["ativo"] else "desativado"
    print(f"{id_restaurante.ljust(3)} | {nome_restaurante.ljust(10)} | {ativo}")

def exibir_nome_programa():
  print("Sabor Express\n")

def exibir_opcoes():
  print("1. Cadastrar restaurante")
  print("2. Listar restaurantes")
  print("3. Ativar restaurante")
  print("4. Sair\n")

def finalizar_app():
  entrada("Encerrando programa...")
  # exit()

def opcao_invalida():
  print("Opção inválida\n")
  retorno()

def cadastrar_restaurante():
  entrada("Cadastrando os novos restaurantes")
  nome_restaurante = input("Escreva o nome do restaurante:\n")
  print(f"O restaurante {nome_restaurante} ativo?\n")
  ativo = input("Digite 1 para sim e 2 para não\n")
  if (ativo == "1"):
    ativo = True
  elif (ativo == "2"):
    ativo = False
  else:
    opcao_invalida()
  id = len(restaurantes) + 1
  restaurante = {"id": id, "nome": nome_restaurante, "ativo": ativo}
  restaurantes.append(restaurante)
  print(f"Restaurante {nome_restaurante} adicionado\n")
  retorno()

def ativar_restaurante():
  entrada("Restaurantes cadastrados:")
  lista_restaurante()
  numero = int(input("\nDigite o numero do restaurante que deseja mudar o status de ativo: \n"))
  if(numero > len(restaurantes)):
    print("\nRestaurante inexistente\n")
    opcao_invalida()
  for restaurante in restaurantes:
    if (restaurante["id"] == numero):
      restaurante["ativo"] = not restaurante["ativo"]
  retorno()

def listar_restaurante():
  entrada("Os restaurantes cadastrados sao:")
  lista_restaurante()
  retorno()

def escolher_opcao():
  try:
    opcao_escolhida = int(input("Escolha uma opção: "))

    if (opcao_escolhida == 1):
      cadastrar_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurante()
    elif opcao_escolhida == 3:
      ativar_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system("cls")
  exibir_nome_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == "__main__":
  main()


