import scratchattach as attach
import time


print("Creating session")
session = attach.login("YORU USERNAME", "YORU PASSWORD")
print("Connecting studio")
studio = session.connect_studio("50683717") # This can be any studio but this is a good one.
off = 11500
index = 10
while True:
    print(f"Fetching projects with offset of {off}")
    projects = studio.projects(limit=5, offset=off)
    for project_info in projects:
        index += 1
        project_info_dict = vars(project_info)
        project = session.connect_project(project_info_dict['id'])
        project.author().follow()
        print(f"{index}: Followed author {project.author()} from project {project.title}")
        time.sleep(20)
    off += 20
    time.sleep(25)
