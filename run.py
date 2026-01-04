import os
from app import create_app, db
from app.models import Post, Comment

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Register objects to the shell context"""
    return {'db': db, 'Post': Post, 'Comment': Comment}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
