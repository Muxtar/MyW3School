from fonks import main

class rule(main):
    def __init__(self):
        super().__init__()
        self.app.add_url_rule('/', 'main', self.main)
        self.app.add_url_rule("/form", "form", self.form, methods = ['POST', 'GET'])
        self.app.add_url_rule("/user", "user", self.user, methods = ['POST', 'GET'])
        self.app.add_url_rule("/user/sigin", "user_sigin", self.user_sigin, methods = ['POST', 'GET'])
        self.app.add_url_rule("/user/login", "user_login", self.user_login, methods  = ['POST', 'GET'])
        self.app.add_url_rule('/user/logout', 'user_logout', self.user_logout, methods = ['POST', 'GET'])
        self.app.add_url_rule('/notready', 'notready', self.notready, methods = ['POST', 'GET'])

        self.app.add_url_rule('/contents/<statusId>', 'contents', self.contents, methods = ['POST', 'GET'])


        self.app.add_url_rule('/yoxla', 'yoxla', self.yoxla, methods = ['POST', 'GET'])

        self.app.add_url_rule('/admin', 'admin', self.admin, methods = ['POST', 'GET'])
        self.app.add_url_rule('/delete', 'delete', self.delete, methods = ['POST', 'GET'])
        self.app.add_url_rule('/edit', 'edit', self.edit, methods = ['POST', 'GET'])

        self.app.add_url_rule('/add', 'add', self.add, methods = ['POST'])
        self.app.add_url_rule('/notReadySend', 'notReadySend', self.notReadySend, methods = ['POST', 'GET'])
        self.app.add_url_rule('/notReadyDelete', 'notReadyDelete', self.notReadyDelete, methods = ['POST', 'GET'])

        self.app.add_url_rule('/ready', 'ready', self.ready, methods = ['POST', 'GET'])
        self.app.add_url_rule('/<thema>/<content>', 'test', self.test, methods = ['POST', 'GET'])


rule().start()
