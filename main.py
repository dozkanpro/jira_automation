import requests
import openpyxl
import os

jira_url = "https://dozkanpyt.atlassian.net/"
api_username = os.environ.get('api_username')
api_password = os.environ.get('api_password')

excel_file_path = "bugs.xlsx"


workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

all_issue_data = []


for row in sheet.iter_rows(min_row=2, values_only=True):
    summary = row[0]
    description = row[1]
    project_key = row[2]
    issue_type = row[3]

    # Define the issue details for this row
    issue_data = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
        }
    }

    all_issue_data.append(issue_data)

for issue_data in all_issue_data:
    response = requests.post(
        f"{jira_url}/rest/api/2/issue",
        auth=(api_username, api_password),
        headers={"Content-Type": "application/json"},
        json=issue_data,
    )

    if response.status_code == 201:
        issue = response.json()
        issue_key = issue["key"]
        print(f"Issue created: {issue_key}")
        url = jira_url + "/browse/" + issue_key
        print(f"Issue Link: {url}")
    else:
        print("Error creating issue")
