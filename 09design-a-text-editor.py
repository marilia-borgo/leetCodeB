class TextEditor:

    def __init__(self, text='', cursor=None):
        self.texto : str = text
        self.cursor :int = len(text) if cursor is None else cursor

    def addText(self, text: str) -> None:
        inicio = self.texto[0:max(0,self.cursor)]
        fim = self.texto[self.cursor:]
        self.texto = inicio+text+fim
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        inicio = self.texto[0:max(0,self.cursor-k)]
        fim = self.texto[self.cursor:]
        retorno = min(self.cursor, k) 
        self.cursor = max(0,self.cursor-k)
        self.texto= inicio + fim
        print(retorno)
        # leetcode
        # return retorno

    def cursorLeft(self, k: int) -> str:
        if self.cursor - k < 0:
            self.cursor = 0
        else:
            self.cursor -= k
        # leetcode
        # return self.getTexto()
        print(self.getTexto())

    def cursorRight(self, k: int) -> str:
        if self.cursor + k > len(self.texto):
            self.cursor = len(self.texto) 
        else:
            self.cursor += k
        # leetcode
        # return self.getTexto()
        print(self.getTexto())

    def getTexto(self) -> str: 
        return self.texto[max(0 , self.cursor-10):min(self.cursor, len(self.texto))]