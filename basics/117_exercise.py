# Załóżmy, że pracujesz nad projektem dotyczącym energii odnawialnej i musisz wykonać obliczenia związane z energią słoneczną. Utworzyłeś już moduł o nazwie solar.py, który zawiera funkcje do wykonywania obliczeń, takich jak natężenie promieniowania słonecznego - solar_irradiance(), wydajność modułu fotowoltaicznego - pv_module_efficiency() i moc wyjściowa - power_output().
#
#
#
# Oblicz natężenie promieniowania słonecznego w W/m^2, biorąc pod uwagę powierzchnię i moc modułu fotowoltaicznego o podanych parametrach:
#
# area = 1.5 m^2
#
# power = 300 W
#
#
#
# Wynik wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# 300.0

from solar_117 import *

area = 1.5
power = 300
print(solar_irradiance(area, power))
