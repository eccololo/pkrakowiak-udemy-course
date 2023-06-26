# Rozważmy dwukrotny rzut kostką.
# Zbuduj przestrzeń zdarzeń elementarnych omega,
# następnie policz prawdopodobieństwo uzyskania sumy
# oczek wyższej niż 10. W rozwiązaniu wykorzystaj
# zbiór składany (set comprehension).

omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
dice_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
print(f"P-stwo: {len(dice_gt_10) / len(omega):.2f}")
