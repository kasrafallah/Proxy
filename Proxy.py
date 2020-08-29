class Proxy:

    def __init__(self, obj):
        self._obj = obj
        self.last_invoked=''
        self.counter = {}

    def __getattr__(self, attr):
        if attr in dir(self._obj):

            self.last_invoked = attr

            if attr in self.counter:
                temp = self.counter.get(attr)
                temp += 1
                temp_dict = { attr : temp }
                self.counter.update(temp_dict)
            else:
                temp_dict = {attr:1}
                self.counter.update(temp_dict)

            return getattr(self._obj, attr)
        else:
            raise Exception('No Such Method')

    def last_invoked_method(self):
        if self.last_invoked == '':
            raise Exception('No Method Is Invoked')
        else:
            return self.last_invoked

    def count_of_calls(self, method_name):
        if method_name in self.counter:
            return self.counter.get(method_name)
        else:
            return 0

    def was_called(self, method_name):
        if method_name in self.counter:
            return True
        else:
            return False

