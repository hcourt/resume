from flask import render_template, send_file
from resume import app
from resume.app import pages

@app.route('/')
def home():
    """Home page.

    """
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@app.route('/download')
def download():
    """Download pdf copy of resume.

    """
    return send_file('static/hcourt_resume_winter_2014.pdf')

@app.route('/<path:path>')
def page(path):
    """Return the document specified by path

    `path` is the filename of a page, without the file extension
    e.g. "first-post"
    """
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
