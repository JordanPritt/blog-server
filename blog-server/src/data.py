from os import scandir
from json import load


class Data:

    def __init__(self):
        self.all_posts = []
        self.get_all_posts()

    def get_all_posts(self):
        for directory in scandir('posts/'):
            if directory.is_dir():
                for file in scandir(directory.path):
                    if file.path.endswith('.json'):
                        with open(file.path) as conf:
                            data = load(conf)
                            post_data = Post(data['title'],
                                             data['type'],
                                             data['date'],
                                             data['desc'],
                                             data['link'])
                            self.all_posts.append(post_data)


class Post:
    def __init__(self, title, post_type, date, desc, link):
        self.title = title
        self.post_type = post_type
        self.date = date
        self.desc = desc
        self.link = link
