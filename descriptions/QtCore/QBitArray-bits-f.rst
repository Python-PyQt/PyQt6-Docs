.. sip:method-description::
    :status: todo
    :pysig: 4b3a6218bb3e3a7303e8a171a60fcf92
    :realsig: () const
    :digest: c28cea3aab088b94cc037e468614f883

Returns a pointer to a dense bit array for this :sip:ref:`~PyQt6.QtCore.QBitArray`. Bits are counted upwards from the least significant bit in each byte. The number of bits relevant in the last byte is given by ``size() % 8``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBitArray.fromBits`, :sip:ref:`~PyQt6.QtCore.QBitArray.size`.
