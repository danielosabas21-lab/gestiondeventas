# EMA MAYOREO WEB — despliegue seguro

Panel web de EMA MAYOREO con interfaz, API, importación de Excel e historial.

## Despliegue configurado
Este proyecto requiere servidor Python. GitHub Pages por sí solo **no** ejecuta el backend. El archivo `render.yaml` configura un servicio web de Render con contraseña y disco persistente.

1. En Render, inicia sesión y elige **New → Blueprint**.
2. Conecta este repositorio: `danielosabas21-lab/gestiondeventas`.
3. Render leerá `render.yaml`, validará el paquete ZIP, instalará dependencias y arrancará el servidor.
4. Espera a que el servicio muestre **Live**. La URL pública será la que Render asigne al servicio.
5. En Render → Environment, consulta `EMA_ACCESS_USER` y `EMA_ACCESS_PASSWORD`. No compartas la contraseña públicamente.

## Datos y seguridad
- El paquete subido está sanitizado: no incluye el Excel original ni la base histórica de ventas.
- La aplicación inicia con datos vacíos. Importa primero un Excel de prueba y comprueba que el historial persiste tras reiniciar.
- El servicio requiere almacenamiento persistente; el plan Starter puede generar cargos.
- Mantén los datos reales de ventas fuera de GitHub y comparte el panel solo con usuarios autorizados.

## Archivos
- `EMA_MAYOREO_WEB_LISTO_PARA_SUBIR.zip`: código de la aplicación, interfaz y datos iniciales vacíos.
- `prepare_app.py`: valida y extrae el paquete sin permitir rutas inseguras ni archivos de datos sensibles.
- `render.yaml`: servicio Python con autenticación y disco persistente.
