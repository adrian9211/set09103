# Flask Notes App

Welcome to the Flask Notes App repository! This project is a fully working production version of a Flask web application that allows users to create accounts and write personal notes. The application securely stores notes in an SQLite database.

## Features

- **Account Creation:** Users can create accounts to access personalized features.
- **Note Creation:** Users can create, edit, and delete personal notes.
- **Secure Storage:** Notes are securely stored in an SQLite database.
- **User Authentication:** Account creation and note management are available only to authenticated users.

## Getting Started

To run the Flask Notes App locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-notes-app.git
   cd flask-notes-app

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
2. Set up the database:

    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```

3. Run the application:

    ```
    flask run
    ```
The app will be accessible at http://localhost:5000.

## Usage
1. Access the application in your web browser.
2. Create a new account or log in if you already have one.
3. Start creating personal notes.

## Database
The application uses SQLite as the database. The database file (database.db) is automatically created and migrated using Flask-Migrate.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- This app was built using the Flask web framework.
- Special thanks to the Flask community and contributors.

Happy note-taking with Flask Notes App! 📝🚀