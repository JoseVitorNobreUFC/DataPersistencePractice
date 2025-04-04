def menu():
  print("=== Lista de Tarefas ===")
  print("1 - Adicionar tarefa")
  print("2 - Listar tarefas")
  print("3 - Buscar tarefa")
  print("4 - Remover tarefa")
  print("0 - Sair")
  return input("Escolha uma opção: ")

def adicionar_tarefa():
  tarefa = input("Digite a descrição da tarefa: ")
  with open("./Aula01/tarefas.txt", "a", encoding="utf-8") as file:
    file.write(tarefa + "\n")

  print("Tarefa adicionada com sucesso!")

def listar_tarefas():
  try:
    with open("./Aula01/tarefas.txt", "r", encoding="utf-8") as file:
      tarefas = file.readlines()
      print("=== Tarefas ===")
      for tarefa in tarefas:
        print(tarefa.strip())
      print("===============")
  except FileNotFoundError:
    print("Nenhuma tarefa encontrada.")

def buscar_tarefa():
  try:
    with open("./Aula01/tarefas.txt", "r", encoding="utf-8") as file:
      tarefas = file.readlines()
      tarefasEncontradas = []
      tarefaProcurada = input("Digite a descrição da tarefa: ")
      for tarefa in tarefas:
        if tarefaProcurada in tarefa:
          tarefasEncontradas.append(tarefa)
      print("=== Tarefas Encontradas ===")
      for tarefa in tarefasEncontradas:
        print(tarefa.strip())
      print("===========================")
  except FileNotFoundError:
    print("Nenhuma tarefa encontrada.")


def remover_tarefa():
  try:
    with open("./Aula01/tarefas.txt", "r", encoding="utf-8") as file:
      tarefas = file.readlines()
      tarefaId = int(input("Digite o ID da tarefa que deseja remover: "))
      for i, tarefa in enumerate(tarefas):
        if tarefaId == i - 1:
          tarefas.pop(i)
          break
      with open("./Aula01/tarefas.txt", "w", encoding="utf-8") as file:
        for tarefa in tarefas:
          file.write(tarefa)
      print("Tarefa removida com sucesso!")
  except FileNotFoundError:
    print("Nenhuma tarefa encontrada.")

while True:
  opcao = menu()
  if opcao == "1":
    adicionar_tarefa()
  elif opcao == "2":
    listar_tarefas()
  elif opcao == "3":
    buscar_tarefa()
  elif opcao == "4":
    remover_tarefa()
  elif opcao == "0":
    break