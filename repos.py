import requests

# Make and API call and store the reponse.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
reponse_dict = r.json()
print(f"Total repositories: {reponse_dict['total_count']}")

# Explore information about the repositories.
repo_dict = reponse_dict['items']
print(f"Repositories returned: {len(repo_dict)}")

# Examine the first repository.
repo_dict = repo_dict[0]

print(f"\n selected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Update: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

print(f"\nkeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)