class Response:
    def __init__(self, data: dict):
        try:
            self._data = data['result']
        except KeyError as e:
            self._data = {}

    @property
    def is_empty(self):
        return bool(self._data)

    def __repr__(self):
        """Returns values as string for debug purposes"""

        from pprint import pprint
        from io import StringIO

        with StringIO() as stream:
            pprint(self._data, stream=stream)
            return stream.getvalue()

    def __getattr__(self, key):
        """Get the entity's property"""
        getter = getattr(self, 'get_%s' % key, None)
        if callable(getter):
            # try:
            return getter()
            # except Exception as err:
            #     logging.error('%s["%s"]: %s', repr(self), key, err)
        elif key in self._data:
            return self._data.get(key)
