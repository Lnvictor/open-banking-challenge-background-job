from mongoengine import connect


class Mongo:
    _connection = None

    def __init__(self, user, password, host, port, db):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = db

        self.conn_string = f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}?authMechanism=' \
            'DEFAULT'

    def get_connection(self):
        if self._connection is None:
            self._connection = connect(host=self.conn_string)

        return self._connection
