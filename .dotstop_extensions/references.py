
from trudag.dotstop.core.reference.references import BaseReference

class CPPTestReference(BaseReference):
    def __init__(self, name: str, path: str) -> None:
        self._name = name
        self._path = path

    @classmethod
    def type(cls) -> str:
        return "cpp_test"

    def get_section(self) -> str:
        # TODO properly extract the test section from the file 
        res = ""
        in_test_section = False
        with open(self._path, 'r') as file:
            for line in file.readlines():
                if f'"{self._name}"' in line:
                    in_test_section = True
                if in_test_section:
                    res += line
        return res
                    

    @property
    def content(self) -> bytes:
        return self.get_section().encode('utf-8')
  

    def as_markdown(self, filepath: None | str = None) -> str:
        with open(self._path, 'r') as file:
            return self.content.decode('utf-8')
        