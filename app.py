import os

restaurantes = [ 
    {'nome': 'Outback',
     'categoria': 'Italiana',
     'especialidade': 'Costela com Barbecue',
     'ativo': True
    }, { 
     'nome': 'MaoKai',
     'categoria': 'Japonesa',
     'especialidade': 'Yakisoba',
     'ativo': False
    }
]

def exibir_nome_do_programa():
    nome = "ᔕᗩᗷᗝᖇ ᗴ᙭ᑭᖇᗴᔕᔕ"
    linha = '*' * (len(nome))
    print(f'\n{linha}')
    print(nome)
    print(linha)
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status de restaurante')
    print('4. Sair\n')
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            status_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    padroniza_restaurantes()
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    especiadade_do_restaurante = input(f'Agora digite a especialidade do restaurante {nome_do_restaurante} ')
    categoria_do_restaurante = input(f'Ainda, diga a categoria que o restaurante {nome_do_restaurante} se enquadra ')
    
    dados_novo_restaurante = { 'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'especialidade': especiadade_do_restaurante, 'ativo': False}
    restaurantes.append(dados_novo_restaurante)
    
    print(f'O restaurante {nome_do_restaurante}, de categoria {categoria_do_restaurante} e especialidade: {especiadade_do_restaurante}, foi cadastrado com sucesso!')
    
    
    voltar_ao_menu_principal()
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    padroniza_restaurantes()
    print(f'  {'NOME'.ljust(22)} | {'CATEGORIA'.ljust(22)} | {'ESPECIALIDADE'.ljust(22)} | {'ATIVIDADE'}\n')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria_do_restaurante = restaurante['categoria']
        especiadade_do_restaurante = restaurante['especialidade']
        atividade_do_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        
        print(f'- {nome_do_restaurante.ljust(22)} | {categoria_do_restaurante.ljust(22)} | {especiadade_do_restaurante.ljust(22)} | {atividade_do_restaurante}')
 
    voltar_ao_menu_principal()
def status_restaurante():
    exibir_subtitulo('Alternando statatus do restaurante')
    padroniza_restaurantes()
    nome_do_restaurante = input('Digite o nome do restaurante que desejas alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante.lower().title() in restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo'] == True:
                mensagem = print(f'O restaurante "{nome_do_restaurante}" foi ativado com sucesso!')
            elif restaurante['ativo'] == False:
                mensagem = print(f'O restaurante "{nome_do_restaurante}" foi desativado com sucesso!')
    if not restaurante_encontrado:
        print(f'Restaurante "{nome_do_restaurante}" não indentificado.')
    voltar_ao_menu_principal()
def finalizar_app():
    exibir_subtitulo('App finalizado')

def padroniza_restaurantes():
    for restaurante in restaurantes:
        restaurante['nome'] = restaurante['nome'].lower().title()
        restaurante['categoria'] = restaurante['categoria'].lower().title()
        restaurante['especialidade'] = restaurante['especialidade'].lower().title()
        restaurante['ativo'] = str(restaurante['ativo']).lower().title()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()