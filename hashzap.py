# Tela inicial
    # Titulo: Hashzap
    # Botão: Iniciar chat
        # quando clicar no botão, abrirá a tela de chat
            #Titulo Bem vindo ao Hashzap
            # caixa de texto: escreva seu nome
            # botao: entrar no chat
                # quando clicar no botão, abrirá a tela de chat e sumirá a tela de boas vindas
                    # carregar chat
                    # carregar campo de texto: escreva sua mensagem
                    # botão: enviar
                        # quando clicar no botão, a mensagem será enviada e aparecerá no chat
                        # limpar campo de texto

# Flet 
# importar o flet
import flet as ft

# criar uma função para a rodar o seu app
def main(pagina):
    # colocar o que essa função vai fazer

    # titulo
    titulo = ft.Text('Hashzap')
    # botão de iniciar chat
    botao = ft.ElevatedButton("Iniciar Chat")
    
    # colocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)

# executar a função com o flet
ft.app(main, view=ft.WEB_BROWSER)