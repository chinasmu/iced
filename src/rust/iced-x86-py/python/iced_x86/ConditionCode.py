#
# Copyright (C) 2018-2019 de4dot@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# ⚠️This file was generated by GENERATOR!🦹‍♂️

"""
Instruction condition code (used by ``Jcc``, ``SETcc``, ``CMOVcc``, ``LOOPcc``)
"""

# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=redefined-builtin
# pylint: disable=too-many-lines

from typing import List

Nothing: int = 0
"""
The instruction doesn't have a condition code
"""
o: int = 1
"""
Overflow (``OF=1``)
"""
no: int = 2
"""
Not overflow (``OF=0``)
"""
b: int = 3
"""
Below (unsigned) (``CF=1``)
"""
ae: int = 4
"""
Above or equal (unsigned) (``CF=0``)
"""
e: int = 5
"""
Equal / zero (``ZF=1``)
"""
ne: int = 6
"""
Not equal / zero (``ZF=0``)
"""
be: int = 7
"""
Below or equal (unsigned) (``CF=1 or ZF=1``)
"""
a: int = 8
"""
Above (unsigned) (``CF=0 and ZF=0``)
"""
s: int = 9
"""
Signed (``SF=1``)
"""
ns: int = 10
"""
Not signed (``SF=0``)
"""
p: int = 11
"""
Parity (``PF=1``)
"""
np: int = 12
"""
Not parity (``PF=0``)
"""
l: int = 13
"""
Less (signed) (``SF!=OF``)
"""
ge: int = 14
"""
Greater than or equal (signed) (``SF=OF``)
"""
le: int = 15
"""
Less than or equal (signed) (``ZF=1 or SF!=OF``)
"""
g: int = 16
"""
Greater (signed) (``ZF=0 and SF=OF``)
"""

__all__: List[str] = []
