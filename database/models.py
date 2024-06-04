from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import VARCHAR


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    first_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    last_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    is_premium: Mapped[bool]
