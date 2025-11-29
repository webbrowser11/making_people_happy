import scratchattach as sa
import time
import html  # <<— decode HTML entities

# Login to Scratch
session = sa.login("YOUR USERNAME", "YOUR PASSWORD")
project = session.connect_project("YOUR PROJECT")

keyword = "/comment"
processed_comments = set()  # To track already processed comments


def has_similar_reply(comment, user):
    replies = comment.replies()
    
    original = html.unescape(comment.content).strip()

    for reply in replies:
        reply_text = html.unescape(reply.content).strip()
        if reply.author == user and reply_text == original:
            return True
    
    return False


def fetch_and_process_comments():
    global processed_comments

    comments = project.comments()
    
    for comment in comments:
        comment_id = comment.id
        raw_content = comment.content
        content = html.unescape(raw_content)  # <<— decode it here

        if comment_id in processed_comments:
            continue

        if has_similar_reply(comment, "sped_ai"):
            print(f"Skipped comment ID {comment_id}: Already has a similar reply.")
            processed_comments.add(comment_id)
            continue

        if keyword in content:
            modified_content = content.replace(keyword, "").strip()

            # Make sure the reply itself is not re-escaped
            safe_reply = html.unescape(modified_content)

            project.reply_comment(safe_reply, parent_id=comment_id)
            print(f"Replied to comment ID {comment_id}: {safe_reply}")

        processed_comments.add(comment_id)


while True:
    try:
        fetch_and_process_comments()
    except Exception as e:
        print(f"Error occurred: {e}")

    time.sleep(20)
