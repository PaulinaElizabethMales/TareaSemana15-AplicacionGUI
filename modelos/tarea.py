class Tarea:
    def __init__(self, id, descripcion, estado_completado=False):
        self.id = id
        self.descripcion = descripcion
        self.estado_completado = estado_completado