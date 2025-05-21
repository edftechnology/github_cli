<!-- LOGOTIPO DO PROJETO -->
<div style="display: flex; justify-content: center;">
   <a href="https://github.com/edendenis/git">
     <img src="figures/gold_edf_technology_logo_transparent_background_and_gold_name.png" alt="Logo" width="160" height="160">
   </a>
</div>

<h3 align="center">Configurar/Instalar/Usar o `GitHub Command Line Interface (GitHub CLI)` e descrição dos seus principais comandos</h3>

<!-- <div style="display: flex; justify-content: center;">
  <a href="https://zenodo.org/doi/10.5281/zenodo.10668919">
    <img src="https://zenodo.org/badge/758237447.svg" alt="DOI">
  </a>
</div> -->

<p align="center">
 Neste documento estão contidos os principais comandos para configurar/instalar/usar o `GitHub Command Line Interface (GitHub CLI)`.
 <br />
 <a href="https://github.com/edendenis/git"><strong>Explore os documentos »</strong></a>
 <br />
 <br />
 <a href="https://github.com/edendenis/git">Ver demonstração</a>
 ·
 <a href="https://github.com/edendenis/git">Relatar bug</a>
 ·
 <a href="https://github.com/edendenis/git">Solicitar recurso</a>
</p>


# Configurar/Instalar/Usar o `GitHub Command Line Interface (GitHub CLI)` e descrição dos seus principais comandos

## Resumo

Neste documento estão contidos os principais comandos para configurar/instalar/usar o `GitHub Command Line Interface (GitHub CLI)`.

## _Abstract_

_This document contains the main commands for configuring/installing/using the `GitHub Command Line Interface (GitHub CLI)`._


## Descrição [2]

### `Git`

O `Git` é um sistema de controle de versão distribuído amplamente utilizado para rastrear e gerenciar o código-fonte de projetos de desenvolvimento de software. Desenvolvido por Linus Torvalds, o criador do `Linux`, o `Git` é conhecido por sua eficiência, flexibilidade e capacidade de trabalhar tanto em projetos individuais quanto em equipes de desenvolvimento. Ele permite que os desenvolvedores acompanhem as alterações feitas no código, revertam para versões anteriores, colaborem em projetos e gerenciem conflitos de maneira eficaz. O `Git` também é suportado por várias plataformas de hospedagem de código, como o GitHub, o GitLab e o Bitbucket, o que o torna uma escolha central para o desenvolvimento colaborativo e a gestão de código-fonte em projetos de software.

### `GitHub Command Line Interface (GitHub CLI)`

O `GitHub Command Line Interface (GitHub CLI)` é uma ferramenta de linha de comando que permite aos usuários interagir com o GitHub diretamente pelo terminal, facilitando o gerenciamento de repositórios e a execução de tarefas comuns sem a necessidade de usar a interface web. Com o GitHub CLI, os usuários podem clonar repositórios, criar e gerenciar pull requests, visualizar problemas, e até mesmo publicar projetos, tudo através de comandos simples. Essa interface é especialmente útil para desenvolvedores que preferem trabalhar no terminal e desejam integrar suas operações no GitHub ao fluxo de trabalho de linha de comando, tornando o processo mais eficiente e produtivo.

## 1. Configurar/Instalar/usar o `Git` [1]

## 1.1 Configurar/Instalar/usar o `Git` no `Linux Ubuntu`

