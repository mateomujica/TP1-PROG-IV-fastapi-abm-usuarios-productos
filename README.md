# TP1 - ABM de Usuarios y Productos con FastAPI

Proyecto para el Trabajo Práctico 1: ABM completo de usuarios y ABM de una
entidad propia (Producto), usando FastAPI y Pydantic.

Este README explica paso a paso cómo ejecutar la aplicación en una máquina
local (instrucciones explícitas para Windows y para macOS/Linux).

---

## Estructura

La aplicación principal está dentro de la carpeta `clase-fastapi`.

- `clase-fastapi/main.py` — punto de entrada (FastAPI app)
- `clase-fastapi/routers/` — routers para usuarios y productos
- `clase-fastapi/models/` — modelos Pydantic
- `clase-fastapi/requirements.txt` — dependencias

---

## Requisitos previos

- Python 3.8+ instalado (se probó con 3.13 en el entorno de desarrollo).
- Recomendado: usar un virtualenv para instalar dependencias sin afectar
  el sistema.

---

## Pasos para ejecutar (forma recomendada)

Abrir una terminal y situarse en la carpeta raíz del proyecto, luego entrar
en la carpeta de la aplicación:

```bash
cd clase-fastapi
```

Crear y activar un virtualenv:

```bash
# Crear (se crea la carpeta .venv dentro de clase-fastapi)
python -m venv .venv

# Activar (PowerShell)
.venv\Scripts\Activate.ps1

# O en CMD (Windows)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

Actualizar pip (opcional pero recomendado):

```bash
python -m pip install --upgrade pip
```

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Iniciar la aplicación con Uvicorn (comando recomendado):

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

- Para desarrollo con recarga automática, agregar `--reload`.
- Si el equipo no tiene `uvicorn` instalado global, se usará el del
  virtualenv (es lo recomendado).

Alternativa (si está disponible):

```bash
# si tienen instalado fastapi-cli
fastapi dev main.py
```

---

## URLs útiles

- API: http://127.0.0.1:8000
- Swagger / OpenAPI (interactivo): http://127.0.0.1:8000/docs
- Esquema OpenAPI JSON: http://127.0.0.1:8000/openapi.json

---

## Endpoints disponibles (resumen)

Usuarios (`/user`):

- GET /user — lista usuarios (opcional: `?is_active=true/false`)
- POST /user — crea un usuario
- PUT /user/{id} — actualiza un usuario
- DELETE /user/{id} — elimina un usuario

Productos (`/producto`):

- GET /producto — lista productos (opcional: `?categoria=<nombre>`)
- GET /producto/{id} — obtiene producto por id
- POST /producto — crea un producto
- PUT /producto/{id} — actualiza un producto
- DELETE /producto/{id} — elimina un producto

Nota: los datos se almacenan en memoria (no hay persistencia). Al reiniciar
el servidor se pierden los cambios. Hay datos de ejemplo cargados al iniciar
la app para facilitar las pruebas.

---

## Lint y chequeo de tipos (opcional)

El repositorio incluye:

- `setup.cfg` — configuración para pycodestyle (PEP 8)
- `pyrightconfig.json` — configuración para pyright (chequeo de tipos)

Comandos sugeridos (con el virtualenv activado):

```bash
python -m pip install pycodestyle
python -m pycodestyle .

# pyright (ya se incluye en requirements.txt)
pyright
```

---

## Solución de problemas comunes

- "Address already in use" al iniciar uvicorn: el puerto 8000 ya está ocupado.
  Usar otro puerto, por ejemplo `--port 8001`.
- Error de import cuando se ejecuta `main:app`: asegurarse de estar en la
  carpeta `clase-fastapi` antes de ejecutar uvicorn.
- Si faltan paquetes, volver a ejecutar `python -m pip install -r
  requirements.txt` dentro del virtualenv.
