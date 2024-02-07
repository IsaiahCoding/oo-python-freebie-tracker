

from .company import Company
from .dev import Dev
from .freebie import Freebie


__all__ = [ 'Company', 'Dev', 'Freebie' ]


costco =Company ("Costco", 1996)
walmart =Company ( "Wal-Mart", 1989)

dave = Dev ("Dave")
rooj = Dev("Rooj")

freebie1 = Freebie (dave, costco, "Hat", 5)