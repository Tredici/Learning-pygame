import pygame

# classe ausiliaria che serve a semplificare le
# operazioni con le posizioni (ovvero vettori di
# due dimensioni)
class Pair:
    def sum(v, w):
        """ Somma di vettori """
        return (v[0]+w[0], v[1]+w[1])
    def neg(v):
        """ Vettore opposto """
        return (v[0], v[1])
    def diff(v, w):
        """ Differenza di vettori """
        return Pair.sum(v, Pair.neg(w))
    def mul(a, v):
        """ Moltiplicazione vettore per scalare """
        return (a*v[0], a*v[1])
    def div(a, v):
        """ Moltiplicazione vettore per l'inverso di uno scalare """
        return (v[0]/a, v[1]/a)

class SquareStack:
    """ Rappresenta e gestisce una pila di quadrati gestiti da pygame  """
    def __init__(self, num = 1, height = 40, width = 40):
        self.squares = [pygame.Rect(left=0, top=i*height, width=width, height=height) for i in range(num)]
        # orientazione
        self.vertical = True
        # dimensione
        self._height = num*height
        self._width = width
        # centro
        self._center = (self.squares[0]+self.width/2, self.squares[0]+self.height/2)

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, new_center):
        """ Cambia il centro di tutto """
        # di quanto viene spostato il tutto?
        offset = Pair.diff(new_center, self.center)
        for el in self.squares:
            el.center = Pair.sum(el.center, offset)
        self._center = new_center

    def blitOn(self, surface):
        pass
