# Blog Website - Flask Application

A modern, fully-featured blog website built with Flask, SQLAlchemy, and modern web technologies.

## Features

- 📝 **Create, Read, Update, Delete Posts** - Full CRUD operations for blog posts
- 💬 **Comments System** - Readers can leave comments on posts
- 🎨 **Modern UI** - Beautiful, responsive design with gradient backgrounds
- 📄 **Pagination** - Browse posts with page navigation
- 🔍 **About Page** - Learn more about the blog
- 📱 **Mobile Responsive** - Works perfectly on all devices
- ⚡ **Fast Performance** - Built with SQLAlchemy ORM
- 🗄️ **Database** - SQLite for easy setup and portability

## Project Structure

```
blog_flaskproject/
├── app/
│   ├── __init__.py          # App factory and initialization
│   ├── models.py            # Database models (Post, Comment)
│   ├── routes.py            # Blueprint with all routes
│   ├── templates/           # HTML templates
│   │   ├── base.html        # Base template with styling
│   │   ├── index.html       # Homepage - list all posts
│   │   ├── post.html        # View single post with comments
│   │   ├── create_post.html # Create new post form
│   │   ├── edit_post.html   # Edit post form
│   │   └── about.html       # About page
│   └── static/              # Static files (CSS, JS, images)
├── run.py                   # Application entry point
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── blog.db                  # SQLite database (created on first run)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd blog_flaskproject
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Usage

### Creating a Post
1. Click the **"New Post"** button in the navigation
2. Enter the post title, author name (optional), and content
3. Click **"Create Post"**

### Reading Posts
- Visit the homepage to see all posts
- Click on any post title to read the full content
- View and add comments on individual posts

### Editing a Post
1. Open the post you want to edit
2. Click the **"✏️ Edit Post"** button
3. Make your changes and click **"Save Changes"**

### Deleting a Post
1. Open the post you want to delete
2. Click the **"🗑️ Delete Post"** button
3. Confirm the deletion

### Adding Comments
1. Scroll down to the comments section on any post
2. Fill in your name, email, and comment
3. Click **"Post Comment"**

## Configuration

Edit `config.py` to customize:
- `SECRET_KEY` - Change to a strong random string in production
- `SQLALCHEMY_DATABASE_URI` - Modify database connection string
- Database tracking and debug settings

## Environment Variables

Edit `.env` file to set:
- `FLASK_ENV` - Set to 'development', 'testing', or 'production'
- `SECRET_KEY` - Your secret key
- `DATABASE_URL` - Database connection string (defaults to SQLite)

## Database Commands

### Using Flask Shell
```bash
# Activate the application shell
python -c "from run import app; app.app_context().push()" -i

# Create tables
>>> from app import db
>>> db.create_all()

# Query posts
>>> from app.models import Post
>>> posts = Post.query.all()

# Create a post
>>> post = Post(title='Hello', content='World', author='Me')
>>> db.session.add(post)
>>> db.session.commit()
```

## Technology Stack

- **Backend**: Flask 3.1.2
- **Database**: SQLAlchemy 2.0.45 + SQLite
- **Templating**: Jinja2 3.1.6
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Migrations**: Flask-Migrate 4.1.0
- **Frontend**: HTML5, CSS3 with Gradient Design

## Security Notes

⚠️ **Important for Production:**
1. Change the `SECRET_KEY` in `config.py` to a strong random string
2. Set `DEBUG = False` in production
3. Use environment variables for sensitive data
4. Consider using PostgreSQL instead of SQLite
5. Implement user authentication for post management
6. Add CSRF protection for forms
7. Sanitize user input to prevent XSS attacks

## Future Enhancements

- User authentication and authorization
- Post categories and tags
- Search functionality
- Comment moderation
- Social media sharing
- Email notifications
- Markdown support for posts
- Post scheduling

## Troubleshooting

### Database issues
If you encounter database errors, delete `blog.db` and restart the application.

### Port already in use
Change the port in `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to another port
```

### Template not found
Ensure all template files are in `app/templates/` with correct filenames.

## License

This project is free to use and modify for personal and commercial purposes.

## Support

For issues or questions, please check the code comments or create an issue in the project repository.

---

**Happy Blogging!** 📝✨
