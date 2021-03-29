.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ecd85b28c673a90ea7debeca37c4c8a6

Returns true if the type of the current element is an IEEE 754 double-precision floating point (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Double`). If this function returns true, you may call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toDouble` to read that data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toDouble`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFloat16`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFloat`.
