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
Instruction operand kind
"""

# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=redefined-builtin
# pylint: disable=too-many-lines

from typing import List

Register: int = 0
"""
A register (``Register``).

This operand kind uses ``Instruction.op0_register``, ``Instruction.op1_register``, ``Instruction.op2_register``, ``Instruction.op3_register`` or ``Instruction.op4_register`` depending on operand number. See also ``Instruction.op_register()``.
"""
NearBranch16: int = 1
"""
Near 16-bit branch. This operand kind uses ``Instruction.near_branch16``
"""
NearBranch32: int = 2
"""
Near 32-bit branch. This operand kind uses ``Instruction.near_branch32``
"""
NearBranch64: int = 3
"""
Near 64-bit branch. This operand kind uses ``Instruction.near_branch64``
"""
FarBranch16: int = 4
"""
Far 16-bit branch. This operand kind uses ``Instruction.far_branch16`` and ``Instruction.far_branch_selector``
"""
FarBranch32: int = 5
"""
Far 32-bit branch. This operand kind uses ``Instruction.far_branch32`` and ``Instruction.far_branch_selector``
"""
Immediate8: int = 6
"""
8-bit constant. This operand kind uses ``Instruction.immediate8``
"""
Immediate8_2nd: int = 7
"""
8-bit constant used by the ``ENTER``, ``EXTRQ``, ``INSERTQ`` instructions. This operand kind uses ``Instruction.immediate8_2nd``
"""
Immediate16: int = 8
"""
16-bit constant. This operand kind uses ``Instruction.immediate16``
"""
Immediate32: int = 9
"""
32-bit constant. This operand kind uses ``Instruction.immediate32``
"""
Immediate64: int = 10
"""
64-bit constant. This operand kind uses ``Instruction.immediate64``
"""
Immediate8to16: int = 11
"""
An 8-bit value sign extended to 16 bits. This operand kind uses ``Instruction.immediate8to16``
"""
Immediate8to32: int = 12
"""
An 8-bit value sign extended to 32 bits. This operand kind uses ``Instruction.immediate8to32``
"""
Immediate8to64: int = 13
"""
An 8-bit value sign extended to 64 bits. This operand kind uses ``Instruction.immediate8to64``
"""
Immediate32to64: int = 14
"""
A 32-bit value sign extended to 64 bits. This operand kind uses ``Instruction.immediate32to64``
"""
MemorySegSI: int = 15
"""
``seg:[SI]``. This operand kind uses ``Instruction.memory_size``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""
MemorySegESI: int = 16
"""
``seg:[ESI]``. This operand kind uses ``Instruction.memory_size``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""
MemorySegRSI: int = 17
"""
``seg:[RSI]``. This operand kind uses ``Instruction.memory_size``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""
MemorySegDI: int = 18
"""
``seg:[DI]``. This operand kind uses ``Instruction.memory_size``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""
MemorySegEDI: int = 19
"""
``seg:[EDI]``. This operand kind uses ``Instruction.memory_size``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""
MemorySegRDI: int = 20
"""
``seg:[RDI]``. This operand kind uses ``Instruction.memory_size``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""
MemoryESDI: int = 21
"""
``ES:[DI]``. This operand kind uses ``Instruction.memory_size``
"""
MemoryESEDI: int = 22
"""
``ES:[EDI]``. This operand kind uses ``Instruction.memory_size``
"""
MemoryESRDI: int = 23
"""
``ES:[RDI]``. This operand kind uses ``Instruction.memory_size``
"""
Memory64: int = 24
"""
64-bit offset ``[xxxxxxxxxxxxxxxx]``. This operand kind uses ``Instruction.memory_address64``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``, ``Instruction.memory_size``
"""
Memory: int = 25
"""
Memory operand.

This operand kind uses ``Instruction.memory_displ_size``, ``Instruction.memory_size``, ``Instruction.memory_index_scale``, ``Instruction.memory_displacement``, ``Instruction.memory_base``, ``Instruction.memory_index``, ``Instruction.memory_segment``, ``Instruction.segment_prefix``
"""

__all__: List[str] = []
