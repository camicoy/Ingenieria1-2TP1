class Bar( object ):
    def __init__( self,nombre, direc, enchufes, descr, wifi ):
        self.Nombre = nombre
        self.Direccion = direc
        self.Enchufes = enchufes
        self.Descripcion = descr
        self.WiFi = wifi
    def nombre( self ):
        return self.Nombre
    def direccion( self ):
        return self.Direccion
    def enchufes( self ):
        return self.Enchufes
    def descripcion( self ):
        return self.Descripcion
    def wifi( self ):
        return self.WiFi
    def __str__(self):
        return self.Nombre +" de " + self.Direccion
    def __repr__(self):
        return self.Nombre +" de " + self.Direccion
