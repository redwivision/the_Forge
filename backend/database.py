from sqlmodel import create_engine, SQLModel, Session
import os

# --- THE FORGE DATABASE ---
# This file is the "Permanent Box" where your knowledge lives.

sqlite_file_name = "forge.db"
sqlite_url = f"sqlite:///./{sqlite_file_name}"

# The "Engine" is the physical motor that talks to the file.
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    """Tells the engine to build the tables based on our Models."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """A helper to give us a 'Talking Session' to the DB."""
    with Session(engine) as session:
        yield session
