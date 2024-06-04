from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, types
from dao import UserDAO


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        if not await UserDAO.user_exists(event.from_user.id):
            await UserDAO.reg_user(event.from_user)
        return await handler(event, data)
