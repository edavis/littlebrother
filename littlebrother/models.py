import peewee

db = peewee.PostgresqlDatabase('littlebrother')
db.connect()

class Voter(peewee.Model):
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

    def __unicode__(self):
        return " ".join([self.first_name, self.last_name])

    class Meta:
        database = db
        db_table = 'voters'
