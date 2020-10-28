# Copyright 2020 Fu Hanxi

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itchat
from itchat.content import TEXT

from .action import import_message, import_user


@itchat.msg_register([TEXT])
def text_reply(msg):
    name = msg.user.get('RemarkName') or msg.user.get('NickName') or msg.user.get('UserName')
    if msg.user.get('UserName') != msg.fromUserName:
        return

    user = import_user(msg.fromUserName, name)
    if user:
        message = import_message(user, msg.text)
