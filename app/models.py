# -*- coding: utf-8 -*-

from peewee import MySQLDatabase, Model, CharField, BooleanField, IntegerField
import json
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import login_manager
from conf.config import config
import os

cfg = config[os.getenv('FLASK_CONFIG') or 'default']

db = MySQLDatabase(host=cfg.DB_HOST, user=cfg.DB_USER, passwd=cfg.DB_PASSWD, database=cfg.DB_DATABASE)


class BaseModel(Model):
    class Meta:
        database = db

    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        # return str(r)
        return json.dumps(r, ensure_ascii=False)


# 管理员工号
class User(UserMixin, BaseModel):
    username = CharField(unique=True)  # 用户名
    password = CharField()  # 密码
    fullname = CharField()  # 真实性名
    email = CharField()  # 邮箱
    phone = CharField()  # 电话
    status = BooleanField(default=False)  # 生效失效标识

    def verify_password(self, raw_password):
        # return check_password_hash(self.password, raw_password) # 未加密安全处理

        if raw_password == self.password:
            return True
        return False


# 通知人配置
class CfgNotify(BaseModel):
    check_order = IntegerField()  # 排序
    notify_type = CharField()  # 通知类型：MAIL/SMS
    notify_name = CharField()  # 通知人姓名
    notify_number = CharField()  # 通知号码
    status = BooleanField(default=True)  # 生效失效标识

# 销售搜集客户有效信息的任务
class CltInfo(BaseModel):
    charge = CharField()  # 负责人
    source = CharField()  # 信息来源
    type1 = CharField()  # 行业分类
    type2 = CharField()  # 具体分类
    info = CharField()  # 其他信息
    product = CharField()  # 对应销售的产品
    method = CharField()  # 跟进方式
    progress = CharField()  # 跟进进度
    who = CharField()  # 对方客户联系人
    tel = CharField()  # 联系电话
    remark = CharField()  # 备注


@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))


# 建表
def create_table():
    db.connect()
    db.create_tables([CltInfo, CfgNotify, User])


if __name__ == '__main__':
    create_table()
