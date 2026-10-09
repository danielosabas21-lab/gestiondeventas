# EMA MAYOREO WEB — despliegue seguro

Panel web de ventas de EMA MAYOREO. La aplicación necesita un servidor Python para que importaciones, pedidos, API e historial funcionen; GitHub Pages solo sirve archivos estáticos.

## Estado actual
El repositorio incluye configuración de despliegue para Render. Falta añadir el paquete limpio **EMA_MAYOREO_WEB_DEPLOY_SEGURO.zip** preparado en esta conversación a la raíz del repositorio. No publiques bases de datos, archivos Excel ni historiales comerciales.

## Publicación
1. Añade el ZIP limpio a la raíz del repositorio.
2. En Render, crea un servicio **Blueprint** y conecta este repositorio.
3. Render leerá `render.yaml`, instalará dependencias y preparará el paquete.
4. Consulta `EMA_ACCESS_PASSWORD` en Environment de Render y compártela solo con usuarios autorizados.
5. Verifica el servicio con un Excel de prueba. Comparte la URL `.onrender.com` cuando el estado aparezca como **Live**.

## Seguridad
No guardes secretos en Git. El paquete debe estar limpio de ventas reales. El disco persistente se monta en `/var/data` para conservar importaciones e historial entre reinicios.