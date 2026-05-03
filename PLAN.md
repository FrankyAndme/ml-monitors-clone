# Proyecto ML-Clone: Monitores LED

## 🎯 Objetivo
Crear una réplica visual de 10 artículos de monitores LED de Mercado Libre, evolucionando desde datos estáticos hasta un sistema dinámico con base de datos.

## 🛠️ Stack Tecnológico
- **Scraping:** Python + Playwright / BeautifulSoup
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **Control de Versiones:** GitHub (Repo: `ml-monitors-clone`)
- **Base de Datos:** MongoDB (NoSQL para esquemas flexibles)

## 🚀 Hoja de Ruta

### Fase 1: Extracción de Datos (Scraping)
- [ ] Tarea 1.1: Identificar URL de la categoría "Monitores LED".
- [ ] Tarea 1.2: Script de scraping (Título, Precio, Imagen, Descripción, Calificación) para 10 artículos.
- [ ] Tarea 1.3: Generar `products.json`.
- **Entregable:** Script + JSON.

### Fase 2: Desarrollo del Frontend (Hardcoded)
- [ ] Tarea 2.1: Estructura HTML de listado (estilo ML).
- [ ] Tarea 2.2: CSS profesional y Responsive.
- [ ] Tarea 2.3: Vista de Detalle del Producto.
- **Entregable:** Prototipo HTML/CSS estático.

### Fase 3: Integración de Datos Estáticos
- [ ] Tarea 3.1: JS para renderizar `products.json` en el HTML.
- [ ] Tarea 3.2: Navegación dinámica Listado $\rightarrow$ Detalle.
- **Entregable:** Web funcional con datos reales extraídos.

### Fase 4: Implementación de Base de Datos
- [ ] Tarea 4.1: Configurar MongoDB.
- [ ] Tarea 4.2: Migración JSON $\rightarrow$ MongoDB.
- [ ] Tarea 4.3: API (Node.js/Express o Python/FastAPI).
- **Entregable:** Aplicación Full-Stack.
