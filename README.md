Aqui está o README para o seu projeto **Hashzap**:

---

# Hashzap - Chat Interativo em Tempo Real

**Hashzap** é um chat interativo criado com a biblioteca Flet em Python. O aplicativo permite aos usuários interagir em tempo real com outros participantes após se registrarem com um nome de usuário. Ele demonstra funcionalidades simples como enviar mensagens e exibir o conteúdo do chat em uma interface amigável.

## Funcionalidades

- **Tela inicial**: Com um botão "Iniciar Chat", que ao ser clicado, direciona o usuário para a tela de boas-vindas.
- **Tela de boas-vindas**: Exibe um campo de texto para que o usuário insira seu nome e um botão "Entrar no Chat".
- **Tela de Chat**: Depois de entrar, o usuário pode enviar mensagens e vê-las sendo exibidas no chat em tempo real.
- **Comunicação em tempo real**: O aplicativo utiliza a funcionalidade de "túnel de conexão" para permitir que todos os usuários que estão conectados vejam as mensagens enviadas.

## Tecnologias Utilizadas

- **Python**  
- **Flet**: Para a construção da interface do usuário e a interação entre os elementos.

## Como Usar

1. Clone ou baixe o repositório.
2. Instale as dependências necessárias, como Flet, usando o seguinte comando:
   ```bash
   pip install flet
   ```
3. Execute o script Python:
   ```bash
   python app.py
   ```
4. O aplicativo abrirá automaticamente no navegador. 
5. Insira seu nome e comece a interagir no chat!

## Estrutura do Código

- **Funções principais**:
  - `main(pagina)`: Função principal que define os elementos da página, como os botões e a interação do chat.
  - `enviar_mensagem`: Envia a mensagem do usuário para todos os participantes.
  - `entrar_chat`: Função chamada quando o usuário entra no chat, escondendo a tela de boas-vindas e mostrando o chat.
  - `abrir_popup`: Exibe a tela inicial para o usuário inserir seu nome.

- **Componentes**:
  - `popup`: Tela de boas-vindas onde o usuário insere seu nome.
  - `chat`: Área onde as mensagens são exibidas.
  - `campo_enviar_mensagem`: Campo de texto para enviar as mensagens.
  - `botao_enviar`: Botão para enviar mensagens.

## Contribuições

Contribuições são bem-vindas! Se você deseja melhorar o projeto ou adicionar novas funcionalidades, faça um fork do repositório, crie uma branch e envie um pull request com suas alterações.

---

Esse README deve te ajudar a documentar bem o projeto e dar uma visão geral clara para os outros que forem acessá-lo! Se precisar de algo mais, é só avisar. 😊
