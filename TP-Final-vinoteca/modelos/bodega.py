import json
from .entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre)
    
    def obtenerVinos(self):
        from vinoteca import Vinoteca  
        todos_vinos = Vinoteca.obtenerVinos()
        return [vino for vino in todos_vinos if vino.obtenerBodega().obtenerId() == self.obtenerId()]
    
    def obtenerCepas(self):
        vinos = self.obtenerVinos()
        cepas = set()
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                cepas.add(cepa)
        return list(cepas)

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            "vinos": [vino.obtenerNombre() for vino in self.obtenerVinos()],
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        return [cepa.obtenerNombre() for cepa in cepas]

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        return [vino.obtenerNombre() for vino in vinos]