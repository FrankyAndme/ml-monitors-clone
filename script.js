async function loadProducts() {
    try {
        const response = await fetch('http://localhost:8000/products');
        const products = await response.json();
        const grid = document.getElementById('product-grid');
        
        grid.innerHTML = products.map((product) => `
            <div class="product-card">
                <img src="${product.image}" alt="${product.title}" class="product-image">
                <div class="product-info">
                    <div class="product-price">$ ${product.price}</div>
                    <a href="detail.html?id=${product.id}" class="product-title">${product.title}</a>
                </div>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading products:', error);
    }
}

document.addEventListener('DOMContentLoaded', loadProducts);
