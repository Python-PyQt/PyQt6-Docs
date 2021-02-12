.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 55b6cf0c35c9f1fc0864696296bd5a75

Returns true if the current element is a boolean value (``true`` or ``false``), false if it is anything else. If this function returns true, you may call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toBool` to retrieve the value of the boolean. You may also call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType` and compare to either QCborSimpleValue::True or QCborSimpleValue::False.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFalse`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isTrue`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toBool`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`.
