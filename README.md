# LibraryProject

A Django-based project for managing a library system. This project will eventually allow users to browse, borrow, and return books.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* pip

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/LibraryProject.git](https://github.com/your-username/LibraryProject.git)
    cd LibraryProject
    ```

2.  **Create and activate a virtual environment:**

    * On macOS and Linux:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    * On Windows:

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply the database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Running the Tests

To run the automated tests for this system, use the following command:

```bash
python manage.py test
