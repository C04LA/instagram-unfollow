from InstagramAPI import InstagramAPI
import time

def principal():
    for user in lista_seguindo:
        if not (user['pk'] in lista_id_seguidores):
            instagram.unfollow(user['pk'])
            print('Você eliminou o seguidor da sua conta: {} com sucesso!'.format(user['username']))
            time.sleep(5)

def layout():
    print('_____________________________________________')
    print('            INSTAGRAM UNFOLLOW   ')
    print('      CREATE BY:  https://github.com/C04LA   ')
    print('_____________________________________________')
    print('')

# isso irá aparecer em sua tela. Caso queira deixar mais rápido comentar essas linhas e tirar os comentarios da linha
# debaixo e definir seu usuario e senha. Assim não irá precisa inserir toda vez que abrir o programa

layout()

user = input('Usuário: ') # essa linha e essa deve ser comenta caso queria automatizar
passwd = input('Senha: ')  # essa linha e essa deve ser comenta caso queria automatizar

# caso queira automatizar retirar o comentario das duas linhas e comentar as linhas de cima
#user = 'seu_usuario'
#passwd = 'sua_senha'

instagram = InstagramAPI(user, passwd)
instagram.login()

id_account = instagram.username_id
lista_seguidores = instagram.getTotalFollowers(id_account)
lista_id_seguidores = []

for user in lista_seguidores:
    lista_id_seguidores.append(user['pk'])

lista_seguindo = instagram.getTotalFollowings(id_account)

principal()
