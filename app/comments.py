import api_key
import pandas as pd
from praw.models import MoreComments

url = "https://www.reddit.com/r/SeattleWA/comments/xa3qnl/what_is_your_favourite_restaurant_in_seattle/"
submission = api_key.reddit_read_only.submission(url=url)

post_comments = []
submission.comments.replace_more()

for comment in submission.comments:
    post_comments.append([comment.body, comment.score])

print(len(post_comments))
# creating a dataframe
comments_df = pd.DataFrame(post_comments, columns=['comment', 'score'])

f = open("../outputs/comments.csv", "w")
for comment, score in comments_df.values:
    comment_encode = comment.encode("gbk", "ignore")
    comment_decode = comment_encode.decode("gbk")
    f.write(f"{comment_decode.replace(',', '.')}, {score}\n")
f.close()

