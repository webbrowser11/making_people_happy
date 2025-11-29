import scratchattach as sa

session = sa.login("YOUR USERNAME","YOUR PASSWORD")
user = session.connect_user("YOUR USERNAME")
user.post_comment("Hey, I uh rebooted the system, your stuff should still be there but... yeah!")
