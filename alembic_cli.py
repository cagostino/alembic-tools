import argparse
import subprocess
import importlib
from sqlalchemy import create_engine

import os
import glob

def find_closest_database(default_db_name):
    # Search for .db or .sqlite files
    db_files = glob.glob("**/*.db", recursive=True) + glob.glob("**/*.sqlite", recursive=True)
    if db_files:
        return db_files[0]  # return the first match
    return default_db_name

def find_models(default_models):
    # Search for .py files containing "Base = declarative_base()"
    for root, _, files in os.walk("."):
        for filename in files:
            if filename.endswith(".py"):
                with open(os.path.join(root, filename), "r") as f:
                    if "Base = declarative_base()" in f.read():
                        return filename.replace(".py", "")
    return default_models



class GeneralDatabaseUtils:
    def __init__(self, db_name, models_module_name=None):
        self.db_name = db_name
        self.db_uri = f"sqlite:///{db_name}.db"
        if models_module_name:
            self.models_module = importlib.import_module(models_module_name)
        else:
            self.models_module = None

    def initialize_db(self):
        if self.models_module:
            engine = create_engine(self.db_uri)
            self.models_module.Base.metadata.create_all(engine)
        else:
            # Initialize empty database
            engine = create_engine(self.db_uri)
            engine.connect().close()

    def apply_migrations(self):
        subprocess.run(["alembic", "upgrade", "head"])

def generate_migration(message="Auto-generated migration"):
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", message])

def main():
    parser = argparse.ArgumentParser(description="General CLI tool for database operations.")
    
    parser.add_argument("--db_name", "-d", required=True, help="Name of the database")
    parser.add_argument("--models", "-m", help="Python module containing SQLAlchemy models")
    
    subparsers = parser.add_subparsers(title='Commands', description='Available commands', help='Additional help', dest='command')
    
    subparsers.add_parser('init', help='Initialize the database')
    migrate_parser = subparsers.add_parser('migrate', help='Apply database migrations')
    migrate_parser.add_argument('--message', '-m', default="Auto-generated migration", help='Migration message')
    
    args = parser.parse_args()
    
    db_util = GeneralDatabaseUtils(args.db_name, args.models)
    
    if args.command == 'init':
        db_util.initialize_db()
    elif args.command == 'migrate':
        if db_util.models_module:
            generate_migration(args.message)
            db_util.apply_migrations()
        else:
            print("No models module provided. Cannot migrate.")
    else:
        print("Invalid command. Use --help for usage information.")

if __name__ == "__main__":
    main()
