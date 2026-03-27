# 🚀 Clase Master: Configuración de Antigravity para Data Science

Este documento detalla el flujo de trabajo profesional utilizando el stack moderno: **Poetry + Polars + Parquet**, optimizado para el entorno agéntico de **Antigravity**.

---

## 1. Conceptos Fundamentales de Antigravity

Antigravity es un **IDE Agéntico**. A diferencia de los editores tradicionales, tiene autonomía para interactuar con tu sistema de archivos, ejecutar comandos y razonar sobre el repositorio completo.

### 🧠 El Cerebro del Editor
*   **Rules (`.antigravityrules`):** Instrucciones pasivas. Es el "manual de conducta" que la IA consulta antes de cada respuesta. 
*   **Skills:** Instrucciones activas. Recetas de automatización que puedes invocar para tareas complejas (ej. "Prepara el entorno de producción").

---

## 2. 📊 Comparativa de Modelos y Planes (Ref. 2026)

Dependiendo de tu nivel de suscripción, tendrás acceso a diferentes capacidades de razonamiento y límites de contexto:

| Plan | Modelos Sugeridos | Capacidad de Contexto | Perfil de Uso |
| :--- | :--- | :--- | :--- |
| **FREE** | **GPT-4o mini**, Claude 3.5 Haiku | 128,000 tokens | Tareas rápidas, scripts unitarios y consultas de sintaxis. |
| **PLUS ($20/mo)** | **GPT-4o**, Claude 3.5 Sonnet | 200,000 tokens | Desarrollo de lógica compleja, ML avanzado y refactorización masiva. |
| **PRO ($200/mo)** | **OpenAI o1 (Pro)**, Claude 3.5 Opus | 2M+ tokens (Gemini) | Arquitecturas de sistemas, razonamiento lógico extremo y análisis de Big Data. |

> [!TIP]
> Para la mayoría de tareas de Data Science en este workshop, el nivel **Plus** con **Claude 3.5 Sonnet** ofrece el mejor balance entre velocidad y precisión en código Python.

---

## 3. Configuración Inicial del Proyecto

### Paso 1: Gestión de Dependencias con Poetry
En lugar de `pip`, usamos **Poetry** para garantizar que el ambiente sea determinístico.

```bash
# 1. Crear directorio y entrar
mkdir workshop_airbnb && cd workshop_airbnb

# 2. Inicializar Poetry
# Instalamos Polars para procesamiento, Pyarrow para Parquet y Scikit-learn para el modelo.
poetry init --name "data-science-airbnb" --dependency "polars" --dependency "pyarrow" --dependency "requests" --dependency "scikit-learn" --dependency "matplotlib" -n

# 3. Forzar el entorno virtual dentro de la carpeta
poetry config virtualenvs.in-project true
poetry install
```

### Paso 2: Estructura de Carpetas
Pide al chat de Antigravity (**Ctrl+L**):
> "Crea las carpetas data/raw, data/processed, notebooks, y src/models. Crea también un archivo README.md."

### Paso 3: Configurar el archivo `.antigravityrules`
Crea este archivo en la raíz para que la IA siga tus estándares:
```markdown
- Priorizar 'Polars' sobre 'Pandas'.
- Almacenamiento obligatorio en formato '.parquet'.
- Type Hinting obligatorio en todas las funciones.
- Documentación 'Google Style' en cada función.
- Usar siempre el entorno virtual de Poetry.
```

---

## 4. Pipeline de Datos: Ingesta y Limpieza

### Script de Ingesta (`src/ingestion.py`)
Utilizamos las capacidades nativas de Polars para manejar la conversión a Parquet eficientemente:

```python
import polars as pl
import requests
from pathlib import Path

def download_data(url: str, save_path: str) -> None:
    """Descarga un CSV y lo persiste como Parquet optimizado.
    
    Args:
        url: Dirección URL del archivo fuente.
        save_path: Ruta final del archivo .parquet.
    """
    print(f"Obteniendo datos de: {url}...")
    response = requests.get(url)
    
    temp_file = "temp_data.csv"
    with open(temp_file, "wb") as f:
        f.write(response.content)
    
    # Lectura con Polars y guardado en Parquet (más rápido y ligero)
    df = pl.read_csv(temp_file)
    df.write_parquet(save_path)
    
    # Limpiar archivo temporal
    Path(temp_file).unlink()
    print(f"✅ Archivo guardado en {save_path}")

if __name__ == "__main__":
    URL = "https://github.com/HarryVargas96/UdeCataluna/raw/refs/heads/main/data/airbnb.csv"
    download_data(URL, "data/raw/airbnb.parquet")
```

---

## 5. Modelamiento Agéntico

Usa el **Composer (Ctrl+I)** para orquestar los siguientes pasos de forma automática:

1.  **Limpieza:** *"Crea src/cleaning.py. Lee el parquet, elimina filas con precios nulos y asegúrate de que 'last_review' sea datetime."*
2.  **EDA:** *"Genera un Notebook en notebooks/ que use Seaborn para mostrar la distribución de precios por barrio."*
3.  **Modelo:** *"Entrena un Random Forest para predecir el precio. Evalúa con RMSE y guarda el modelo en src/models/model_v1.pkl."*

---

## 6. Control de Versiones (Git)

1.  **Generar .gitignore:** Pide al chat: *"Genera un .gitignore para Python que incluya .venv/, pycache/, y toda la carpeta data/"*.
2.  **Commit Inicial:**
    ```bash
    git init
    git add .
    git commit -m "feat: setup inicial, reglas de proyecto e ingesta airbnb"
    ```

---

> [!IMPORTANT]
> **Tip de Pro:** Si ocurre un error en la terminal, haz clic en el botón **"Debug with AI"**. Antigravity corregirá el código automáticamente siguiendo tus reglas definidas en `.antigravityrules`.
