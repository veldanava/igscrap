# scraping ig with python
import instaloader
# instance
bot = instaloader.Instaloader()
# Load a profile
profile = instaloader.Profile.from_username(bot.context, input("input username: "))
# Get all posts in a generator object
# posts = profile.get_posts()
# for index, post in enumerate(posts, 1):
#     bot.download_post(post, target=f"{profile.username}_{index}")
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Following: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)