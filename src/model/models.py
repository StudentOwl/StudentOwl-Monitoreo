class Component(object):
    """
    Class to represent an academic component
    """

    def __init__(self, code: str, name: str, parallel: str):
        """
        Constructor de clase
        """
        self._code = code
        self._name = name
        self._parallel = parallel

    @property
    def code(self) -> str:
        """
        code property.
        """
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def name(self) -> str:
        """
        name property.
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def parallel(self) -> str:
        """
        parallel property.
        """
        return self._parallel

    @parallel.setter
    def parallel(self, value):
        self._parallel = value

    def __str__(self) -> str:
        return f'{self._name} ({self._parallel})'
