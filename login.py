def login(username, password):
    if username == '' or len(username) == 0:
        return "用户名不能为空"
    if password == '' or len(password) == 0:
        return "密码不能为空"

    if username == 'admin' and password == '123':
        return "登录成功"
    if username == '' and password == '123':
        return "用户名不能为空"
