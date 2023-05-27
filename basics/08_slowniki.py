empty_dict = dict()
print(empty_dict)

d = {}
print(d)

pol_to_eng = {"jeden": "one", "dwa": "two"}
pol_to_eng["trzy"] = "three"

print(pol_to_eng)

pol_to_eng_copies = pol_to_eng.copy()
pol_to_eng.clear()
print(pol_to_eng_copies)

print(list(pol_to_eng_copies.keys()))
print(list(pol_to_eng_copies.values()))
print(list(pol_to_eng_copies.items()))

# Get daje możliwość podania co zwrocic kiedy elementu nie znaleziono.
print(pol_to_eng_copies.get("zero", "Nie znaleziono."))

pol_to_eng_copies.pop("dwa")
print(pol_to_eng_copies)
pol_to_eng_copies.popitem()
print(pol_to_eng_copies)

pol_to_eng = {"jeden": "one", "dwa": "two"}

pol_to_eng.update({"jeden": 1})
pol_to_eng.update({"dwa": 2})
print(pol_to_eng)