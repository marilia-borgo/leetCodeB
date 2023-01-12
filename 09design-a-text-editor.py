class TextEditor(object):

    def __init__(self):
        self.cursor = 0
        self.texto='' 
        print('null')
        # inicia o valor do cursor na posição do texto
        # inicia o texto

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        self.texto = self.texto+text
        self.cursor= len(self.texto)+1
        print('null')
        # pega o texto e local do cursos e adiciona o texto.
        # coloca o cursor no final do texto
        

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        # texto_cursor = self.texto[:self.cursor]
        self.texto = self.texto[:-k]
        self.cursor = (self.cursor-k)+1
        print(k)
        # leetcode
        # return k
        # for k elements text.pop
        #-k cursor 
        # retorna o numero de caracteres deletados 

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        # +k cursor 
        # retorn min(10,lentext_ caracteres na esquerda do cursor)
        if len(self.texto) > k:
            self.cursor = self.cursor-k
        texto_cursor= self.texto[:-self.cursor]
        print(texto_cursor[-10:])
            # leetcode
            # return texto_cursor[-10:]
    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        #-k cursor 
        if len(self.texto) > k:
            self.cursor = self.cursor+k
        texto_cursor= self.texto[:self.cursor]
        print(texto_cursor[-10:])
            # leetcode
            # return texto_cursor[-10:]
        

        


# Your TextEditor object will be instantiated and called as such:
obj = TextEditor()
obj.addText("leetcode")
obj.deleteText(4)
obj.addText("practice")
obj.cursorRight(3)
obj.cursorLeft(8)
obj.deleteText(10)
obj.cursorLeft(2)
obj.cursorRight(6)
