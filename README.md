Certainly! Below is the README content that you can use for your GitHub repository:

---

# My Alembic CLI

A CLI tool for managing SQLAlchemy databases and applying Alembic migrations. This tool aims to generalize database initialization and migration tasks so that you can use it across multiple projects.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/cagostino/alembic-tools.git
    ```

2. Navigate into the cloned directory:

    ```bash
    cd alembic-tools
    ```

3. Install the package:

    ```bash
    pip install --editable .
    ```

    > **Note**: You may need administrative privileges to install system-wide packages. On Unix-like systems, you can use `sudo pip install --editable .`.

## Usage

After installation, the CLI tool will be available as `my_alembic_cli`. You can run the following commands:

### Initialize Database

To initialize a new database:

```bash
my_alembic_cli --db_name your_db_name --models your_models_module init
```

### Apply Migrations

To apply database migrations:

```bash
my_alembic_cli --db_name your_db_name --models your_models_module migrate
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Feel free to adjust the content as needed. Would you like help with anything else?
