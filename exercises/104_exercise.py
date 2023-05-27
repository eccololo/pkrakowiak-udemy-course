"""
Wykorzystując pętlę while policz ile trzeba czekać lat,
aby zwrot z poniżej opisanej inwestycji co najmniej się
podwoił (pod uwagę bierzemy tylko pełne okresy).
"""
n = 1
pv = 1000
r = 0.04
fv = pv
"""
n - liczba okresów (w latach)
pv - present value - wartość obecna
r - stopa procentowa (roczna)
fv - future value - wartość przyszła
"""
while fv < 2000:
    fv = fv * (1 + r)
    n += 1

fv = round(fv, 2)
print("Wartość przyszła: {} PLN. Liczba okresów: {} lat".format(fv, n-1))