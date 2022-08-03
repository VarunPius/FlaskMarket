####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# External modules:
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

# Internal Modules:
from market.models import User


####################################################################################################
# Form models                                                                                     ##
####################################################################################################

## Registration form ##
class RegisterForm(FlaskForm):
    def validate_user_name(self, username_to_chk):      # FlaskForm will see `validate_` and
                                                        # then check if field exists for value after that
                                                        # It will automatically apply the validation
                                                        # hence important to choose proper naming and having it start with `validate_`
        user = User.query.filter_by(username=username_to_chk.data).first()
        if user:
            raise ValidationError('Username already exists! Please choose another username')
    
    def validate_email_address(self, email_to_chk):
        user = User.query.filter_by(email=email_to_chk.data).first()
        if user:
            raise ValidationError('Email already exists! Please login')

    #user_name = StringField(label = 'User Name:')         
        # `user_name` is used by Jinja forms to reference with variable
        # while `label = 'User Name:'` will be what's displayed in the HTML
        # HTML code: {{ form.user_name.label() }}  ==>  HTML page: User Name:
    #user_name = StringField(label = 'User Name:', validators=Length(min=5, max=30))
    user_name = StringField(label = 'User Name:', validators=[Length(min=5, max=30), DataRequired()]) 
    email_address = StringField(label = 'Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = 'Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label = 'Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create account')


class LoginForm(FlaskForm):
    user_name = StringField(label = 'User Name:', validators=[DataRequired()]) 
    password = PasswordField(label = 'Password:', validators=[DataRequired()])
    submit = SubmitField(label = 'Sign in')


class BuyItemForm(FlaskForm):
    submit = SubmitField(label = 'Buy Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label = 'Sell Item!')
