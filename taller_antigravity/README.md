# 🐍 Taller de Agentes: Setup de Ciencia de Datos

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Ready_to_Start-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OS-Windows_/_macOS-orange?style=for-the-badge" />
</div>

---

## 🚀 Bienvenido al Taller
¡Felicidades por dar el primer paso! Este entorno ha sido diseñado para que te enfoques en los datos, mientras tu **Agente de IA** se encarga de la configuración técnica por ti.

### 🛠️ ¿Qué vamos a configurar?
El agente realizará automáticamente las siguientes tareas:
1. **Verificación de Salud:** Asegurarse de que Python esté listo en tu equipo.
2. **Entorno de Trabajo:** Crear un "espacio aislado" (ambiente virtual) para que nada se rompa.
3. **Instalación de Librerías:** Preparar las herramientas de análisis:
   - `Pandas` (Para manipular tablas).
   - `NumPy` (Para cálculos matemáticos).
   - `Scikit-Learn` (Para modelos de IA).
4. **Reproducibilidad:** Generar un archivo `requirements.txt` con las versiones exactas para que tu trabajo sea replicable.
5. **Arquitectura de Carpetas:** Organizar tu proyecto como un profesional.

---

## 📂 Estructura del Proyecto
Una vez configurado, verás estas carpetas:

| Carpeta | Propósito |
| :--- | :--- |
| `data/` | Tus archivos CSV, Excel o bases de datos. |
| `notebooks/` | Tus laboratorios de experimentación (.ipynb). |
| `src/` | Código fuente y scripts reutilizables. |
| `reports/` | Gráficos y resultados finales. |
| `requirements.txt` | Lista de librerías y sus versiones exactas. |

---

## 🏁 Cómo Empezar
No necesitas abrir la terminal. Simplemente escribe en el chat:

> **"Antigravity, configura mi proyecto"**

---
<p align="center">
  <i>"La mejor forma de predecir el futuro es creándolo con datos."</i>
</p>


## 🧪 Laboratorio 1: Carga de Datos ICFES
Una vez configurado el proyecto, puedes iniciar tu primer análisis. 

**Datos:** `icfes_2022_filtered.parquet`
**URL:** `https://github.com/HarryVargas96/UdeCataluna/raw/refs/heads/main/data/icfes_2022_filtered.parquet`

### Instrucciones para el Estudiante:
Pídele a tu agente: *"Ayúdame a crear un notebook para leer los datos del ICFES"* y él te guiará paso a paso con este código base:

```python
import pandas as pd
df = pd.read_parquet("URL_DEL_DATASET")
```

