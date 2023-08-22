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

import logging

from pyrogram1 import raw
from pyrogram1.scaffold import Scaffold

log = logging.getLogger(__name__)


class GetPasswordHint(Scaffold):
    async def get_password_hint(self) -> str:
        """Get your Two-Step Verification password hint.

        Returns:
            ``str``: On success, the password hint as string is returned.
        """
        return (await self.send(raw.functions.account.GetPassword())).hint