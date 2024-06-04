from database.db_config import async_session_maker
from database.models import User


class UserDAO():
    @classmethod
    async def user_exists(cls, id: int):
        async with async_session_maker() as session:
            return await session.get(User, id)

    @classmethod
    async def reg_user(cls, user):
        async with async_session_maker() as session:
            new_user = User(
                id=user.id,
                username=user.username,
                first_name=user.first_name or '',
                last_name=user.last_name or '',
                is_premium=user.is_premium or False
            )
            session.add(new_user)
            await session.commit()
