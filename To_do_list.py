class Tarefa:
    def __init__ (self, id, titulo, descricao, status, data_de_entrega):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_de_entrega = data_de_entrega
        self.array = [{"id": self.id} , {"Titulo" : self.titulo} ,{"descricao": self.descricao} ,{"status":self.status} , {"data de entrega":self.data_de_entrega}]

    def __str__(self):
        return str(self.array)



