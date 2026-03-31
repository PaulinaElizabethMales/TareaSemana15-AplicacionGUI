import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.servicio = TareaServicio()

        # -------------------------
        # Campo de entrada
        # -------------------------
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # -------------------------
        # Botones
        # -------------------------
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack(pady=5)
        tk.Button(root, text="Marcar Completada", command=self.marcar_completada).pack(pady=5)
        tk.Button(root, text="Marcar Pendiente", command=self.marcar_pendiente).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack(pady=5)

        # -------------------------
        # Lista de tareas
        # -------------------------
        self.tree = ttk.Treeview(root, columns=("Descripcion", "Estado"), show="headings")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack(pady=10)

        # Estilos visuales
        self.tree.tag_configure("pendiente", foreground="orange")
        self.tree.tag_configure("hecho", foreground="green")

        # Eventos con ratón
        self.tree.bind("<Double-1>", self.marcar_completada_evento)

        # -------------------------
        # Atajos de teclado
        # -------------------------
        root.bind("<c>", self.marcar_completada_evento)   # tecla C
        root.bind("<C>", self.marcar_completada_evento)
        root.bind("<d>", self.eliminar_evento)            # tecla D
        root.bind("<D>", self.eliminar_evento)
        root.bind("<Delete>", self.eliminar_evento)       # tecla Supr
        root.bind("<Escape>", lambda e: root.destroy())   # cerrar app

    # -------------------------
    # Métodos funcionales
    # -------------------------

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def agregar_tarea(self):
        descripcion = self.entry.get()
        if descripcion:
            tarea = self.servicio.agregar_tarea(descripcion)
            self.tree.insert("", "end", iid=tarea.id,
                             values=(tarea.descripcion, "Pendiente"),
                             tags=("pendiente",))
            self.entry.delete(0, tk.END)

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def marcar_completada(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_tarea = int(seleccion[0])
            tarea = self.servicio.marcar_completada(id_tarea)
            if tarea:
                self.tree.item(id_tarea, values=(tarea.descripcion, "Hecho"),
                               tags=("hecho",))

    def marcar_pendiente(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_tarea = int(seleccion[0])
            for tarea in self.servicio.tareas:
                if tarea.id == id_tarea:
                    tarea.estado_completado = False
                    self.tree.item(id_tarea, values=(tarea.descripcion, "Pendiente"),
                                   tags=("pendiente",))
                    break

    def eliminar_evento(self, event):
        self.eliminar_tarea()

    def eliminar_tarea(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_tarea = int(seleccion[0])
            self.servicio.eliminar_tarea(id_tarea)
            self.tree.delete(id_tarea)