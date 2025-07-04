from typing import Optional

from app import db, login
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    username : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), index = True, unique = True)
    password_hash : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(256))

    # Relationships
    # posts : sqlo.WriteOnlyMapped['Post'] = sqlo.relationship(back_populates= 'writer') FROM TEMPLATE, NOT RELAVENT

    def __repr__(self):
        return 'id: {} username: {}'.format(self.id, self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # def get_user_posts(self):
    #     return db.session.scalars(self.posts.select()).all() FROM TEMPLATE, NOT RELAVENT