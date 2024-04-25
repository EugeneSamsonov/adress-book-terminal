class AdrBookExceptions(Exception):
    msg = 'AdrBookExceptions'

    def __init__(self, msg='AdrBookExceptions'):
        super().__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class ABInputError(AdrBookExceptions):
    def __init__(self, msg="You enter invalid data, enter data in correct format:\n "
                           "{number (with out spaces) - Family Name Surname}"):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return self.msg
