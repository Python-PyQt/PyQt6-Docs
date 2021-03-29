.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 87e19b8a9526b3f07571e1c406fc61ea

Returns the boolean value of the current element.

This function does not perform any type conversions, including from integer. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isTrue`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFalse` or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isBool` returned true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isBool`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isTrue`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFalse`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger`.
