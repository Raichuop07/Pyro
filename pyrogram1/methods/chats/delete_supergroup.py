#  Pyrogram1 - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram1.
#
#  Pyrogram1 is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram1 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram1.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union

from pyrogram1 import raw
from pyrogram1.scaffold import Scaffold


class DeleteSupergroup(Scaffold):
    async def delete_supergroup(self, chat_id: Union[int, str]) -> bool:
        """Delete a supergroup.

        Parameters:
            chat_id (``int`` | ``str``):
                The id of the supergroup to be deleted.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                app.delete_supergroup(supergroup_id)
        """
        await self.send(
            raw.functions.channels.DeleteChannel(
                channel=await self.resolve_peer(chat_id)
            )
        )

        return True
