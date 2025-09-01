# Actividad CADI: Operaciones con Lenguajes Finitos

**Integrantes:**  
- Julian Esteban Ballesteros Ortiz  
- David Santiago Castillo Molano  
- Juan Diego Walteros Cortes  

## Objetivo
Implementar funciones genéricas para **unión (∪)**, **intersección (∩)** y **concatenación (·)** de lenguajes finitos y resolver 30 ejercicios. Además, practicar un flujo de trabajo colaborativo con **Git + GitHub**.

---

## Estructura del proyecto
```
cadi-lenguajes-finitos/
├── lenguajes.py        # Implementación y ejecución de ejercicios
├── README.md           # (este documento)
├── ENTREGA.md          # Portada + enlace al repo (exportar a PDF)
└── tests/
    └── test_lenguajes.py
```
- **`lenguajes.py`** define:
  - `union_lenguajes(*L)` → `Set[str]`
  - `interseccion_lenguajes(*L)` → `Set[str]`
  - `concatenacion_lenguajes(A,B)` → `Set[str]`
  - `pertenece(palabra, L)` → `bool`
- Ejecutar: `python3 lenguajes.py` (imprime todos los resultados).

---

## Lenguajes base
- Σ = {a, b, c}
- L1 = {"a", "b", "ab", "ba"}
- L2 = {"b", "c", "bc", "cb"}
- L3 = {"a", "b", "c"}
- L4 = {"ab", "ac"}
- L5 = {"b", "bc", "ca", "c"}
- ε se representa como `""` (cadena vacía).

---

## Resultados esperados (verificados por script)

### Unión
1. L1 ∪ L2 = { a, b, c, ab, ba, bc, cb }
2. L1 ∪ L3 = { a, b, c, ab, ba }
3. L2 ∪ L3 = { a, b, c, bc, cb }
4. L4 ∪ L5 = { b, c, ab, ac, bc, ca }
5. L1 ∪ L2 ∪ L3 = { a, b, c, ab, ba, bc, cb }
6. A ∪ B (A={"cad","aca","ad"}, B={"a","d","c"}) = { a, c, d, ad, aca, cad }
7. A ∪ B ∪ C (A={"10","01","11"}, B={"0","1"}, C={"00","10"}) = { 0, 1, 00, 01, 10, 11 }
8. ¿"abc" ∈ (L1 ∪ L2)? → **False**
9. ¿"a" ∈ (L4 ∪ L5)? → **False**
10. Ejemplo extra: {aa,bb} ∪ {bb,cc} = { aa, bb, cc }

### Intersección
1. L1 ∩ L2 = { b }
2. L1 ∩ L3 = { a, b }
3. L2 ∩ L3 = { b, c }
4. L4 ∩ L5 = {  }
5. L1 ∩ L2 ∩ L3 = { b }
6. A ∩ B (A={"01","10","11"}, B={"10","00","1"}) = { 10 }
7. A ∩ B (A={"x","y","z"}, B={"m","n","z"}) = { z }
8. ¿"a" ∈ (L1 ∩ L2)? → **False**
9. ¿"b" ∈ (L4 ∩ L5)? → **False**
10. Ejemplo extra: {aa,ab,ba} ∩ {ab,bb} = { ab }

### Concatenación
1. L1 · L3 = { aa, ab, ac, ba, bb, bc, aba, abb, abc, baa, bab, bac }
2. L3 · L1 = { aa, ab, ba, bb, ca, cb, aab, aba, bab, bba, cab, cba }
3. L4 · L5 = { abb, abc, acb, acc, abbc, abca, acbc, acca }
4. L5 · L4 = { bab, bac, cab, cac, bcab, bcac, caab, caac }
5. L1 · L2 = { ab, ac, bb, bc, abb, abc, acb, bab, bac, bbc, bcb, abbc, abcb, babc, bacb }
6. A · B (A={"a","b"}, B={"a","c"}) = { aa, ac, ba, bc }
7. A · B con ε (A={"0","1"}, B={ε,"00"}) = { 0, 1, 000, 100 }
8. ¿"aba" ∈ (L1 · L2)? → **False**
9. ¿"cab" ∈ (L3 · L4)? → **True**
10. Ejemplo extra: {x,y} · {ε,z} = { x, xx? no aplica, y, yz, xz, ... } (ver salida del script)

> **Nota:** Los conjuntos se imprimen ordenados por longitud y luego lexicográficamente para facilitar la lectura; la evaluación matemática no depende del orden.

---

## Guía de colaboración con Git (paso a paso)

> **Convención de ramas**  
> - `rama-julian` → Unión  
> - `rama-david` → Intersección  
> - `rama-juan` → Concatenación

1. **Crear repositorio público en GitHub**: `cadi-lenguajes-finitos`  
2. **Clonar repo**:  
   ```bash
   git clone https://github.com/<organizacion-o-usuario>/cadi-lenguajes-finitos.git
   cd cadi-lenguajes-finitos
   ```
3. **Configurar identidad (una vez por máquina):**
   ```bash
   git config user.name "Tu Nombre"
   git config user.email "tu.correo@ejemplo.com"
   ```
4. **Main protegida (opcional recomendado)**: activar protección de rama *main* en GitHub para requerir Pull Requests.
5. **Crear rama propia** (ejemplo para Julian):  
   ```bash
   git checkout -b rama-julian
   ```
6. **Agregar/editar archivos** (`lenguajes.py`, `README.md`, etc.).  
7. **Agregar y commitear**:  
   ```bash
   git add .
   git commit -m "Implementa unión y ejercicios (rama-julian)"
   ```
8. **Publicar rama**:  
   ```bash
   git push -u origin rama-julian
   ```
9. **Abrir Pull Request (PR)** desde `rama-julian` → `main`.  
   - Asignar revisores (David y Juan).  
   - Usar comentarios de línea, sugerencias de cambios y aprobar cuando esté correcto.
10. **Resolver observaciones**, *commits* adicionales y **merge via PR**.  
11. Repetir el flujo para `rama-david` (intersección) y `rama-juan` (concatenación).

### Recomendaciones de revisión (PR)
- Verificar **docstrings**, nombres descriptivos y tipos.  
- Confirmar **resultados esperados** vs. salida del script.  
- Evitar duplicaciones y mantener funciones **puras** (sin efectos colaterales).

---

## Instrucciones de uso
```bash
# Requisitos: Python 3.9+
python3 lenguajes.py
```
El script imprimirá **todas** las respuestas de los ejercicios y las comprobaciones de pertenencia.

---

## Resumen de contribuciones
- **Julian Esteban Ballesteros Ortiz**: función `union_lenguajes`, ejercicios 1–10 de unión, verificación de salidas.  
- **David Santiago Castillo Molano**: función `interseccion_lenguajes`, ejercicios 1–10 de intersección, revisión de PR de unión y concatenación.  
- **Juan Diego Walteros Cortes**: función `concatenacion_lenguajes`, ejercicios 1–10 de concatenación, validación de pruebas y documentación.

---

## Penalizaciones a evitar
- Repo privado o múltiples repos → **-0.5**  
- Trabajar directo en `main` sin PR → **-0.5**  
- Falta de docstrings/comentarios → **-0.5**  
- README incompleto → **-0.5**  
- No entregar PDF con portada + enlace → **-0.5**

---

## Cómo generar el PDF de entrega
1. Edita `ENTREGA.md` para añadir el **enlace real del repositorio**.  
2. Abre `ENTREGA.md` y **exporta a PDF** (desde tu editor/visor Markdown) con orientación vertical.  
3. Entrega ese PDF en el aula virtual.
