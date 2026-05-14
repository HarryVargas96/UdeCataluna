import os
import sys
import subprocess
import platform

def print_step(message):
    print(f"\n[STEP] {message}...")

def check_python():
    print_step("Verificando versión de Python")
    version = sys.version.split()[0]
    print(f"Detectado: Python {version} en {platform.system()}")
    return True

def create_venv():
    print_step("Creando ambiente virtual (.venv)")
    if os.path.exists(".venv"):
        print("El ambiente virtual ya existe. Saltando paso.")
        return
    
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("Ambiente virtual creado exitosamente.")
    except Exception as e:
        print(f"Error creando venv: {e}")
        sys.exit(1)

def install_libraries():
    print_step("Instalando librerías (Pandas, NumPy, Scikit-Learn)")
    
    # Determinar el ejecutable de python según el OS
    if platform.system() == "Windows":
        python_path = os.path.join(".venv", "Scripts", "python.exe")
    else:
        python_path = os.path.join(".venv", "bin", "python")

    libs = ["pandas", "numpy", "scikit-learn", "matplotlib", "seaborn", "pyarrow", "fastparquet"]
    
    try:
        print("Actualizando pip...")
        subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        print("Instalando librerías base...")
        subprocess.run([python_path, "-m", "pip", "install"] + libs, check=True)
        print(f"Librerías instaladas: {', '.join(libs)}")
    except Exception as e:
        print(f"Error instalando librerías: {e}")
        sys.exit(1)

def generate_requirements():
    print_step("Generando archivo de reproducibilidad (requirements.txt)")
    
    if platform.system() == "Windows":
        python_path = os.path.join(".venv", "Scripts", "python.exe")
    else:
        python_path = os.path.join(".venv", "bin", "python")
    
    try:
        # Usamos pip freeze para capturar las versiones exactas instaladas
        with open("requirements.txt", "w") as f:
            subprocess.run([python_path, "-m", "pip", "freeze"], stdout=f, check=True)
        print("Archivo requirements.txt generado con éxito.")
    except Exception as e:
        print(f"Error generando requirements.txt: {e}")

def create_folders():
    print_step("Creando estructura de carpetas")
    folders = [
        "data/raw",
        "data/processed",
        "src",
        "notebooks",
        "reports/figures"
    ]
    
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Creada: {folder}")
        else:
            print(f"Ya existe: {folder}")

def main():
    print("=== INICIANDO CONFIGURACIÓN DEL TALLER ===")
    
    if check_python():
        create_venv()
        install_libraries()
        generate_requirements()
        create_folders()
        
    print("\n=== ¡CONFIGURACIÓN COMPLETADA CON ÉXITO! ===")
    print("Ya puedes empezar a trabajar en tus notebooks.")

if __name__ == "__main__":
    main()
