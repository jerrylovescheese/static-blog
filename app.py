from flask import Flask, render_template, abort
import os

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

# Base route for the homepage


@app.route('/')
def index():
    post_files = os.listdir('posts/')
    posts = [post.replace('.html', '')
             for post in post_files if post.endswith('.html')]
    print(f"Posts: {posts}")  # Debugging line
    return render_template('index.html', posts=posts)

# Route for individual posts


@app.route('/posts/<post_name>.html')
def post(post_name):
    post_path = f'posts/{post_name}.html'
    try:
        with open(post_path, 'r') as file:
            content = file.read()
        return render_template('post.html', title=post_name.capitalize(), content=content)
    except FileNotFoundError:
        abort(404)


from flask_frozen import Freezer
freezer = Freezer(app)


if __name__ == '__main__':
    freezer.freeze()
