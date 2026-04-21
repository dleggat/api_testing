import requests

def get_repo_issues(repo: str, state="all"):
    ### Get all issues from repo in given state
    
    # REST API endpoint for issues in a repo.
    # repo has form owner/repo
    url = f"https://api.github.com/repos/{repo}/issues"
    
    # Accessing GitHub requires authorisation
    kwargs = get_auth_headers()

    # Filter based on chosen state
    kwargs["params"] = {"state": state}

    return requests.get(url, **kwargs)
    


def get_github_token(secrets_file):
    ### Get github token from secrets file
    github_token = ""
    import yaml
    from pathlib import Path
    with Path(secrets_file).open() as f:
        file_contents = yaml.safe_load(f)
        if "github_token" in file_contents.keys():
            return file_contents["github_token"]


def get_auth_headers():
    ### Get the authorisation headers required for GitHub access

    headers = {"Authorization": f"Bearer {get_github_token('secrets.yml')}"}
    return {"headers": headers}
