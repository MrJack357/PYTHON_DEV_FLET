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

    # criar chat
    campo_enviar_mensagem = ft.TextField(label="Escreva sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar")

    # função para entrar no chat
    def entrar_chat(evento):
        # fechar popup
        popup.open = False
        #sumir com o titulo e botão
        pagina.remove(titulo)
        pagina.remove(botao)
        # criar chat
        # carregar campo de texto
        pagina.add(campo_enviar_mensagem)
        # botão enviar
        pagina.add(botao_enviar)

    pagina.update()

    # criar popup
    titulo_popup =  ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup =  ft.AlertDialog(title= titulo_popup, content= caixa_nome, actions=[botao_popup])

    # botão de iniciar chat
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    # colocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)

# executar a função com o flet
ft.app(main, view=ft.WEB_BROWSER)