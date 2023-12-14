from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form to add pet to adoption list."""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Comments", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form to edit pet information."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Comments", validators=[Optional()])
    available = BooleanField("Available?")
