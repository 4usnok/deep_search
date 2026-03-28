from datetime import datetime

from pydantic import BaseModel


class UserSchemas(BaseModel):
    """SQLAlchemy модель для пользователей"""

    id: int
    title: str
    description: str
    created_at: datetime
