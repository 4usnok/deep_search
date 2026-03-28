from datetime import datetime

from pydantic import BaseModel


class DocumentSchemas(BaseModel):
    """SQLAlchemy модель для документов"""

    id: int
    user_id: int
    filename: str
    file_path: str
    file_size: int
    file_type: str
    description: str
    created_at: datetime
