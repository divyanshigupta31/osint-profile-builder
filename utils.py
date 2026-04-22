import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}
def get_repositories(username):
    url = f"https://github.com/{username}?tab=repositories"
    
    try:
        r = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        
        repo_list = []
        
        repos = soup.find_all("a", itemprop="name codeRepository")
        
        for repo in repos:
            repo_list.append(repo.text.strip())
        
        return repo_list[:5]
    
    except:
        return []

def check_github(username):
    url = f"https://github.com/{username}"
    
    try:
        r = requests.get(url, headers=headers, timeout=5)
        
        if r.status_code != 200:
            return None
        
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Name
        name_tag = soup.find("span", class_="p-name")
        name = name_tag.text.strip() if name_tag else "N/A"
        
        # Bio
        bio_tag = soup.find("div", class_="p-note")
        bio = bio_tag.text.strip() if bio_tag else "N/A"
        
        # Followers
        followers_tag = soup.find("a", href=f"/{username}?tab=followers")
        followers = followers_tag.text.strip() if followers_tag else "N/A"
        
        # Following
        following_tag = soup.find("a", href=f"/{username}?tab=following")
        following = following_tag.text.strip() if following_tag else "N/A"
        
        # Repositories
        repos_tag = soup.find("a", href=f"/{username}?tab=repositories")
        repos = repos_tag.text.strip() if repos_tag else "N/A"
        
        repos_list = get_repositories(username)
        return {
            "platform": "GitHub",
            "name": name,
            "bio": bio,
            "followers": followers,
            "following": following,
            "repos": repos,
            "url": url,
            "repositories": repos_list
        }
    
    except:
        return None