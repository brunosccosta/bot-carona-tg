class Carona(object):
    
    def __init__(self, pessoa, horario):
        self.pessoa = pessoa
        self.horario = horario

    def __str__(self):
        return "Carona " + self.pessoa + " as " + str(self.horario)
