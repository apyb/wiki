# wiki

## Atualizando a wiki

A wiki usa como base o *framework* de documentação Sphinx. Para instalar o Sphinx, e as outras dependências do projeto, você precisará ter o Poetry em sua máquina.

[Veja aqui](https://python-poetry.org/docs/#installation) as instruções recomendadas para instalar o Poetry de acordo com o seu sistema operacional.


**Instalando as dependências com Poetry**

```
$ poetry install
```

**Executando a wiki localmente**
```
$ poetry run make live
```

Usando o comando `live`, Sphinx rodará um servidor local, na porta 8000, em que você poderá ver o resultado as mudanças que fizer. Além disso, qualquer alteração nos arquivos, o servidor será atualizado automaticamente, sem necessidade de rodar o mesmo comando novamente.
