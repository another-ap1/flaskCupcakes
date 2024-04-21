from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL

class AddCupcakeForm(FlaskForm):
    """Form for adding a new cupcake"""

    flavor=StringField("Flavor", validators=[InputRequired()])
    size=StringField("Size", validators=[InputRequired()])
    rating=FloatField("Rating", validators=[InputRequired()])
    image=StringField("image", validators=[Optional(), URL()])
