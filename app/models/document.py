from sqlalchemy import Column, Integer, DateTime, Text, String

from app.core.config import Base


class DocumentModel(Base):
    """Модель для обработки документов"""

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True) # id файла
    user_id = Column(String(36), index=True)  # Связь с пользователем
    filename = Column(String(255))  # Текстовое поле — хранит имя
    file_path = Column(String(512))  # Текстовое поле — хранит путь
    file_size = Column(Integer)  # Числовое поле — хранит размер
    file_type = Column(String(50))  # Тип файла pdf, docx, txt, md
    description = Column(Text) # описание документа
    created_at = Column(DateTime, index=True) # дата загрузки файла
