from app import db


class Bird(db.Model):
    __tablename__ = "bird_tania_nal"  # зміни на назву своєї таблиці
    bird_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(20))
    type = db.Column('type', db.String(20))
    weight = db.Column('weight', db.Integer)

    def __str__(self):
        return str("bird id: " + str(self.bird_id) + "\nname: " + str(
            self.name) + "\ntype: " + str(self.type) + "\nweight: " +
                   str(self.weight))
