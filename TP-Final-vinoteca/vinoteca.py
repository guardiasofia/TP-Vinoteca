import os
import json
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:
    __nombreArchivoDeDatos =  "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def __obtenerRutaArchivo(cls):
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        ruta_archivo = os.path.join(script_dir, cls.__nombreArchivoDeDatos)  
        return ruta_archivo

    @classmethod
    def __parsearArchivoDeDatos(cls):
        ruta_archivo = cls.__obtenerRutaArchivo() 
        try:
            
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)  
            return datos
        except FileNotFoundError:
            print(f"Error: El archivo {ruta_archivo} no se encontro.")
            raise
        except json.JSONDecodeError:
            print(f"Error: El archivo {ruta_archivo} no se pudo decodificar como JSON.")
            raise

    @classmethod
    def __convertirJsonAListas(cls, datos):
        cls.__bodegas = [Bodega(b['id'], b['nombre']) for b in datos['bodegas']]
        cls.__cepas = [Cepa(c['id'], c['nombre']) for c in datos['cepas']]
        cls.__vinos = [Vino(v['id'], v['nombre'], v['bodega'], v['cepas'], v['partidas']) 
                    for v in datos['vinos']]

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        bodegas = cls.__bodegas.copy()
        if orden == "nombre":
            bodegas.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
        elif orden == "vinos":
            bodegas.sort(key=lambda x: len(x.obtenerVinos()), reverse=reverso)
        return bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        cepas = cls.__cepas.copy()
        if orden == "nombre":
            cepas.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
        return cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos = cls.__vinos.copy()
        if anio:
            vinos = [v for v in vinos if anio in v.obtenerPartidas()]
        
        if orden == "nombre":
            vinos.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
        elif orden == "bodega":
            vinos.sort(key=lambda x: x.obtenerBodega().obtenerNombre(), reverse=reverso)
        elif orden == "cepas":
            vinos.sort(key=lambda x: len(x.obtenerCepas()), reverse=reverso)
        
        return vinos

    @classmethod
    def buscarBodega(cls, id):
        for bodega in cls.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    @classmethod
    def buscarCepa(cls, id):
        for cepa in cls.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    @classmethod
    def buscarVino(cls, id):
        for vino in cls.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None