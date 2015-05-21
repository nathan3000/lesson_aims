from flask.ext.wtf import Form
from wtforms import SelectField, TextAreaField, TextField, validators

class RequiredIf(object):
    # a validator which makes a field required if
    # another field is set and has a truthy value

    def __init__(self, other_field_name, values, message=None):
        self.other_field_name = other_field_name
        self.values = values
        if not message:
            message = u'This field is required.'
        self.message = message

    def __call__(self, form, field):
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        for value in self.values:
       		if (other_field.data == value) and (not field.data):
        		raise validators.ValidationError(self.message)


class AimsForm(Form):
	groupName = SelectField('Group Name', [validators.NumberRange(0, message="Please select a group.")], coerce=int)
	seriesName = SelectField('Series Name', [validators.NumberRange(0, message="Please select a series.")], coerce=int, )
	biblePassage = TextField('Bible Passage', [validators.Required()])
	whatTheyLearnt = TextAreaField('Today your child learnt that..', [validators.Required()])
	lessonAim = TextAreaField('Lesson Aim', [RequiredIf('groupName', [2,3])])
	tip1 = TextField('Tip #1', [validators.Required()])
	tip2 = TextField('Tip #2', [validators.Required()])
	memoryVerse = TextField('Memory Verse', [RequiredIf('groupName', [2,3])])
	newSeriesName = TextField('New Series Name', [RequiredIf('seriesName', [0])])