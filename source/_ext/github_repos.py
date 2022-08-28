import json
from pathlib import Path

import httpx
from sphinx.util import logging

logger = logging.getLogger(__name__)


class Cache:
    path = Path.cwd() / "build" / "repositories.json"

    @staticmethod
    def read():
        if not Cache.path.exists():
            return None

        with open(Cache.path) as file:
            return json.load(file)

    @staticmethod
    def store(content):
        with open(Cache.path, "w") as file:
            json.dump(content, file)


def list_repositories_from_github(org):
    url = f"https://api.github.com/orgs/{org}/repos"
    response = httpx.get(url, params={"per_page": 100})
    response.raise_for_status()
    return response.json()


def github_repos(app, config):
    repos = Cache.read()
    if not repos:
        logger.info("Loading repositories from Github API")
        apyb = list_repositories_from_github("apyb")
        pythonbrasil = list_repositories_from_github("pythonbrasil")

        repos = apyb + pythonbrasil
        repos = sorted(repos, key=lambda repo: repo["full_name"])
        Cache.store(repos)

    context = getattr(config, "templates_context", {})
    context["github_repositories"] = repos

    config.templates_context = context


def setup(app):
    app.connect("config-inited", github_repos)
