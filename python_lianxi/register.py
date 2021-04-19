users = [{'user': 'lemontree', 'password': '123456'}]
class register():
    def __init__(self,username, password1,password2):
        self.username = username
        self.password1 = password1
        self.password2 = password2
    # 判断是否有参数为空
    def re(self):
        if not self.username and not self.password1 and not self.password2:
            return {"code": 0, "msg": "所有参数不能为空"}

        # 注册功能
        for user in users:  # 遍历出所有账号，判断账号是否存在
            if self.username == user['user']:
                # 账号存在
                return {"code": 0, "msg": "该账户已存在"}
        else:
            if self.password1 != self.password2:
                # 两次密码不一致
                return {"code": 0, "msg": "两次密码不一致"}
            else:
                # 账号不存在 密码不重复，判断账号密码长度是否在 6-18位之间
                if 6 <= len(self.username)<=18 or 6 <= len(self.password1) <= 18:
                    # 注册账号
                    users.append({'user': self.username, 'password': self.password2})
                    return {"code": 1, "msg": "注册成功"}
                else:
                    # 账号密码长度不对，注册失败
                    return {"code": 0, "msg": "账号和密码必须在6-18位之间"}
if __name__ == "__main__":
    a = register('lemontree', '123456', '123456')
    print(a.re())