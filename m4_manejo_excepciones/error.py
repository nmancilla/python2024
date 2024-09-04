class DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension < 1:
            return f'La dimensión {self.dimension} no puede ser menor a 1'
        else:
            return f'La dimesión {self.dimension} no pude ser mayor al máximo {self.maximo}'