from sqlalchemy import Column, Integer, DateTime, String, Text

from app.core.config import Base


class UserModel(Base):
    """Модель для пользователя"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    title = Column(String(500)) # название
    description = Column(Text) # описание
    created_at = Column(DateTime, index=True)
