from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime

from config import CARD_REGEX, SECURITY_CODE_REGEX, EXPIRATION_DATE_FORMAT


class PaymentInputSchema(Schema):
    card_number = fields.Str(required=True, validate=validate.Regexp(CARD_REGEX))
    card_holder = fields.Str(required=True)
    expiration_date = fields.Str(required=True)
    security_code = fields.Str(required=True, validate=validate.Regexp(SECURITY_CODE_REGEX))
    amount = fields.Decimal(required=True, validate=[validate.Range(min=1, error="Value must be greater than 0")])

    @validates('expiration_date')
    def is_not_in_future(self, value):
        try:
            date = datetime.strptime(value, EXPIRATION_DATE_FORMAT)
        except:
            raise ValidationError("Invalid date format!")

        now = datetime.now()
        if date <= now:
            raise ValidationError("Expiry date can not be in the past!")
