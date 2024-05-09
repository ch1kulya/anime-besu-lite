from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Функция для получения соединения с базой данных
def get_db_connection():
    conn = sqlite3.connect('anime_movies.db')
    conn.row_factory = sqlite3.Row
    return conn

# Функция для получения топ-15 самых просматриваемых фильмов
def get_top_movies():
    conn = get_db_connection()
    top_movies = conn.execute('SELECT * FROM movies ORDER BY views DESC LIMIT 15').fetchall()
    conn.close()
    return top_movies

@app.route('/')
def index():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies ORDER BY views DESC').fetchall()
    conn.close()
    return render_template('index.html', title='Anime Besu', meta_description='Watch anime movies online for free.', movies=movies)

@app.route('/watch/<int:movie_id>')
def watch(movie_id):
    conn = get_db_connection()
    conn.execute('UPDATE movies SET views = views + 1 WHERE id = ?', (movie_id,))
    conn.commit()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    conn.close()
    if movie is not None:
        return render_template('watch.html', title=f'{movie["title"]} | Anime Besu', meta_description=f'Watch {movie["title"]} anime movie online for free.', movie=movie)
    else:
        return redirect(url_for('index'))

@app.route('/movie_form', methods=['GET', 'POST'])
@app.route('/movie_form/<int:movie_id>', methods=['GET', 'POST'])
def movie_form(movie_id=None):
    top_movies = get_top_movies()  # Получаем топ-15 фильмов
    
    conn = get_db_connection()
    movie = None
    if movie_id:
        # Получаем фильм по ID для редактирования
        movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    
    if request.method == 'POST':
        title = request.form['title']
        banner = request.form['banner']
        video_url = request.form['video_url']
        poster = request.form['poster']
        description = request.form['description']  # Получаем описание из формы

        if movie:
            # Обновляем существующий фильм
            conn.execute('UPDATE movies SET title = ?, banner = ?, video_url = ?, poster = ?, description = ? WHERE id = ?',
                         (title, banner, video_url, poster, description, movie_id))
        else:
            # Добавляем новый фильм
            conn.execute('INSERT INTO movies (title, banner, video_url, poster, description) VALUES (?, ?, ?, ?, ?)',
                         (title, banner, video_url, poster, description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    conn.close()
    return render_template('movie_form.html', title='Anime Besu Form', meta_description='Anime Besu Form.', movie=movie, top_movies=top_movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
