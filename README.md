# 🚢 Hundir la flota

Proyecto individual del bootcamp de Data Science de **The Bridge** (octubre 2026).
El clásico juego de *Hundir la flota* en la terminal, escrito en **Python** con **NumPy**: tú contra un **algoritmo** que, cuando toca uno de tus barcos, sigue disparando a su alrededor hasta hundirlo.

---

## ▶️ Cómo jugar

**Requisitos:** Python 3 y NumPy.

```bash
git clone https://github.com/claudia30aiabuser/flota-The-Bridge-Alesia-Navumenka-.git
cd flota-The-Bridge-Alesia-Navumenka-
pip install numpy
python main.py
```

Al empezar, el juego te hace dos preguntas:

| Pregunta | Qué escribir |
|---|---|
| tamaño del tablero | el número de filas (= columnas), por ejemplo `10` |
| esloras de los barcos | `0` para la **flota clásica** (4, 3, 3, 2, 2, 2, 1, 1, 1, 1), o las esloras que quieras, por ejemplo `4,3,2,1` (como máximo 4) |

Después, en cada turno escribes tu disparo como **`fila, columna`**, por ejemplo `3,7`. También vale separarlo con espacio, punto o punto y coma: `3 7`, `3.7`, `3;7`.

### Reglas

- Gana quien hunde primero **todos** los barcos del rival.
- Si **tocas** o **hundes** un barco, vuelves a disparar. Si das en el **agua**, le toca al otro.
- Los barcos nunca se tocan: alrededor de cada uno siempre hay agua.
- Cuando hundes un barco, el agua que lo rodea se descubre automáticamente.

### Símbolos del tablero

| Símbolo | Significado |
|---|---|
| `■` | barco |
| `~` | agua junto a un barco |
| `X` | tocado |
| `A` | agua (disparo fallado) |
| `.` | casilla sin disparar |
