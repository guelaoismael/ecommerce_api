# E-commerce Product API

The **E-commerce Product API** is a Django-based application designed to handle core e-commerce functionalities such as user management, product catalog, wishlist operations, discount management, and order processing.

---

## Project Structure

The project has the following main directories:

- `discounts`: Manage discounts and promotional offers.
- `media`: Handle file uploads and media management.
- `orders`: Manage customer orders.
- `products`: Manage product catalog and inventory.
- `user`: Manage user accounts and authentication.
- `wishlists`: Handle user wishlists and saved items.

---

## Quick Start

1. Add `ecommerce_api` to your `INSTALLED_APPS` setting in `settings.py` like this:

   ```python
   INSTALLED_APPS = [
       ...,
       "ecommerce_api",
   ]
   ```

2. Include the `ecommerce_api` URLconf in your project's `urls.py` file:

   ```python
   from django.urls import path, include

   urlpatterns = [
       ...,
       path("api/", include("ecommerce_api.urls")),
   ]
   ```

3. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Use an API client such as Postman or cURL to test the available endpoints:

   ### User Endpoints

   - **User Registration:** `POST /api/users/register/`
   - **Token Retrieval:** `POST /api/users/token/`
   - **Token Refresh:** `POST /api/users/token/refresh/`

   ### Product Endpoints

   - **Product Management:** `GET/POST/PUT/DELETE /api/products/`
   - **Add Review:** `POST /api/products/<int:pk>/reviews/new/`
   - **Product Reviews:** `GET /api/products/<int:pk>/reviews/`

   ### Review Endpoints

   - **Review List:** `GET /api/reviews/`
   - **Review Detail:** `GET/PUT/DELETE /api/reviews/<int:pk>/`

   ### Wishlist Endpoints

   - **Add to Wishlist:** `POST /api/products/<int:pk>/wishlists/add/`
   - **Wishlist Management:** `GET /api/wishlists/`
   - **Wishlist Detail:** `GET/PUT/DELETE /api/wishlists/<int:pk>/`

   ### Order Endpoints

   - **Order Processing:** `GET/POST /api/orders/`

   ### Discount Endpoints

   - **Discount Management:** `GET/POST/PUT/DELETE /api/discounts/`

   ### Category Endpoints

   - **Category Management:** `GET/POST/PUT/DELETE /api/categories/`

6. Access the Django Admin panel to manage database entities:

   - URL: `http://127.0.0.1:8000/admin/`

---

## Usage

Utilize the API endpoints to perform various operations within the e-commerce platform, such as managing users, products, categories, wishlists, discounts, and orders.
