# Lucas Garcia Marques

import time
import os

lst_nome = []
lst_idade = []
lst_peso = []
lst_altura = []
lst_imc = []

def limpaTela():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

def calculaIMC(peso, altura):
  try:
    imc = peso / (altura * altura)
    return round(imc, 2)
  except ZeroDivisionError:
    print("Não é possível dividir por zero.")

def incluiAluno():
  while True:
    print("----- CADASTRO DE ALUNOS -----")
    nome = input("Digite o nome do aluno (ou 'F' para encerrar): ")
    if nome == "":
      print("O nome do aluno não pode estar vazio. Digite novamente. ")
      break
    elif nome.upper() == 'F':
      print("Encerrando o cadastro ...\n")
      time.sleep(1)
      limpaTela()
      break
    else:
      idade = int(input("Digite a idade do aluno: "))
      peso = float(input("Digite o peso do aluno: "))
      altura = float(input("Digite a altura do aluno: "))
  
      imc = calculaIMC(peso, altura)
  
      lst_nome.append(nome)
      lst_idade.append(idade)
      lst_peso.append(peso)
      lst_altura.append(altura)
      lst_imc.append(imc)
  
      print("Aluno adicionado com sucesso!\n")
      time.sleep(1)
      limpaTela()

def listaAlunos():
  limpaTela()
  try:
    if len(lst_nome) == 0:
      print("Não há alunos na lista.")
    else:
      print("--------------------------------------")
      print("INFORMAÇÕES DO ALUNO(S) CADASTRADO(S):")
      print("--------------------------------------")
      for i in range(len(lst_nome)):
        print(f'Aluno {i + 1}:')
        print(f'Nome: {lst_nome[i]}')
        print(f'Idade: {lst_idade[i]}')
        print(f'Peso: {lst_peso[i]}')
        print(f'Altura: {lst_altura[i]}')
        print(f'IMC: {lst_imc[i]:.2f}')
        print("------------------------")
  
    media_imc = sum(lst_imc) / len(lst_imc)
    print(f'A média do IMC dos alunos cadastrados: {media_imc:.2f}\n')
  except ZeroDivisionError:
    print("Cadastre alguns alunos ...")

def listaAluno():
  limpaTela()
  while True:
    if len(lst_nome) == 0:
      print("Não há alunos na lista.")
      break

    nome = input("Digite o nome do aluno para pesquisar (ou 'F' para encerrar): ")

    if nome.upper() == 'F':
      break
    elif nome == "":
        print("O nome do aluno não pode estar vazio. Digite novamente. ")
        break
    elif nome not in lst_nome:
      print("Aluno não encontrado.\n")
      return
  
    i = lst_nome.index(nome)
    
    print("--------------------------------")
    print("INFORMAÇÕES DO ALUNO CADASTRADO:")
    print("--------------------------------")
    print(f'Aluno {i + 1}:')
    print(f'Nome: {lst_nome[i]}')
    print(f'Idade: {lst_idade[i]}')
    print(f'Peso: {lst_peso[i]}')
    print(f'Altura: {lst_altura[i]}')
    print(f'IMC: {lst_imc[i]:.2f}')

def listaAlunoIdade():
  limpaTela()
  idade = int(input("Digite a idade do alunos: "))
  alunos_idade = []

  for i in range(len(lst_nome)):
    if lst_idade[i] == idade:
      alunos_idade.append(i)

  if not alunos_idade:
    print("Não há alunos com essa idade.")
    return
    
  print("------------------------------------")
  print(f'INFORMAÇÕES DOS ALUNOS COM {idade} ANOS:')
  print("------------------------------------")
  for i in alunos_idade:
    print(f'Aluno {i + 1}:')
    print(f'Nome: {lst_nome[i]}')
    print(f'Idade: {lst_idade[i]}')
    print(f'Peso: {lst_peso[i]}')
    print(f'Altura: {lst_altura[i]}')
    print(f'IMC: {lst_imc[i]:.2f}\n')

  media_imc = sum([lst_imc[i] for i in alunos_idade]) / len(alunos_idade)
  print(f'IMC médio do grupo: {media_imc:.2f}')

def excluiAluno():
  limpaTela()
  nome = input("Digite o nome de um aluno para excluir: ")

  if len(lst_nome) == 0:
      print("Não há alunos na lista.")
  elif nome not in lst_nome:
    print("Aluno não encontrado.")
    return

  index = lst_nome.index(nome)

  lst_nome.pop(index)
  lst_idade.pop(index)
  lst_peso.pop(index)
  lst_altura.pop(index)
  lst_imc.pop(index)

  print(f'O aluno {nome} foi excluído!\n')

def exibeMenu():
  print("---- CADASTRO DE ALUNOS ----")
  print("1 - Incluir Aluno")
  print("2 - Listar todos alunos e seus dados")
  print("3 - Listar os dados de um aluno")
  print("4 - Listar os dados de todos alunos de uma determinada idade")
  print("5 - Excluir um aluno")
  print("9 - Fim")

def leOpcao():
  opcao = input("Digite a opção desejada: ")
  return opcao
  
def executaOpcao(opcao):
  if opcao == "1":
    incluiAluno()
  elif opcao == "2":
    listaAlunos()
  elif opcao == "3":
    listaAluno()
  elif opcao == "4":
    listaAlunoIdade()
  elif opcao == "5":
    excluiAluno()
  elif opcao == "9":
    print("Encerrando o programa.")
    time.sleep(1)
    quit()
  else:
    print("Opção inválida. Tente novamente.")

def main():
  while True:
    exibeMenu()
    opcao = leOpcao()
    executaOpcao(opcao)

if __name__ == '__main__':
  main()