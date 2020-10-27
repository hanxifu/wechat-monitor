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

import logging

from .model import Message, User


def import_user(user_id: str, user_name: str):
    user, _ = User.get_or_create(id=user_id, name=user_name)
    logging.info(f'Imported: {user}')
    return user


def import_message(user: User, message: str):
    message = Message.create(user=user, text=message)
    logging.info(f'Imported: {message}')
    return message
