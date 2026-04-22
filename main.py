from utils import check_github
import json 

def build_profile(username):
    print("\n===== OSINT PROFILE =====\n")
    print("-" * 30)
    
    github = check_github(username)
    
    if github:
        print("Platform: GitHub")
        print("Name:", github["name"])
        print("Bio:", github["bio"])
        print("Followers:", github["followers"])
        print("Following:", github["following"])
        print("Repositories:", github["repos"])
        print("Profile:", github["url"])
        print("Repositories:")
        for repo in github["repositories"]:
            print("-", repo)
        all_profiles = []

        for username in usernames:
            profile = check_github(username.strip())
            if profile:
                all_profiles.append(profile)

        with open("all_profiles.json", "w") as f:
            json.dump(all_profiles, f, indent=4)
    else:
        print("GitHub profile not found")

if __name__ == "__main__":
    usernames = input("Enter usernames (comma separated): ").split(",")
    for username in usernames:
        username = username.strip()
        build_profile(username)