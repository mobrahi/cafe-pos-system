restaurant-pos-system/
│
├── backend/                          # FastAPI application
│   ├── __init__.py
│   ├── main.py                       # FastAPI app entry point
│   ├── config.py                     # Configuration settings
│   ├── database.py                   # Database connection & session
│   │
│   ├── models/                       # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── menu_item.py
│   │   ├── order.py
│   │   └── order_item.py
│   │
│   ├── schemas/                      # Pydantic schemas for validation
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── menu_item.py
│   │   ├── order.py
│   │   └── order_item.py
│   │
│   ├── api/                          # API routes
│   │   ├── __init__.py
│   │   ├── dependencies.py           # Shared dependencies
│   │   └── v1/                       # API version 1
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── __init__.py
│   │       │   ├── categories.py
│   │       │   ├── menu_items.py
│   │       │   ├── orders.py
│   │       │   └── reports.py
│   │       └── router.py             # Aggregate all endpoints
│   │
│   ├── crud/                         # CRUD operations
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── menu_item.py
│   │   ├── order.py
│   │   └── order_item.py
│   │
│   └── utils/                        # Utility functions
│       ├── __init__.py
│       ├── receipt_generator.py
│       └── order_number_generator.py
│
├── frontend/                         # Streamlit application
│   ├── __init__.py
│   ├── app.py                        # Main Streamlit app
│   ├── config.py                     # Frontend configuration
│   │
│   ├── pages/                        # Streamlit pages
│   │   ├── 1_📋_Take_Order.py
│   │   ├── 2_🍽️_Menu_Management.py
│   │   ├── 3_📊_Sales_Reports.py
│   │   └── 4_📦_Inventory.py
│   │
│   ├── components/                   # Reusable UI components
│   │   ├── __init__.py
│   │   ├── cart_display.py
│   │   ├── menu_card.py
│   │   └── receipt_display.py
│   │
│   └── services/                     # API client services
│       ├── __init__.py
│       ├── api_client.py             # Base API client
│       ├── category_service.py
│       ├── menu_service.py
│       ├── order_service.py
│       └── report_service.py
│
├── database/                         # Database files
│   ├── restaurant_pos.db             # SQLite database (gitignored)
│   └── init_db.py                    # Database initialization script
│
├── tests/                            # Test files
│   ├── __init__.py
│   ├── test_api/
│   │   ├── __init__.py
│   │   ├── test_categories.py
│   │   ├── test_menu_items.py
│   │   └── test_orders.py
│   └── test_crud/
│       ├── __init__.py
│       └── test_menu_crud.py
│
├── scripts/                          # Utility scripts
│   ├── seed_data.py                  # Insert sample data
│   ├── run_backend.py                # Start FastAPI server
│   └── run_frontend.py               # Start Streamlit app
│
├── docs/                             # Documentation
│   ├── API.md                        # API documentation
│   ├── DATABASE.md                   # Database schema docs
│   └── USER_GUIDE.md                 # User guide
│
├── .env.example                      # Example environment variables
├── .env                              # Actual env variables (gitignored)
├── .gitignore
├── requirements.txt                  # Python dependencies
├── README.md                         # Project overview
└── setup.py                          # Package setup (optional)