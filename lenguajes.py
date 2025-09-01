#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actividad CADI: Operaciones con Lenguajes Finitos
-------------------------------------------------
Funciones genéricas (unión, intersección, concatenación) y resolución automática
de los 30 ejercicios solicitados.

Ejecución:
    python3 lenguajes.py

Salida:
    Imprime todos los resultados de los ejercicios (conjuntos ordenados) y
    las comprobaciones de pertenencia solicitadas.

Autoría (equipo):
    - Julian Esteban Ballesteros Ortiz
    - David Santiago Castillo Molano
    - Juan Diego Walteros Cortes
"""
from __future__ import annotations
from typing import Iterable, Set, Tuple, List

# ============================ Definiciones base ============================

Sigma: Set[str] = {"a", "b", "c"}  # Alfabeto base para L1..L5

L1: Set[str] = {"a", "b", "ab", "ba"}
L2: Set[str] = {"b", "c", "bc", "cb"}
L3: Set[str] = {"a", "b", "c"}
L4: Set[str] = {"ab", "ac"}
L5: Set[str] = {"b", "bc", "ca", "c"}

# Nota sobre epsilon: representamos la cadena vacía como "" (string vacío).
EPSILON = ""

# ============================= Funciones core ==============================

def union_lenguajes(*lenguajes: Iterable[str]) -> Set[str]:
    """
    Calcula la unión finita de 2 o más lenguajes.

    Args:
        *lenguajes: Secuencia de conjuntos/iterables de palabras (str).

    Returns:
        Conjunto con todas las palabras que aparecen en al menos uno de los lenguajes.
    """
    U: Set[str] = set()
    for L in lenguajes:
        U |= set(L)
    return U


def interseccion_lenguajes(*lenguajes: Iterable[str]) -> Set[str]:
    """
    Calcula la intersección finita de 2 o más lenguajes.

    Args:
        *lenguajes: Secuencia de conjuntos/iterables de palabras (str).

    Returns:
        Conjunto con las palabras comunes a todos los lenguajes.
    """
    if not lenguajes:
        return set()
    I: Set[str] = set(lenguajes[0])
    for L in lenguajes[1:]:
        I &= set(L)
    return I


def concatenacion_lenguajes(A: Iterable[str], B: Iterable[str]) -> Set[str]:
    """
    Concatenación de dos lenguajes finitos:
        A · B = { x + y | x ∈ A, y ∈ B }

    Reglas con epsilon (cadena vacía):
        - "" + y = y
        - x + "" = x

    Args:
        A: Lenguaje izquierdo (iterable de str).
        B: Lenguaje derecho (iterable de str).

    Returns:
        Conjunto con todas las concatenaciones posibles.
    """
    A = set(A)
    B = set(B)
    return {x + y for x in A for y in B}


def pertenece(palabra: str, L: Iterable[str]) -> bool:
    """Comprueba pertenencia exacta de una palabra a un lenguaje finito."""
    return palabra in set(L)


def ordenado(L: Iterable[str]) -> List[str]:
    """
    Devuelve una lista ordenada lexicográficamente para impresión estable.
    Nota: se ordena por longitud y luego léxico, para mayor legibilidad.
    """
    return sorted(set(L), key=lambda s: (len(s), s))


# ======================= Ejercicios (salidas impresas) =====================

def imprimir_resultado(titulo: str, L: Iterable[str]) -> None:
    print(f"\n== {titulo} ==")
    print("{ " + ", ".join(ordenado(L)) + " }")


def main() -> None:
    # ---------------- Rama 1: Unión ----------------
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

    # ------------- Rama 2: Intersección -------------
    imprimir_resultado("1) L1 ∩ L2", interseccion_lenguajes(L1, L2))
    imprimir_resultado("2) L1 ∩ L3", interseccion_lenguajes(L1, L3))
    imprimir_resultado("3) L2 ∩ L3", interseccion_lenguajes(L2, L3))
    imprimir_resultado("4) L4 ∩ L5", interseccion_lenguajes(L4, L5))
    imprimir_resultado("5) L1 ∩ L2 ∩ L3", interseccion_lenguajes(L1, L2, L3))

    A6i = {"01", "10", "11"}
    B6i = {"10", "00", "1"}
    imprimir_resultado("6) A ∩ B", interseccion_lenguajes(A6i, B6i))

    A7i = {"x", "y", "z"}
    B7i = {"m", "n", "z"}
    imprimir_resultado("7) A ∩ B", interseccion_lenguajes(A7i, B7i))

    I12 = interseccion_lenguajes(L1, L2)
    print(f"\n8) ¿\"a\" ∈ (L1 ∩ L2)? -> {pertenece('a', I12)}")

    I45 = interseccion_lenguajes(L4, L5)
    print(f"9) ¿\"b\" ∈ (L4 ∩ L5)? -> {pertenece('b', I45)}")

    imprimir_resultado("10) Ejemplo extra intersección: {aa,ab,ba} ∩ {ab,bb}",
                       interseccion_lenguajes({'aa','ab','ba'},{'ab','bb'}))

    # ----------- Rama 3: Concatenación -----------
    imprimir_resultado("1) L1 · L3", concatenacion_lenguajes(L1, L3))
    imprimir_resultado("2) L3 · L1", concatenacion_lenguajes(L3, L1))
    imprimir_resultado("3) L4 · L5", concatenacion_lenguajes(L4, L5))
    imprimir_resultado("4) L5 · L4", concatenacion_lenguajes(L5, L4))
    imprimir_resultado("5) L1 · L2", concatenacion_lenguajes(L1, L2))

    A6c = {"a", "b"}
    B6c = {"a", "c"}
    imprimir_resultado("6) A · B", concatenacion_lenguajes(A6c, B6c))

    A7c = {"0", "1"}
    B7c = {EPSILON, "00"}  # epsilon representado como cadena vacía
    imprimir_resultado("7) A · B (con ε)", concatenacion_lenguajes(A7c, B7c))

    C12 = concatenacion_lenguajes(L1, L2)
    print(f"\n8) ¿\"aba\" ∈ (L1 · L2)? -> {pertenece('aba', C12)}")

    C34 = concatenacion_lenguajes(L3, L4)
    print(f"9) ¿\"cab\" ∈ (L3 · L4)? -> {pertenece('cab', C34)}")

    imprimir_resultado("10) Ejemplo extra concatenación: {x,y} · {ε,z}",
                       concatenacion_lenguajes({'x','y'}, {EPSILON,'z'}))


if __name__ == "__main__":
    main()
