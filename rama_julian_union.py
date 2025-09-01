# ===================== Rama 1: Unión =====================
def ejercicios_union():
    imprimir_resultado("1) L1 ∪ L2", union_lenguajes(L1, L2))
    imprimir_resultado("2) L1 ∪ L3", union_lenguajes(L1, L3))
    imprimir_resultado("3) L2 ∪ L3", union_lenguajes(L2, L3))
    imprimir_resultado("4) L4 ∪ L5", union_lenguajes(L4, L5))
    imprimir_resultado("5) L1 ∪ L2 ∪ L3", union_lenguajes(L1, L2, L3))

    A6 = {"cad", "aca", "ad"}
    B6 = {"a", "d", "c"}
    imprimir_resultado("6) A ∪ B", union_lenguajes(A6, B6))

    A7 = {"10", "01", "11"}
    B7 = {"0", "1"}
    C7 = {"00", "10"}
    imprimir_resultado("7) A ∪ B ∪ C", union_lenguajes(A7, B7, C7))

    U12 = union_lenguajes(L1, L2)
    print(f"\n8) ¿\"abc\" ∈ (L1 ∪ L2)? -> {pertenece('abc', U12)}")

    U45 = union_lenguajes(L4, L5)
    print(f"9) ¿\"a\" ∈ (L4 ∪ L5)? -> {pertenece('a', U45)}")

    imprimir_resultado("10) Ejemplo extra unión: {aa, bb} ∪ {bb, cc}",
                       union_lenguajes({'aa','bb'},{'bb','cc'}))
