# 🍷 TP Final - API REST para Gestión de Vinoteca

Trabajo Final de la materia **Programación II**  
Tecnicatura Universitaria en Desarrollo Web – Universidad Nacional de Entre Ríos

Este proyecto implementa una **API REST** para gestionar la información de una vinoteca, incluyendo vinos, bodegas y cepas.  
El backend está desarrollado en **Python** utilizando **Flask** y **Flask-RESTful**.

---

## 🔧 Funcionalidades de la API

- 📚 Obtener listado completo de vinos, bodegas y cepas.
- 🔍 Consultar un vino, bodega o cepa por su ID.
- 🔗 Consultas relacionadas:
  - Vinos de una bodega
  - Cepas de una bodega
  - Vinos de una cepa
  - Bodega de un vino
  - Cepas de un vino

---

## 🚀 Cómo ejecutar la API

# Clonar el repositorio y moverse a la carpeta del proyecto
git clone https://github.com/guardiasofia/TP-Vinoteca.git
cd TP-Vinoteca/TP-Final-vinoteca

# (Opcional) Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias necesarias
pip install flask flask-restful

# Ejecutar la API
python main.py

