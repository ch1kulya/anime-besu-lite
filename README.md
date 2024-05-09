# Anime Besu

Anime Besu is a simple Flask web application that allows users to watch anime movies online for free. Users can browse through a collection of anime movies, view details about each movie, and watch them directly through the application.

## Installation

To run the Anime Besu application locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed (preferably Python 3.x).
3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```
4. Run the Flask application:

   ```
   python app.py
   ```
5. Open your web browser and navigate to `http://localhost:80` to access the application.

## Features

- **Browse Movies**: Users can browse through a list of anime movies.
- **Watch Movies**: Users can watch anime movies online.
- **Add/Edit Movies**: Admin users can add new movies to the collection or edit existing ones.

## Usage

Upon launching the application, users are presented with a list of anime movies sorted by popularity. They can click on any movie to view its details and watch it online.

Admin users can access the movie form to add new movies or edit existing ones. The form includes fields for the title, banner image URL, video URL, poster image URL, and description of the movie.

## Database

The application uses SQLite as the database management system. The database file (`anime_movies.db`) stores information about the movies, including their titles, banner image URLs, video URLs, poster image URLs, descriptions, and view counts.

## Routes

- `/`: Displays the home page with a list of anime movies.
- `/watch/<int:movie_id>`: Allows users to watch a specific movie by its ID.
- `/movie_form`: Displays the movie form for adding a new movie.
- `/movie_form/<int:movie_id>`: Displays the movie form for editing an existing movie.

## Contributors

- **ch1ka**: [ch1kulya](https://github.com/ch1kulya)

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests. Enjoy watching anime movies on Anime Besu! 🎬🍿
