from utils import check_github

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
    else:
        print("GitHub profile not found")

if __name__ == "__main__":
    username = input("Enter username: ")
    build_profile(username)