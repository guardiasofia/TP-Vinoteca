import json
from .entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre)
        self._bodega = bodega      
        self._cepas = cepas        
        self._partidas = partidas  
    
    def establecerBodega(self, bodega: str):
        self._bodega = bodega
    
    def establecerCepas(self, cepas: list):
        self._cepas = cepas
    
    def establecerPartidas(self, partidas: list):
        self._partidas = partidas
    
    def obtenerBodega(self):
        # Esta funcion sera implementada despues de la inicializacion
        pass
    
    def obtenerCepas(self):
        # Esta funcion sera implementada despues de la inicializacion
        pass
    
    def obtenerPartidas(self):
        return self._partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def convertirAJSONFull(self):
        return self.convertirAJSON()

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)