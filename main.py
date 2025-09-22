def syracuse(n: int) -> tuple[int, int, int]:
    """
    Calcule les métriques de la suite de Syracuse (Collatz) pour un entier n.

    Définitions:
    - Temps de vol (tv): nombre d'étapes pour atteindre 1.
    - Temps de vol en altitude (tva): nombre d'étapes où la valeur est strictement
      supérieure à n (le terme initial).
    - Altitude maximale (am): valeur maximale atteinte par la suite, n inclus.

    Args:
        n (int): entier strictement positif.

    Returns:
        tuple[int, int, int]: (tv, tva, am).

    Raises:
        ValueError: si n <= 0.
    """
    if n <= 0:
        raise ValueError("n doit être un entier strictement positif")

    u0: int = n
    u: int = n
    tv: int = 0
    tva: int = 0
    am: int = n

    while u != 1:
        # calcul du terme suivant
        if u % 2 == 0:
            u = u // 2
        else:
            u = 3 * u + 1

        # mise à jour des métriques
        tv += 1
        if u > u0:
            tva += 1
        if u > am:
            am = u

    return tv, tva, am

def main() -> None:
    n = 127
    tv, am, tva = syracuse(n)
    print(n, tv, am, tva)

    # Vérifications simples pour quelques valeurs
    for x in (3, 7, 15):
        print(x, "->", syracuse(x))

    # Maxima sur un intervalle (ex: 1..100)
    start, end = 1, 9999
    max_am = 0
    max_tv = 0
    max_tva = 0
    argmax_am = argmax_tv = argmax_tva = None

    for x in range(start, end + 1):
        tv, tva, am = syracuse(x)
        if am > max_am:
            max_am, argmax_am = am, x
        if tv > max_tv:
            max_tv, argmax_tv = tv, x
        if tva > max_tva:
            max_tva, argmax_tva = tva, x

    print(f"Max am sur [{start}, {end}] = {max_am} atteint pour n = {argmax_am}")
    print(f"Max tv sur [{start}, {end}] = {max_tv} atteint pour n = {argmax_tv}")
    print(f"Max tva sur [{start}, {end}] = {max_tva} atteint pour n = {argmax_tva}")


if __name__ == "__main__":
    main()