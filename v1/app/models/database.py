from v1.app.extension import db

"""
    User - for customers
    Product - for product details
    Category - categorize product
    Oder - customer orders
    Order item - items in order
    Payment - tracks Payments
    Review - reviews made
"""
class User(db.Models):
    """User data"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(15), default="customer")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    order = db.relationship("Order", bakref="customer", lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"

class Product(db.Models):
    __tablename__ = 'products'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Texet, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    images = db.Column(db.LargeBinary, nullable=False)

    category = db.relationship("Catedory", backref="products")

    def __repr__(self):
        return f"<Product {self.name}>"

class Category(db.Models):
    __teblename__ = 'caregories'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"
    
class Order(db.Models):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    user_id = id = db.Column(db.Intger, db.ForeignKey("user_id"), nullable=False)
    status = db.Column(db.String(20), default="pending") # shipping, delivered, ready for pickup
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    order_items = db.relationship("OrderItem", backref="order", lazy=True)

    def __repr__(self):
        return f"<Order {self.id} - Status {self.status}>"
    
class OrderItem(db.Model):
    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    product = db.relationship("Product", backref="order_items")

    def __repr__(self):
        return f"<OrderItem: {self.order_id} Product: {self.product_id}>"

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(20), nullable=False, default="waiting")
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", backref="payment")

    def __repr__(self):
        return f"<Payment {self.tansaction_id} Amount: {self.amount} Status: {self.payment_status}>"
    
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    rating = quantity = db.Column(db.Integer, nullable=False) # rating 1-5
    comment = quantity = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    user = db.relationship("User", backref="reviews")
    product = db.relationship("Product", backref="reviews")

    def __repr__(self):
        return f"<Reviews {self.product_id} Rating {self.rating}>"