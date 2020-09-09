from json import load
from markdown2 import markdown_path
from flask import Flask, render_template
from data import Data

app = Flask(__name__)


@app.route('/')
def index():
    data = Data()
    all_posts = data.all_posts
    return render_template('index.html', posts=all_posts)


@app.route('/blog/<post_name>')
def post(post_name):
    data = {}

    with open('posts/'+str(post_name)+'/'+str(post_name)+'.json') as conf:
        data = load(conf)

    post_content = markdown_path(
        "posts/" + str(post_name) + "/" + str(post_name) + ".md", extras=['code-friendly', 'fenced-code-blocks'])

    return render_template('post.html', content=post_content,
                           title=data['title'],
                           author=data['author'],
                           date=data['date'])


if __name__ == '__main__':
    app.run(debug=True)
