from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.next_id = 1

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self.next_id, descripcion)
        self.tareas.append(tarea)
        self.next_id += 1
        return tarea

    def marcar_completada(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.estado_completado = True
                return tarea
        return None

    def eliminar_tarea(self, id_tarea):
        self.tareas = [t for t in self.tareas if t.id != id_tarea]

    def listar_tareas(self):
        return self.tareas