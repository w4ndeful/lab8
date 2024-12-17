from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"rows": 10, "cols": 50})
    author = SelectField('Author', coerce=int, choices=[])
    tags = SelectMultipleField('Tags', coerce=int, choices=[])
