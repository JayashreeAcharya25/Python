import instaloader

mod = instaloader.Instaloader()

a = input("Enter the username:")

mod.download_profile(a,profile_pic_only=True)