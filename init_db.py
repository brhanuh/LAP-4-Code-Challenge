from LazyURL import db
from LazyURL.Models.lazy import LazyUrl

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()