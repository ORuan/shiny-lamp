import sys, requests

def verify_exists(urlRepository):
    try:
        if requests.get(urlRepository).status_code == 404:
            raise NameError('Não encontrado')
        else:
            print('Repositório verificado')
    except Exception as err:
        print(err)

if __name__ == "__main__":
    try:
        urlRepository = sys.argv[1]
        print('A url do repositório é: '+urlRepository)
        print('Fazendo verifição do repositório')
        verify_exists(urlRepository)
        print("Tudo prondo, logo estaremos pronto para sincronizar os arquivos")
    except IndexError:
        print('''
                \n
                !--------------------------------------------------------------------!\n
                Processo de automação de apropriação do servidor de arquivos do github\n
                !--------------------------------------------------------------------!\n
                Os Dados do repositório nunca serão enviados para fontes externas, el-\n
                sempre estarão armazenados locamente. Prezamos pela sua privacidade e-\n
                segurança.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
                !--------------------------------------------------------------------!\n
                Comandos abaixo:
            ''')
    