async function loadProductDetail() {
    try {
        const params = new URLSearchParams(window.location.search);
        const productId = params.get('id');
        
        if (!productId) {
            document.getElementById('product-detail').innerHTML = '<p>Producto no encontrado.</p>';
            return;
        }

        const response = await fetch('products.json');
        const products = await response.json();
        const product = products[productId];

        if (!product) {
            document.getElementById('product-detail').innerHTML = '<p>Producto no encontrado.</p>';
            return;
        }

        const detailDiv = document.getElementById('product-detail');
        detailDiv.innerHTML = `
            <div class="detail-content">
                <img src="${product.image}" alt="${product.title}" class="detail-image">
                <div class="detail-info">
                    <h1>${product.title}</h1>
                    <div class="detail-price">$ ${product.price}</div>
                    <p class="detail-description">Descripción detallada del monitor LED. Este producto cuenta con las mejores especificaciones del mercado, ideal para gaming y productividad.</p>
                    <button class="buy-button">Comprar ahora</button>
                </div>
            </div>
        `;
    } catch (error) {
        console.error('Error loading product detail:', error);
        document.getElementById('product-detail').innerHTML = '<p>Error al cargar el producto.</p>';
    }
}

document.addEventListener('DOMContentLoaded', loadProductDetail);
