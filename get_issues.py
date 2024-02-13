
from promptflow import tool
import requests

def get_github_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.get(url)
    if response.status_code == 200:
        issues = response.json()
        return issues
    else:
        print(f"Failed to retrieve issues: {response.status_code}")
        return None

# Replace 'owner' and 'repo' with the desired owner and repository name
owner = "microsoft"
repo = "promptflow"

issues = get_github_issues(owner, repo)

if issues:
    issues_dict = {}
    for issue in issues:
        issue_number = issue['number']
        issue_title = issue['title']
        issues_dict[issue_number] = issue_title

    print(issues_dict)
else:
    print("No issues found.")


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: dict) -> str:
    return 'hello ' + input1
