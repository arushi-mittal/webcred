from flask_wtf import Form
from wtforms import TextField, DecimalField, StringField, IntegerField, RadioField, SubmitField, SelectField, validators

class PreferencesForm (Form) :
    Feature = SelectField(choices=[ "Surface", "Content", "Off-Page"])
    Genre = SelectField(choices=["Personal", "Blog", "Academic", "Social", "Business"])
    S1Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S2Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S3Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S4Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S5Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S6Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S7Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S8Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S9Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    S10Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C1Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C2Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C3Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C4Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C5Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C6Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    C7Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])
    O1Weightage = DecimalField("Weightage", [validators.Required("Enter weightage"), validators.NumberRange(min=0, max=1, message="Value must be between 0 and 1")])


    submit = SubmitField("Confirm")