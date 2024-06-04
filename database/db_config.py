from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine()
async_session_maker = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)
