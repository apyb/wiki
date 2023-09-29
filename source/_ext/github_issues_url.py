from urllib.parse import urljoin
from urllib.parse import urlencode


def get_page_url(app, docname):
    site_base_url = app.config.html_baseurl
    document_uri = app.builder.get_relative_uri(app.builder.config.master_doc, docname)
    return urljoin(site_base_url, document_uri)


def get_page_source_url(context, filepath):
    return "{source_url}/blob/{branch}/{dir}/{filepath}".format(
        source_url=context["source_url"],
        branch=context["source_branch"],
        dir=context["source_dir"],
        filepath=filepath,

    )


def setup_github_issues_url(app, pagename, templatename, context, doctree):
    def github_issues_url(root_doc, pagename, page_source_suffix):
        if not root_doc or not page_source_suffix:
            return ""

        document_path = pagename + page_source_suffix

        page_url = get_page_url(app, pagename)
        page_source_url = get_page_source_url(context, document_path)


        source_url = context["source_url"]
        source_url = context["source_url"]

        new_issue_context = {
            "document_path": document_path,
            "page_url": page_url,
            "page_source_url": page_source_url,
        }

        new_issue_title = context["new_issue_title"].format_map(new_issue_context)
        new_issue_body = context["new_issue_body"].format_map(new_issue_context)
        url_params = urlencode({
            "title": new_issue_title,
            "body": new_issue_body,
        })

        return f"{source_url}/issues/new?{url_params}"

    context["github_issues_url"] = github_issues_url



def setup(app):
    app.connect("html-page-context", setup_github_issues_url)
