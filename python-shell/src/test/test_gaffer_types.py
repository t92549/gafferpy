#
# Copyright 2016 Crown Copyright
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import unittest

from gafferpy import gaffer as g


class GafferOperationsTest(unittest.TestCase):
    examples = [
        [
            '''
            {
            "type": "t", 
            "subType": "st", 
            "value": "v", 
            "class": "uk.gov.gchq.gaffer.types.TypeSubTypeValue"
            }
            ''',
            g.TypeSubTypeValue(
                type='t',
                sub_type='st',
                value='v'
            )
        ],
        [
            '''
            {
            "type": "t", 
            "value": "v", 
            "class": "uk.gov.gchq.gaffer.types.TypeValue"
            }
            ''',
            g.TypeValue(
                type='t',
                value='v'
            )
        ]
    ]

    def test_operations(self):
        for example in self.examples:
            self.assertEqual(
                json.loads(example[0]),
                example[1].to_json(),
                "json failed: \nexpected: \n" + example[0]
            )


if __name__ == "__main__":
    unittest.main()
