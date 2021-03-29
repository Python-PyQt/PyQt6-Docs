.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 4ff5d86fd2e9eeff7cef2784e86fc98c

Returns true if the type of the current element is a negative integer (that is if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.NegativeInteger`). If this function returns true, you may call toNegativeInteger() or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger` to read that value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, toNegativeInteger(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isUnsignedInteger`.
