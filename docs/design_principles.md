Key Design Principles:
1. Separation of Concerns:

Backend and frontend are completely separate
Each has its own configuration and dependencies
Clear API contract between them

2. Layered Architecture (Backend):

models/ - Database layer (SQLAlchemy ORM)
schemas/ - Data validation layer (Pydantic)
crud/ - Data access layer (business logic)
api/ - Presentation layer (HTTP endpoints)
utils/ - Helper functions

3. API Versioning:

/api/v1/ structure allows future API changes without breaking existing clients

4. Frontend Organization:

pages/ - Multi-page Streamlit app
components/ - Reusable UI elements
services/ - API communication logic (keeps pages clean)

