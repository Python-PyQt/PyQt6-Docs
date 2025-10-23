.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (double)
    :digest: 2bb37bcd025c62ef3ddec33ccba1d4e6

Appends the floating point number *d* to the stream, creating a CBOR 64-bit Double-Precision Floating Point value. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` always appends the number as-is, performing no check for whether the number is the canonical form for NaN, an infinite, whether it is denormal or if it could be written with a shorter format.

The following code performs all those checks, except for the denormal one, which is expected to be taken into account by the system FPU or floating point emulation directly.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 177-193

Determining if a double can be converted to an integral with no loss of precision is left as an exercise to the reader.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isDouble`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toDouble`.
