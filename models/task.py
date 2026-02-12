#1. criar classe tarefa
#2. passar atributos dentro do construtor init:
#atributos: id, titulo, descrincao da tarefa e se esta completada ou nao
#3.Definir os atributos passando self
#4 .criar um metodo de retorno em seguida que da retorno em dicionario de todas informaçoes que tem add na classe

class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        
    def to_dict(self):
        return {
            "id":self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }