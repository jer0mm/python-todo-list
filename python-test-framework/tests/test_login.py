class LoginTest:

    def login(self, username, password):
        if username == 'admin' and password == 'admin123':
            return 'success'
        return 'failure'
