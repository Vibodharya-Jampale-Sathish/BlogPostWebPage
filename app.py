from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import get_connection  # Your DB connection function

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random value in production

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash("Please enter both username and password.")
            return render_template('login.html')

        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT id, password FROM users WHERE user_name = %s", (username,))
            user = cur.fetchone()
            if user and user[1] == password:
                session['user_id'] = user[0]
                flash("Logged in successfully!")
                return redirect(url_for('create_blog'))
            else:
                flash("Invalid username or password.")
        except Exception as e:
            flash(f"Login error: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash("Please enter both username and password.")
            return render_template('register.html')

        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT id FROM users WHERE user_name = %s", (username,))
            if cur.fetchone():
                flash("Username already exists. Choose another.")
                return render_template('register.html')

            cur.execute("INSERT INTO users (user_name, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Registration error: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    return render_template('register.html')


@app.route('/blog', methods=['GET', 'POST'])
def create_blog():
    if 'user_id' not in session:
        flash("Please log in first.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        blog_name = request.form.get('blog_name', '').strip()
        blog_content = request.form.get('blog_content', '').strip()

        if not blog_name or not blog_content:
            flash("Both blog title and content are required.")
            return render_template('blog.html')

        conn = None
        cur = None
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO blogs (user_id, blog_name, blog_content) VALUES (%s, %s, %s)",
                (session['user_id'], blog_name, blog_content)
            )
            conn.commit()
            flash("Blog post created successfully!")
            return redirect(url_for('create_blog'))
        except Exception as e:
            flash(f"Error creating blog post: {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    return render_template('blog.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)