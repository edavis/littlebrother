from wtforms import Form, TextField, SelectField

class Search(Form):
    type = SelectField(u'Search type', choices=[('name', 'Name'),
                                                ('address', 'Address')])
    query = TextField(u'Search query')
