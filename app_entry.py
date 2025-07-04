from config import Config

from app import create_app, db
from app.main.home.models import Room
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
# from app.main.home.models import Tag

app = create_app(Config)

# @app.shell_context_processor
# def make_shell_context():
#     return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'Post': Post, 'Tag': Tag, 'User': User } UNCOMMENT LATER

def add_tags(*args, **kwargs):
    allrooms = [{'building' : 'Fuller', 'roomNumber' : 'B46', 'capacity' : 60}, 
                {'building' : 'UnityHall', 'roomNumber' : '175', 'capacity' : 100},
                {'building' : 'UnityHall', 'roomNumber' : '150', 'capacity' : 80},
                {'building' : 'Goddard', 'roomNumber' : '227', 'capacity' : 56}]
    if len(db.session.scalars(sqla.select(Room)).all()) == 0:
        for room in allrooms:
            theroom = Room (building = room['building'],roomNumber=room['roomNumber'], capacity = room['capacity'] ) 
            db.session.add(theroom)
            db.session.commit()


@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()
        add_tags()

if __name__ == "__main__":
    app.run(debug=True)