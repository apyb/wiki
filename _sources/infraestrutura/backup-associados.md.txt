# Backup site associados

O repositório [apyb/associados](https://github.com/apyb/associados) contém o código fonte do site legado de associados da APyB. Ele é um site Django que rodava no Heroku, mas foi descontinuado em 2025 e hoje todo o gerenciamento de associados é realizado via [Stripe](../associados/associe-se.rst).

Caso seja necessário acessar o banco de dados do site legado, o backup mais recente está disponível no [cofre](./cofre.md). E você pode restaurá-lo localmente seguindo os passos abaixo:

> **Resumo rápido (TL;DR)**
>
> 1. Instale o PostgreSQL (inclui `psql` e `pg_restore`).
>
> 2. Crie um banco vazio: `createdb associadosdb`.
>
> 3. Rode: `pg_restore --verbose --clean --no-acl --no-owner -h localhost -d associadosdb backup_banco_associados.dump`.
>
> 4. Valide com `psql -d associadosdb -c "\dt"`.

---

### 1) Pré‑requisitos

* **PostgreSQL** instalado localmente (versão igual ou mais nova que a do backup para evitar incompatibilidades -  Versão 17.4).

  * macOS: `brew install postgresql` (ou `postgresql@<versão>`)
  * Ubuntu/Debian: `sudo apt-get install postgresql postgresql-client`
  * Windows: instalar via [PostgreSQL Installer](https://www.postgresql.org/download/windows/)
* A ferramenta **`pg_restore`** (vem junto com a instalação do PostgreSQL).
* O arquivo `backup_banco_associados.dump` baixado do Heroku.
* Acesso ao usuário local do Postgres (ex.: `postgres`) e sua senha, caso configurada.

> **Dica:** Para conferir sua versão local: `psql --version` e `pg_restore --version`.

---

### 2) Confirmar integridade (opcional, mas recomendado)

No mesmo diretório do arquivo de dump (`backup_banco_associados.dump`):

```bash
# macOS/Linux
shasum -a 256 backup_banco_associados.dump

# Windows (PowerShell)
Get-FileHash .\backup_banco_associados.dump -Algorithm SHA256
```

Guarde o hash junto com o arquivo para auditoria.

---

### 3) Criar o banco de destino

Crie um banco **vazio** onde o dump será restaurado.

```bash
# macOS/Linux
createdb -h localhost -U postgres associadosdb

# Windows (PowerShell / CMD)
createdb -h localhost -U postgres associadosdb
```

Se preferir criar via `psql`:

```bash
psql -h localhost -U postgres -c "CREATE DATABASE associadosdb;"
```

> Se o usuário pedir senha, informe a senha do usuário do Postgres local (ex.: `postgres`).

---

### 4) Restaurar com `pg_restore` (formato custom)

O dump do Heroku normalmente é em **formato custom** (`-Fc`), ideal para `pg_restore`.

Comando recomendado (idempotente, sem restaurar ACLs/donos):

```bash
pg_restore \
  --verbose \
  --clean \
  --no-acl \
  --no-owner \
  -h localhost \
  -d associadosdb \
  backup_banco_associados.dump
```

**O que cada flag faz:**

* `--verbose`: imprime detalhes do progresso
* `--clean`: executa `DROP` antes de `CREATE` (útil para reimportar no mesmo DB)
* `--no-acl`: ignora permissões do dump
* `--no-owner`: não tenta recriar donos/roles do Heroku

> **Se precisar de schema específico**: normalmente o Heroku usa `public`. Se o seu dump tiver outro schema, você pode restringir com `-n <schema>`.

> **Se quiser restaurar só uma tabela**: liste o conteúdo (`pg_restore -l backup_banco_associados.dump > toc.list`), edite a lista e use `pg_restore -L toc.list ...`.

---
