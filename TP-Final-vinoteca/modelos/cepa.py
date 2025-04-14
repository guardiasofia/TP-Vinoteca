import json
from .entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre)
    
    def obtenerVinos(self):
        from vinoteca import Vinoteca 
        todos_vinos = Vinoteca.obtenerVinos()
        return [vino for vino in todos_vinos if self.obtenerId() in [cepa.obtenerId() for cepa in vino.obtenerCepas()]]

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos":self.obtenerVinos(),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)