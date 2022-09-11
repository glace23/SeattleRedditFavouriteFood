import api_key
import pandas as pd
from praw.models import MoreComments

url = "https://www.reddit.com/r/SeattleWA/comments/xa3qnl/what_is_your_favourite_restaurant_in_seattle/"
submission = api_key.reddit_read_only.submission(url=url)
print(submission.title)

comments = submission.comments.list()
post_comments = []

for comment in comments:
    if type(comment) == MoreComments:
        continue

    post_comments.append([comment.body, comment.score])

# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment', 'score'])

f = open("comments.txt", "w")
for comment, score in comments_df.values:
    print(comment)
    comment_encode = comment.encode("ascii", "ignore")
    comment_decode = comment_encode.decode()
    f.write(f"{comment_decode}\n")
    #f.write(f"{comment}\n")
f.close()