Para configurar/instalar/usar o `Git` no `Linux Ubuntu`, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`


2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
    
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
    
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    
    ```bash
    sudo apt full-upgrade -y
    ```

Para instalar o `GitHub CLI` no `Linux Ubuntu` pelo `Terminal Emulator`, você pode seguir os seguintes passos:

1. Abra o `Terminal Emulator`.

2. **Adicione o repositório do `GitHub CLI`**: Execute o seguinte comando para adicionar o repositório oficial do `GitHub CLI`:

    ```
    sudo apt-add-repository -y ppa:git-core/ppa
    ```

3. **Atualize a lista de pacotes**: Após adicionar o repositório, atualize a lista de pacotes com o comando:

    ```
    sudo apt update
    ```

4. **Instale o `GitHub CLI`**: Agora, você pode instalar o `GitHub CLI` usando o comando:

    ```
    sudo apt install gh -y
    ```

5. **Verifique a instalação**: Para garantir que o `GitHub CLI` foi instalado corretamente, você pode verificar a versão instalada com o comando:

    ```
    gh --version
    ```

Se tudo estiver correto, você verá a versão do `GitHub CLI` instalada em seu sistema. Agora você pode começar a usar o gh para interagir com seus repositórios do `GitHub` diretamente do terminal!

### 2. Autenticar no `GitHub` para usar o `GitHub CLI`

1. Digite o seguinte comando para iniciar o processo de autenticação:

    ```
    gh auth login
    ```

2. **Escolha a Conta e o Protocolo**: Responda às perguntas que aparecem no `Terminal Emulator`:

    2.1 Conta: Selecione `GitHub.com`.

    2.2 Protocolo preferido para operações Git: `Escolha SSH`.

3. **Envie sua Chave Pública SSH**: O `Terminal Emulator` perguntará se você deseja enviar sua chave pública SSH para sua conta do `GitHub`. O caminho padrão geralmente é:

    ```
    /home/seu_usuario/.ssh/id_rsa.pub
    ```

4. **Autenticação com navegador**:

    4.1 O `GitHub CLI` solicitará como você deseja se autenticar. Selecione a opção para fazer _login_ com um navegador.

    4.2 Você verá um código de autenticação de uso único, por exemplo:

    ```
    First copy your one-time code: 4050-A33D
    ```

5. **Abra o navegador**: Pressione `Enter` para abrir o `GitHub` em seu navegador padrão. Você será redirecionado para uma página de autenticação.

6. **Complete a autenticação**:

    6.1 Cole o código que você copiou anteriormente na página do `GitHub` e conclua o processo de autenticação.

    6.2 Após autenticar, volte ao terminal e pressione Enter para continuar.

7. Configure o Protocolo Git: O `GitHub CLI` deve configurar automaticamente o protocolo Git. Você verá uma mensagem de confirmação:

    ```
    ✓ Configured git protocol
    ```

8. **Erros Possíveis**: Se aparecer um erro como `HTTP 422: Validation Failed`, isso pode indicar que a chave SSH já está em uso. Nesse caso, verifique se a chave pública já está adicionada à sua conta do `GitHub`.

Agora, você deve ter criado um repositório no `GitHub` e autenticado sua conta com sucesso usando o `GitHub CLI`! Se tiver alguma dúvida ou se algo não funcionar como esperado, sinta-se à vontade para perguntar.


## 3 Criar repositório e enviar os arquivos e pastas

### 3.1 Comandos pelo `Git Hub CLI (Command Line Interface, CLI)` do `gh`

1. Entrar na pasta do repositório que será enviado para o `Git`:

    ```bash
    cd <nome_do_repositorio>
    ```

    Substitua `<nome_do_repositorio>` pelo nome que você deseja.

2. Caso **NÃO** possua arquivo `README.md` já escrito e deseja adicionar um arquivo, execute o comando a seguir:

    ```bash
    echo " <nome_do_repositorio>" >> README.md
    ```

    Substitua `<nome_do_repositorio>` pelo nome que você deseja.

3. **Inicializa um novo repositório `Git` no diretório atual**:

    ```bash
    git init
    ```

4. **Criar o repositório**: Com o `GitHub CLI`, você pode criar um novo repositório usando:

    ```bash
    gh repo create <nome-do-repositorio> --private
    ```

    Substitua `<nome-do-repositorio>` pelo nome que você deseja e use `--public` ou `--private` para definir a visibilidade do repositório.

5. **Verificar as _branches_ locais**: Primeiro, verifique quais _branches_ existem no seu repositório local usando o comando

    ```bash
    git branch
    ```

    Isso lista todas as _branches_ locais.
    
6. **Certifique-se de que a `branch` `"main"` exista**: Se não existir ou se não existir nenhuma, você pode criá-la a partir da `branch` atual ou mudar para ela usando:

    ```bash
    git branch -M main
    ```

    Isso cria uma nova `branch main"` baseada na `branch` atual.

7. **Atualizar a URL do Repositório Remoto**: Certifique-se de que a URL do seu repositório remoto esteja configurada para usar SSH:

    ```bash
    git remote add origin git@github.com:edendenis/<nome-do-repositorio>.git
    ```

