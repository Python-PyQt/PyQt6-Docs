.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 7cfde97484ff27ad9ef35edadbfa0778

Returns true if the type of the current element is an unsigned integer (that is if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.UnsignedInteger`). If this function returns true, you may call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toUnsignedInteger` or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger` to read that value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toUnsignedInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isNegativeInteger`.
