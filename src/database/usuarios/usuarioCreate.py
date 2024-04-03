from database.connection import database

def usuarioCreate(nome, endereco, rg):
    global database
    usuario = {
        "nome": nome,
        "endereco": endereco,
        "rg": rg
    }

    try:
        database.usuario.insert_one(usuario)
        print()
        print("Usuario registrado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA INSERÇÃO DE USUARIO !")
        input()
