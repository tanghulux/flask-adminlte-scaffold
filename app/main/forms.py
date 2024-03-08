from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class CfgNotifyForm(FlaskForm):
    check_order = StringField('排序', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_type = SelectField('通知类型', choices=[('MAIL', '邮件通知'), ('SMS', '短信通知')],
                              validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_name = StringField('通知人姓名', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_number = StringField('通知号码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    status = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')

class CltInfoForm(FlaskForm):
    charge = StringField('负责人', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    source = SelectField('信息来源', choices=['行业会议', '公开信息', '熟人推荐', '客户介绍'], validators=[Length(0, 64, message='长度不正确')])
    type1 = SelectField('行业分类', choices=['化工', '钢铁', '电力', '水泥', '其他'], validators=[Length(0, 64, message='长度不正确')])
    type2 = SelectField('具体类别', choices=['硫酸', '锅炉', '玻璃窑炉', '燃煤锅炉'], validators=[Length(0, 64, message='长度不正确')])
    info = StringField('其他信息', validators=[Length(0, 200, message='长度不正确')])
    product = SelectField('适用产品', choices=['催化剂', '工程', '活性炭', '其他'], validators=[Length(0, 64, message='长度不正确')])
    method = SelectField('跟进方式', choices=['电话', '微信', '到访', '其他'],validators=[Length(0, 64, message='长度不正确')])
    progress = StringField('跟进进度', validators=[Length(0, 64, message='长度不正确')])
    who = StringField('联系人', validators=[Length(0, 64, message='长度不正确')])
    tel = StringField('联系电话', validators=[Length(0, 64, message='长度不正确')])
    remark = StringField('备注', validators=[Length(0, 200, message='长度不正确')])
    submit = SubmitField('提交')