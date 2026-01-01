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

**É muito importante manter o repositório do cofre sempre sincronizado**. Isso evitará conflitos no git que só poderão ser resolvidos manualmente, já que o `apyb-cofre.kdbx` é um arquivo binário. As recomendações são:

1. Sempre que for acessar uma senha no cofre, execute `git pull`.
1. Sempre que for adicionar uma senha no cofre, antes de abrir o Keepass, execute `git pull`.
1. Após adicionar um novo item no cofre, crie um novo *commit* e atualize o repositório com `git push`.
1. Por fim, notifique os diretores da atualização.

## Python Brasil

No caso da Python Brasil, para auxiliar o gerenciamneto de senha utilizamos o [1password](https://1password.com/). Apenas a APyB e a comissão organizadora da Python Brasil têm acesso a esse cofre. Para saber mais como que funciona o nosso plano no 1password, consulte o repositório [1Password for Open Source](https://github.com/1Password/for-open-source).

```{important}
A senha de acesso ao 1password é diferente da senha de acesso ao KeePassXC, e para saber mais detalhes sobre como acessar o cofre da Python Brasil, pesquise por `1password` no cofre da APyB. 
```
