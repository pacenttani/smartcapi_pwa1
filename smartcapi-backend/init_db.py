
from app.services.db import Base, engine
from app.model import tables

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created.")
