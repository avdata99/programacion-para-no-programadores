import requests

# JSON con los datos de un usuario de GitHub
url = 'https://api.github.com/users/avdata99'
response = requests.get(url)
data = response.json()
print(f'Datos: {data}')

# De que tipo es data?
print(type(data))

"""
Ejemplo

{
    "login": "avdata99",
    "id": 3237309,
    "node_id": "MDQ6VXNlcjMyMzczMDk=",
    "avatar_url": "https://avatars.githubusercontent.com/u/3237309?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/avdata99",
    "html_url": "https://github.com/avdata99",
    "followers_url": "https://api.github.com/users/avdata99/followers",
    "following_url": "https://api.github.com/users/avdata99/following{/other_user}",
    "gists_url": "https://api.github.com/users/avdata99/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/avdata99/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/avdata99/subscriptions",
    "organizations_url": "https://api.github.com/users/avdata99/orgs",
    "repos_url": "https://api.github.com/users/avdata99/repos",
    "events_url": "https://api.github.com/users/avdata99/events{/privacy}",
    "received_events_url": "https://api.github.com/users/avdata99/received_events",
    "type": "User",
    "site_admin": false,
    "name": "Andres Vazquez",
    "company": "OKFN",
    "blog": "http://andresvazquez.com.ar",
    "location": "Mendiolaza, Cordoba, Argentina",
    "email": null,
    "hireable": null,
    "bio": null,
    "twitter_username": "avdata99",
    "public_repos": 153,
    "public_gists": 19,
    "followers": 82,
    "following": 18,
    "created_at": "2013-01-10T17:45:49Z",
    "updated_at": "2022-08-28T17:01:16Z"
}
"""