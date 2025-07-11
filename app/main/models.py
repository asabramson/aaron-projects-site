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
    lm_stats : sqlo.Mapped['LaskerMorrisStats'] = sqlo.relationship(back_populates= 'player')

    # posts : sqlo.WriteOnlyMapped['Post'] = sqlo.relationship(back_populates= 'writer') FROM TEMPLATE, NOT RELAVENT

    def __repr__(self):
        return 'id: {} username: {}'.format(self.id, self.username)
    
    def get_username(self):
        return self.username
    
    def get_lm_stats(self):
        return self.lm_stats
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # def get_user_posts(self):
    #     return db.session.scalars(self.posts.select()).all() FROM TEMPLATE, NOT RELAVENT


class LaskerMorrisStats(db.Model):
    __tablename__ = 'laskermorris'
    id: sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    num_games: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default=0)
    num_wins: sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default=0)

    # Relationships & Foreign Keys
    user_id : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(User.id), index = True)
    player : sqlo.Mapped[User] = sqlo.relationship(back_populates= 'lm_stats')

    def get_games(self):
        return self.num_games

    def get_wins(self):
        return self.num_wins
    
    def get_user(self):
        return self.player