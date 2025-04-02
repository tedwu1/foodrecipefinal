from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=80)])
    description = TextAreaField("Description", validators=[DataRequired()], render_kw={"rows": 3})
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()], render_kw={"rows": 5})
    instructions = TextAreaField("Instructions", validators=[DataRequired()], render_kw={"rows": 8})
    submit = SubmitField("Submit")
