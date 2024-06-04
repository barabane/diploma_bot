from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings import settings

engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)
