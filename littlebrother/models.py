import datetime
import peewee
from littlebrother import db

class Voter(db.Model):
    id = peewee.PrimaryKeyField(column_class=peewee.IntegerColumn, db_column='voterid')
    county = peewee.CharField()
    first_name = peewee.CharField()
    middle_name = peewee.CharField()
    last_name = peewee.CharField()
    suffix = peewee.CharField()
    birthdate = peewee.CharField()
    registrationdate = peewee.CharField()
    address1 = peewee.CharField()
    address2 = peewee.CharField()
    city = peewee.CharField()
    state = peewee.CharField()
    zip = peewee.CharField()
    phone = peewee.CharField()
    party = peewee.CharField()
    congressionaldistrict = peewee.CharField()
    senatedistrict = peewee.CharField()
    assemblydistrict = peewee.CharField()
    educationdistrict = peewee.CharField()
    regentdistrict = peewee.CharField()
    registeredprecinct = peewee.CharField()
    countystatus = peewee.CharField()
    countyvoterid = peewee.CharField()
    idrequired = peewee.CharField()

    @property
    def full_name(self):
        return " ".join([self.first_name or '(no first name)',
                         self.last_name or '(no last name)'])

    @property
    def url(self):
        return "/detail/%d" % self.id

    @property
    def years_old(self):
        """
        Return age (in years) of voter.
        """
        today = datetime.datetime.today()
        born = datetime.datetime.strptime(self.birthdate, "%m/%d/%Y")
        return (today - born).days / 365

    @classmethod
    def search(cls, query, field='name'):
        if field == 'name':
            search = peewee.R("to_tsvector('english', last_name || ' ' || first_name) @@ "
                              "plainto_tsquery('english', %s)", query)
        elif field == 'address':
            search = peewee.R("to_tsvector('english', address1) @@ "
                              "plainto_tsquery('english', %s)", query)

        return cls.select().where(search).order_by('last_name', 'first_name')

    class Meta:
        db_table = 'voters'
        ordering = ('last_name', 'first_name')
