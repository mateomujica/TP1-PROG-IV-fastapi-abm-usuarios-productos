# TP1 - ABM de Usuarios y Productos con FastAPI

Proyecto para el Trabajo Práctico 1: ABM completo de usuarios y ABM de una
entidad propia (Producto), usando **FastAPI** y **Pydantic**.

## Crear el entorno virtual (venv)

Desde esta carpeta (`clase-fastapi`):

```bash
python -m venv .venv
```

Activar el entorno virtual:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

## Instalar los requerimientos

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
fastapi dev main.py
```

La API quedará disponible en `http://127.0.0.1:8000` y la documentación
interactiva (Swagger) en `http://127.0.0.1:8000/docs`, donde se pueden
probar todos los endpoints.

## Endpoints disponibles

### Usuarios (`/user`)

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/user` | Lista usuarios. Acepta filtro opcional `?is_active=true/false` |
| POST | `/user` | Crea un usuario |
| PUT | `/user/{id}` | Modifica un usuario existente |
| DELETE | `/user/{id}` | Elimina un usuario |

### Productos (`/producto`)

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/producto` | Lista productos. Acepta filtro opcional `?categoria=Tecnología` |
| GET | `/producto/{id}` | Obtiene un producto por id |
| POST | `/producto` | Crea un producto |
| PUT | `/producto/{id}` | Modifica un producto existente |
| DELETE | `/producto/{id}` | Elimina un producto |

Los datos se almacenan en memoria (se pierden al reiniciar el servidor).
Ambas entidades vienen con algunos registros de ejemplo cargados al
arrancar la aplicación, para poder probar los endpoints sin necesidad de
crear datos primero.

## Lint y chequeo de tipos

El proyecto incluye configuración local para dos herramientas:

- **[`setup.cfg`](./setup.cfg)**: configuración de [`pycodestyle`](https://pycodestyle.pycqa.org/) (chequeo de estilo PEP 8). Define `max-line-length = 79` y excluye `.venv` y `__pycache__` del análisis.
- **[`pyrightconfig.json`](./pyrightconfig.json)**: configuración de [`pyright`](https://microsoft.github.io/pyright/) (chequeo de tipos). Apunta al entorno virtual local (`.venv`) para resolver las dependencias instaladas y excluye `.venv` y `__pycache__`.

`pyright` ya está incluido en `requirements.txt`. `pycodestyle` no, así que hay que instalarlo aparte.

Con el entorno virtual activado, correr:

```bash
pip install pycodestyle
python -m pycodestyle .
```

```bash
pyright
```