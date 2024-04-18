function apyb-pull() {
    local repo=${APYB_COFRE_PATH:? Erro: o caminho do repositório não foi definido na variável de ambiente APYB_COFRE_PATH}
    [[ -d "$repo" ]] || {
        echo "Erro: o caminho do repositório não existe.";
        return 1;
    }

    [[ -z $(git --git-dir=$repo/.git --work-tree=$repo status --porcelain) ]] || {
        echo "Erro: há arquivos não commitados no repositório local.";
        return 1;
    }

    git --git-dir=$repo/.git --work-tree=$repo pull
}

function apyb-push() {
    local repo=${APYB_COFRE_PATH:? Erro: o caminho do repositório não foi definido na variável de ambiente APYB_COFRE_PATH}
    [[ -d "$repo" ]] || {
        echo "Erro: o caminho do repositório não existe.";
        return 1;
    }

    [[ -n $(git --git-dir=$repo/.git --work-tree=$repo status --porcelain) ]] || {
        echo "Não há mudanças no repositório local para serem enviadas";
        return 0;
    }
    [[ -n "$1" ]] || {
        echo "Erro: nenhum parâmetro informado.";
        return 1;
    }

    git --git-dir=$repo/.git --work-tree=$repo commit -m "$1" && \
    git --git-dir=$repo/.git --work-tree=$repo push upstream || {
        echo "Erro: falha ao realizar o commit e/ou enviar as mudanças para o upstream.";
        return 1;
    }
}
