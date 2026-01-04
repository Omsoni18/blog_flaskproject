from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Post, Comment
from sqlalchemy import desc

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Home page - display all posts"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(desc(Post.created_at)).paginate(page=page, per_page=10)
    return render_template('index.html', posts=posts)


@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def view_post(post_id):
    """View a single blog post with comments"""
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        content = request.form.get('content')
        
        if not all([name, email, content]):
            flash('Please fill in all fields', 'error')
            return redirect(url_for('main.view_post', post_id=post_id))
        
        comment = Comment(name=name, email=email, content=content, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added successfully!', 'success')
        return redirect(url_for('main.view_post', post_id=post_id))
    
    comments = Comment.query.filter_by(post_id=post_id).order_by(desc(Comment.created_at)).all()
    return render_template('post.html', post=post, comments=comments)


@main.route('/create', methods=['GET', 'POST'])
def create_post():
    """Create a new blog post"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author', 'Anonymous')
        
        if not title or not content:
            flash('Title and content are required', 'error')
            return redirect(url_for('main.create_post'))
        
        post = Post(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))
    
    return render_template('create_post.html')


@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    """Edit a blog post"""
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        post.author = request.form.get('author', 'Anonymous')
        
        if not post.title or not post.content:
            flash('Title and content are required', 'error')
            return redirect(url_for('main.edit_post', post_id=post_id))
        
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))
    
    return render_template('edit_post.html', post=post)


@main.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    """Delete a blog post"""
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.index'))


@main.route('/about')
def about():
    """About page"""
    return render_template('about.html')
