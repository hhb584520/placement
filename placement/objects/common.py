#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class ObjectList(object):
    """Provide listiness for objects which are a list of other objects."""
    def __init__(self, objects=None):
        self.objects = objects or []

    def __len__(self):
        """List length is a proxy for truthiness."""
        return len(self.objects)

    def __getitem__(self, index):
        return self.objects[index]