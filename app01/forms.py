from django.forms import Form,fields,widgets
from django.core.exceptions import ValidationError

class RegisterForm(Form):
    username = fields.CharField()
    password1 = fields.CharField()
    password2 = fields.CharField()
    avatar = fields.FileField()
    code = fields.CharField()

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request

    def clean_code(self):
        input_code = self.cleaned_data.get("code")
        sess_code = self.request.session.get("code")
        if input_code.upper() == sess_code.upper():
            return input_code
        raise ValidationError("验证码错误！")

    def clean(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 == p2:
            return None
        self.add_error("password2",ValidationError("密码不一致！"))