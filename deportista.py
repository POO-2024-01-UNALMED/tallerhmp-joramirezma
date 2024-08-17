class Deportista():
    
    def __init__(self,deporte,añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self,deporte):
        self._deporte = deporte

    def getAñosPracticados(self):
        return self._añosPracticando
    
    def setAñosPracticados(self, añosPracticando):
        self._añosPracticando = añosPracticando