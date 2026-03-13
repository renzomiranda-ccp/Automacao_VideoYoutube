🤖 Python Web Automation

📌 Sobre o Projeto

Este projeto demonstra automação de tarefas no computador utilizando Python e a biblioteca PyAutoGUI. O objetivo é simular ações humanas como pressionar teclas, digitar textos e clicar na tela para automatizar processos repetitivos.

A automação implementada abre o navegador, acessa o YouTube, realiza uma pesquisa e seleciona um vídeo automaticamente. O projeto também inclui um utilitário para identificar coordenadas do cursor do mouse, permitindo configurar cliques com precisão durante a automação.

Este projeto foi desenvolvido como prática de automação de interface gráfica (GUI Automation) e organização de scripts Python em uma estrutura de projeto mais profissional.



✨ Funcionalidades

   • Abrir automaticamente o navegador

   • Realizar pesquisas automáticas no YouTube

   • Simular cliques do mouse em posições específicas

   • Simular digitação e atalhos de teclado

   • Identificar coordenadas do cursor para automações

   • Código modular para reutilização em outros scripts


🛠 Tecnologias Utilizadas

   • Python 3

   • PyAutoGUI – automação de teclado e mouse

   • time – controle de pausas entre ações


📂 Estrutura do Projeto

Descrição dos Arquivos:

• abrir_navegador.py

•  Contém funções reutilizáveis para abrir e controlar o navegador.

•  automacao_youtube.py

• Script principal responsável por executar a automação de busca no YouTube.

•  posicao_mouse.py

•  Ferramenta auxiliar para descobrir as coordenadas da posição do mouse na tela.


📍 Encontrar coordenadas do mouse

Para descobrir as coordenadas usadas em cliques automatizados:

  • python src/posicao_mouse.py

  • O programa aguardará alguns segundos para que você posicione o mouse e então exibirá no terminal a posição (x, y) do cursor.


⚠️ Observações

As coordenadas utilizadas para os cliques podem variar dependendo de fatores como:

   • resolução da tela

   • tamanho da janela do navegador

   • layout da página

   Caso necessário, utilize o script posicao_mouse.py para ajustar as posições de clique.


🎯 Objetivo do Projeto

Este projeto foi criado com o objetivo de praticar:

   • automação de tarefas no computador

   • manipulação de teclado e mouse com Python

   • organização de projetos em múltiplos arquivos

   • criação de scripts reutilizáveis


🚀 Possíveis Melhorias Futuras

   • Automação com reconhecimento de elementos na tela

   • Suporte para múltiplos navegadores

   • Interface gráfica para controlar as automações

   • Execução de múltiplas pesquisas automaticamente

   • Uso de bibliotecas de automação web mais robustas como Selenium



👨‍💻 Autor

   Projeto desenvolvido por Renzo Miranda como parte dos estudos em Ciência da Computação e automação com Python.
