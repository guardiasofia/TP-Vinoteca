from flask import Flask
from flask_restful import Api

from vinoteca import Vinoteca
from recursos import *

def implementar_funciones():
    def obtener_vinos_bodega(self):
        return [vino for vino in Vinoteca.obtenerVinos() 
                if vino.obtenerBodega().obtenerId() == self.obtenerId()]
    
    def obtener_cepas_bodega(self):
        vinos = self.obtenerVinos()
        cepas_set = set()
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                cepas_set.add(cepa.obtenerId())
        
        
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in cepas_set]
    
    def obtener_vinos_cepa(self):
        return [vino for vino in Vinoteca.obtenerVinos() 
                if self.obtenerId() in [cepa.obtenerId() for cepa in vino.obtenerCepas()]]
    
    def obtener_bodega_vino(self):
        return Vinoteca.buscarBodega(self._bodega)
    
    def obtener_cepas_vino(self):
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self._cepas]

    from modelos.bodega import Bodega
    from modelos.cepa import Cepa
    from modelos.vino import Vino

    Bodega.obtenerVinos = obtener_vinos_bodega
    Bodega.obtenerCepas = obtener_cepas_bodega
    Cepa.obtenerVinos = obtener_vinos_cepa
    Vino.obtenerBodega = obtener_bodega_vino
    Vino.obtenerCepas = obtener_cepas_vino

if __name__ == "__main__":
    Vinoteca.inicializar()
    implementar_funciones()

    app = Flask(__name__)
    api = Api(app)
    
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')

    app.run(debug=True)
