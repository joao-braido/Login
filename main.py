usuarios = {
  "Braido": "1234",
  "Leleo" : "4321",
}

def verificar_credenciais(usuario, senha):
  print("Verificando as credenciais...")
  if usuario in usuarios and usuarios[usuario] == senha:
    return True
  else:
    raise ValueError("Nome de usuário ou senha incorreto")

def login():
  while True:
    try:
      usuario = input("Digite seu nome de usuario (ou digite 'sair' para encerrar)")
      if usuario == 'sair':
        print("encerrando...")
        break
      senha = input("Digite sua senha: ")

      if verificar_credenciais(usuario, senha):
        print(f"Login bem sucedido. Bem vindo, {usuario}") 

      break
    except ValueError as e:
      print(e)
    else:
      print("Você está logado com sucesso")
  
    finally:
      print("tentativa de login finalizada")

login()