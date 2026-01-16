"""
Database initialization script for Restaurant POS System
Run this once to create the database and populate with sample data
"""

import sqlite3
import os
from datetime import datetime

# Database path
DB_DIR = "database"
DB_PATH = os.path.join(DB_DIR, "cafe_pos.db")

def create_database():
    """Create database and tables"""
    
    # Ensure database directory exists
    os.makedirs(DB_DIR, exist_ok=True)
    
    # Connect to database (creates file if doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("Creating tables...")
    
    # Create categories table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name VARCHAR(50) NOT NULL UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create menu_items table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name VARCHAR(100) NOT NULL,
            category_id INTEGER NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            description TEXT,
            stock_quantity INTEGER DEFAULT 0,
            is_available BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    """)


    # Create orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number VARCHAR(20) UNIQUE NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total_amount DECIMAL(10, 2) NOT NULL,
            payment_method VARCHAR(20),
            status VARCHAR(20) DEFAULT 'completed',
            customer_name VARCHAR(100),
            notes TEXT
        )
    """)


    # Create order_items table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price DECIMAL(10, 2) NOT NULL,
            subtotal DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
        )
    """)

    # Create indexes for better performance
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_menu_items_category ON menu_items(category_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id)")
    
    conn.commit()
    print("✓ Tables created successfully")
    
    return conn, cursor

def seed_sample_data(cursor, conn):
    """Insert sample data for testing"""
    
    print("\nInserting sample data...")
    
    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM categories")
    if cursor.fetchone()[0] > 0:
        print("⚠ Sample data already exists. Skipping seed.")
        return
    
    # Insert categories
    categories = [
        ('Appetizers', 'Starters and small bites'),
        ('Main Course', 'Main dishes and meals'),
        ('Beverages', 'Hot and cold drinks'),
        ('Desserts', 'Sweet treats and desserts')
    ]

    cursor.executemany(
        "INSERT INTO categories (category_name, description) VALUES (?, ?)",
        categories
    )
    print("✓ Categories inserted")
    
    # Insert menu items
    menu_items = [
        # Appetizers (category_id = 1)
        ('Spring Rolls', 1, 12.50, 'Crispy vegetable spring rolls', 50, 1),
        ('Chicken Wings', 1, 18.00, 'Spicy buffalo wings with blue cheese', 40, 1),
        ('Garlic Bread', 1, 8.00, 'Toasted bread with garlic butter', 60, 1),
        ('Soup of the Day', 1, 10.00, 'Chef special soup', 30, 1),
        
        # Main Course (category_id = 2)
        ('Nasi Lemak', 2, 15.00, 'Traditional Malaysian rice dish with sambal', 30, 1),
        ('Grilled Chicken', 2, 25.00, 'Marinated grilled chicken with vegetables', 25, 1),
        ('Beef Rendang', 2, 28.00, 'Slow-cooked beef in coconut curry', 20, 1),
        ('Fish & Chips', 2, 22.00, 'Crispy battered fish with fries', 35, 1),
        ('Vegetarian Pasta', 2, 20.00, 'Pasta with seasonal vegetables', 40, 1),
        
        # Beverages (category_id = 3)
        ('Teh Tarik', 3, 4.50, 'Malaysian pulled milk tea', 100, 1),
        ('Iced Coffee', 3, 6.00, 'Cold brew coffee with ice', 100, 1),
        ('Fresh Orange Juice', 3, 8.00, 'Freshly squeezed orange juice', 50, 1),
        ('Soft Drinks', 3, 3.50, 'Assorted carbonated drinks', 120, 1),
        ('Mineral Water', 3, 2.50, 'Bottled water', 150, 1),
        
        # Desserts (category_id = 4)
        ('Ice Cream', 4, 8.00, 'Vanilla ice cream with toppings', 25, 1),
        ('Chocolate Cake', 4, 12.00, 'Rich chocolate fudge cake', 15, 1),
        ('Fruit Salad', 4, 9.00, 'Fresh seasonal fruits', 20, 1),
        ('Creme Brulee', 4, 14.00, 'Classic French custard dessert', 10, 1)
    ]

    cursor.executemany(
        """INSERT INTO menu_items 
           (item_name, category_id, price, description, stock_quantity, is_available) 
           VALUES (?, ?, ?, ?, ?, ?)""",
        menu_items
    )
    print("✓ Menu items inserted")
    
    # Insert sample order
    order_number = f"ORD-{datetime.now().strftime('%Y%m%d')}-001"
    cursor.execute(
        """INSERT INTO orders 
           (order_number, total_amount, payment_method, customer_name) 
           VALUES (?, ?, ?, ?)""",
        (order_number, 47.50, 'Cash', 'Walk-in Customer')
    )
    order_id = cursor.lastrowid
    
    # Insert order items for the sample order
    order_items = [
        (order_id, 1, 2, 12.50, 25.00),  # 2x Spring Rolls
        (order_id, 5, 1, 15.00, 15.00),  # 1x Nasi Lemak
        (order_id, 10, 1, 4.50, 4.50),   # 1x Teh Tarik
        (order_id, 14, 1, 3.00, 3.00)    # 1x Soft Drink
    ]
    
    cursor.executemany(
        """INSERT INTO order_items 
           (order_id, item_id, quantity, unit_price, subtotal) 
           VALUES (?, ?, ?, ?, ?)""",
        order_items
    )
    print("✓ Sample order inserted")
    
    conn.commit()
    print("\n✅ Database initialized successfully!")
    print(f"📁 Database location: {os.path.abspath(DB_PATH)}")

def main():
    """Main execution"""
    print("=" * 50)
    print("Restaurant POS - Database Initialization")
    print("=" * 50)
    
    # Check if database already exists
    if os.path.exists(DB_PATH):
        response = input(f"\n⚠ Database already exists at {DB_PATH}\nDo you want to recreate it? (yes/no): ")
        if response.lower() != 'yes':
            print("Initialization cancelled.")
            return
        os.remove(DB_PATH)
        print("Old database removed.")
    
    # Create database and tables
    conn, cursor = create_database()
    
    # Insert sample data
    seed_sample_data(cursor, conn)
    
    # Close connection
    conn.close()
    
    print("\n" + "=" * 50)
    print("You can now run the FastAPI backend!")
    print("=" * 50)

if __name__ == "__main__":
    main()
