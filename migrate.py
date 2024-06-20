from peewee_migrate import Router
from database.db import db

router = Router(db)

router.run()
