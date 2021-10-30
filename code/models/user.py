import sqlite3


class UserModel:
    def __init__(self, _id, username, password):
        # _id -> python's variable
        self.id = _id
        self.username = username
        self.password = password

    # not using 'self', make 'cls' as User class
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"

        # query parameter has to tuple. Do (var,) -> add ',' in the end to tell python this is tuple. (if only 1 paramator)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            # same as 'cls(row[0], row[1], row[2])'
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"

        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
