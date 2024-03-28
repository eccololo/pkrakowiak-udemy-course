quotations = {}

quotations.setdefault("source", "NYSE")
print(quotations)
quotations.setdefault("source", "LSE")
print(quotations)
print(quotations["source"])