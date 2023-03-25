# Cofre

Os segredos da APyB são encriptados usando o gerenciador de senhas KeePassXC. Ele está disponível em múltiplas plataformas, como Linux ou MacOS, tem plugins de auto completar para os navegadores e aplicativos para celular.

```{attention}
É **Importante** que você se familiarizar com as funcionalidades, interface, etc. O [guia para iniciantes](https://keepassxc.org/docs/KeePassXC_GettingStarted.html) do KeePassXC (disponível apenas em inglês) é um ótimo começo.
```

## Abrindo o cofre

1. Faça download e instale o [KeePassXC](https://keepassxc.org/download).
1. Clone o repositório [apyb/cofre](https://github.com/apyb/cofre). Como este é um repositório privado, apenas a direção da APyB tem acesso.
    ```
    $ git clone git@github.com:apyb/cofre
    ```
1. Em posse da senha mestre, você poderá abrir o arquivo `apyb-cofre.kdbx` usando o KeePassXC e ter acesso a todos os dados mantidos por lá.


## Sincronizando os segredos

Para manter o repositório sincronizado, podemos usar normalmente os comandos `git pull` e `git commit + push`. Porém, para facilitar, criamos os comandos `apyb-pull` e `apyb-push`. Esses dois comandos simplificam o passo a passo necessário quando usamos diretamente o git.

Você pode conferir e copiar o código fonte dos comandos [aqui](https://apyb.python.org.br/apyb-cofre.sh), ou então executar os três passos abaixo para torná-los disponíveis no seu computador. Caso você use Zsh ou outro *shell*, mude o arquivo `.bashrc` usado no exemplo de acordo com o seu caso.

1. Adicione a variável de ambiente `APYB_COFRE_PATH` apontando para o caminho do repositório:
    ```
    $ echo 'export APYB_COFRE_PATH="$HOME/caminho/do/repo"' >> ~/.bashrc
    ```
1. Faça download do arquivo `apyb-cofre.sh` em seu computador:
    ```
    $ curl https://apyb.python.org.br/apyb-cofre.sh -o ~/.apyb-cofre.sh
    ```
1. Torne as funções disponíveis executando o comando `source` no arquivo baixado:
    ```
    $ echo 'source ~/.apyb-cofre.sh' >> ~/.bashrc
    ```

Pronto, com esses passos feitos, você poderá usar os comandos `apyb-pull` e `apyb-push`. Aqui vai uma breve explicação de como os comandos funcionam.

1. Quando desejar atualizar o repositório local com as últimas alterações, base executar a função `apyb-pull`. Essa função atualizará o repositório local com as alterações remotas e garantirá que não haja arquivos não commitados no repositório local antes de prosseguir com a atualização.
1. Quando desejar enviar suas próprias alterações para o repositório remoto, basta executar a função `apyb-push`, passando uma string como parâmetro que descreve as alterações que foram feitas. Essa função verificará se há alterações não commitadas no repositório local e, se não houver, exibirá um erro e não prosseguirá. Caso haja alterações, a função fará um commit usando a string passada como descrição e enviará as alterações para o repositório remoto.

Dessa forma, todas as alterações feitas pelos quatro usuários serão mantidas sincronizadas, e o uso das funções `apyb-pull` e `apyb-push` garante que não haverá conflitos devido a alterações não sincronizadas.
