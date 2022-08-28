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