8. **Consultar se a URL do seu repositório local está configurada com o repositório remoto para usar SSH**:

    ```
    git remote -v
    ```

9. **Adicionar um novo repositório remoto chamado `origin` ao seu repositório `Git` local**: O `origin` é o nome padrão usado para referir-se ao repositório remoto principal:

    ```
    git add .
    ```

9. **Fazer um `commit`**: Após criar a `branch` `"main"`, você precisa fazer pelo menos um `commit` nela. Adicione arquivos, faça o `commit` e forneça uma mensagem de `commit`:

    ```bash
    git commit -m "first commit within branch main"
    ```

10. **Enviar seu repositório local para o `GitHub`**: Finalmente, envie seu repositório para o `GitHub`:

    ```bash
    git push -u origin HEAD:main
    ```

Esses comandos permitem que você crie um repositório no `GitHub` e o gerencie completamente a partir da linha de comando.


## 4. Consultar Repositórios no `GitHub` com o `GitHub CLI`

Você pode consultar os repositórios diretamente pelo terminal. Aqui está como você pode fazer isso:

1. **Listar seus repositórios no `GitHub`**: Após estar autenticado, você pode listar todos os repositórios associados à sua conta com o comando:

    ```bash
    gh repo list
    ```
    Esse comando irá listar todos os repositórios públicos e privados (dependendo das permissões de acesso) associados à sua conta `GitHub`.

    O `GitHub CLI` (`gh`) mostra apenas 30 repositórios por vez por padrão. Para visualizar todos os seus repositórios, você pode adicionar o parâmetro `--limit` para aumentar o número de repositórios mostrados.

    1.1 **Passo para listar todos os repositórios**:
    
    ```bash
    gh repo list --limit 1000
    ```

    Isso deve mostrar até `1000` repositórios, se você os tiver.

    Se você ainda não consegue ver todos os repositórios, pode realizar a paginação para listar todos.

    1.2 Se você quiser listar repositórios de uma organização específica, você pode adicionar o nome da organização:

    ```bash
    gh repo list <organization-name>
    ```

4. **Filtrar repositórios**: Você também pode filtrar os repositórios usando a opção `--visibility` (para listar apenas públicos ou privados):

    ```bash
    gh repo list --visibility public
    ```

<!-- LICENÇA -->
## Licença

Distribuído sob a licença MIT. Consulte `LICENSE.txt` para obter mais informações.

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

<!-- ROTEIRO -->
## Roteiro

- [x] Adicionar registro de alterações

- [x] Adicionar links de volta ao topo

- [x] Adicionar modelos adicionais com exemplos

- [x] Suporte multilíngue

     - [ ] Espanhol

     - [ ] Inglês

     - [ ] Português

     - [x] Português brasileiro 

Consulte os [problemas abertos](https://github.com/edendenis/google_chrome/issues) para obter uma lista completa dos recursos propostos (e problemas conhecidos).

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


<!-- CONTRIBUIÇÔES -->
## Contribuições

As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

Se você tiver uma sugestão que possa melhorar isso, bifurque o repositório e crie uma solicitação `pull`. Você também pode simplesmente abrir um problema com a _tag_ “aprimoramento”.

Não se esqueça de dar uma estrela ao projeto! Obrigado novamente!

1. Bifurque o projeto

2. Crie sua ramificação de recursos (`git checkout -b feature/AmazingFeature`)

3. Confirme suas alterações (`git commit -m 'Add some AmazingFeature'`)

4. Envie para a filial (`git push origin feature/AmazingFeature`)

5. Abra uma solicitação `pull`

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Agradecimentos

* [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file)

* [Choose an Open Source License](https://choosealicense.com)

* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)

* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)

* [Malven's Grid Cheatsheet](https://grid.malven.co/)

* [Img Shields](https://shields.io)

* [GitHub Pages](https://pages.github.com)

* [Font Awesome](https://fontawesome.com)

* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>


## Referências

[1] OPENAI. ***Instalação do github cli.*** Disponível em: <https://chatgpt.com/c/67042c07-816c-8002-8913-7c8cdbc167a9> (texto adaptado). ChatGPT. Acessado em: 07/10/2024 15:49.

[2] OPENAI. ***Vs code: editor popular:*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 07/10/2024 15:49.


