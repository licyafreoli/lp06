username_correct = "admin"
password_correct = "1234"
max_attempts = 3

def login_system():
    attempts = max_attempts
    while attempts > 0:
        username = input("Digite o nome de usuário: ")
        password = input("Digite a senha: ")
        
        if username == username_correct and password == password_correct:
            print("Bem-vindo(a)!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Credenciais incorretas. Você tem {attempts} tentativa(s) restante(s).")
    
    for _ in range(3):
        print("Acesso bloqueado")

login_system()
