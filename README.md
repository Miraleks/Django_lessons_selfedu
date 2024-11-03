# Django Website Project

This project is based on the tutorial series "Kind Django" by Sergey Balakirev, available on YouTube: [Kind Django Playlist](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8yU5h2vwZ4LO7h1xt8COUXl).

## Overview

This is an educational project to create a website using the Django framework. The goal is to learn Django basics through practical examples and build a functional website step by step.

## Features

- User authentication
- CRUD operations
- Dynamic content rendering
- Admin panel management
- Custom templates and static files

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-website-project.git
    cd django-website-project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

After running the server, open your browser and go to `http://127.0.0.1:8000/` to view the website. You can log in, create, read, update, and delete posts, and explore various features implemented in the project.

## Contributing

Feel free to fork this repository and submit pull requests if you have improvements or fixes. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to Sergey Balakirev for his amazing tutorial series: [Kind Django Playlist](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8yU5h2vwZ4LO7h1xt8COUXl).
