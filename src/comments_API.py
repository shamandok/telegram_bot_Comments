from PyCommentAPI import Comments

def __get_postbot(token):
    return Comments(token=token)

def create_post(text, owner_id, token):
    postbot = __get_postbot(token)
    post = postbot.create_post(owner_id=owner_id, type='text', text=text, parse_mode='HTML')
    return post.link