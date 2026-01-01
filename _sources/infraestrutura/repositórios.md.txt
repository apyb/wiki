!template

# Repositórios

Lista de repositórios ativos nas organizações **[/apyb](https://github.com/apyb)** e **[/pythonbrasil](https://github.com/pythonbrasil)**.

Gerado automaticamente durante o processo de *deploy* desse site.

Atualizado em: `{{ now }}`

## APyB

{% macro issue_label(repo) -%}
[![GitHub issues](https://img.shields.io/github/issues-raw/{{ repo }}?color=%230074D9&label=issues)](https://github.com/{{ repo }}/issues)
{%- endmacro %}

{% macro pr_label(repo) -%}
[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/{{ repo }}?color=%23FFDC00&label=pull%20requests)](https://github.com/{{ repo }}/pulls)
{%- endmacro %}

{% macro repo_row(repo) -%}
| [{{ repo.name }}]({{ repo.html_url }}) | {{ repo.description }} | {{ issue_label(repo.full_name) }} |  {{ pr_label(repo.full_name) }} |
{%- endmacro %}

| Repositório | Descrição | Issues | Pull Requests |
| ----------- | --------- | ------ | ------------- |
{% for repo in github_repositories|selectattr("owner.login", "equalto", "apyb")|rejectattr("archived") -%}
{{ repo_row(repo) }}
{% endfor -%}

## Python Brasil

| Repositório | Descrição | Issues | Pull Requests |
| ----------- | --------- | ------ | ------------- |
{% for repo in github_repositories|selectattr("owner.login", "equalto", "pythonbrasil")|rejectattr("archived") -%}
{{ repo_row(repo) }}
{% endfor %}

## Como é feito o controle de acesso aos repositórios?

O controle de acesso aos repositórios é feito via times do GitHub.

```{important}
Recomenda-se que as pessoas usuárias sejam adicionadas aos times corretos, ao invés de serem adicionadas diretamente aos repositórios. Além disso, é importante que você habilite as notificações do GitHub para receber atualizações nos repositórios que você tem acesso.
```

| Organização                                   | Time            | Repositórios com acesso                                                        |
|-----------------------------------------------|----------------------|--------------------------------------------------------------------------------|
| [apyb](https://github.com/apyb)               | [Conselho Deliberativo](https://github.com/orgs/apyb/teams/conselho-deliberativo) | [apyb/associados](https://github.com/apyb/associados), [apyb/estatuto](https://github.com/apyb/estatuto), [apyb/wiki](https://github.com/apyb/wiki)                                      |
|                                               | [Conselho Fiscal](https://github.com/orgs/apyb/teams/conselho-fiscal)       | [apyb/financeiro](https://github.com/apyb/financeiro)                                                                |
|                                               | [Diretoria](https://github.com/orgs/apyb/teams/diretoria)             | Todos os repositórios                                                          |
| [pythonbrasil](https://github.com/pythonbrasil) | [APyB](https://github.com/orgs/pythonbrasil/teams/apyb)                | [pythonbrasil/dados](https://github.com/pythonbrasil/dados), [pythonbrasil/manual](https://github.com/pythonbrasil/manual), [pythonbrasil/wiki](https://github.com/pythonbrasil/wiki)                     |
|                                               | [Conselho Deliberativo](https://github.com/orgs/pythonbrasil/teams/conselho-deliberativo) | [pythonbrasil/dados](https://github.com/pythonbrasil/dados), [pythonbrasil/manual](https://github.com/pythonbrasil/manual)                                        |
|                                               | [Conselho Fiscal](https://github.com/orgs/pythonbrasil/teams/conselho-fiscal)       | [pythonbrasil/manual](https://github.com/pythonbrasil/manual)                                                            |