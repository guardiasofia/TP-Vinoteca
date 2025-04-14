class EntidadVineria:
    def __init__(self, id: str, nombre: str):
        self._id = id
        self._nombre = nombre

    def establecerNombre(self, nombre: str):
        self._nombre = nombre

    def obtenerId(self) -> str:
        return self._id

    def obtenerNombre(self) -> str:
        return self._nombre

    def __eq__(self, otro):
        if not isinstance(otro, EntidadVineria):
            return False
        return self._id == otro._id

    def __hash__(self):
        return hash(self._id)  