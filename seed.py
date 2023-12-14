from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

pet1 = Pet(
    name="Sammy",
    species="dog",
    photo_url="",
    age=6,
    notes="High energy.",
    available=True,
)

db.session.add(pet1)
db.session.commit()
