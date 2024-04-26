.. sip:method-description::
    :status: todo
    :pysig: 992e8d0e5b57a6e4e940f41b84286512
    :realsig: ()
    :digest: c4367496ccf72d4b08eda8e0a729e9b3

Returns the current system time zone IANA ID.

Equivalent to calling :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`.\ :sip:ref:`~PyQt6.QtCore.QTimeZone.id`, but may bypass some computation to obtain it. Constructing a :sip:ref:`~PyQt6.QtCore.QTimeZone` from the returned byte array will produce the same result as :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`.

If the backend is unable to determine the correct system zone, the result is empty. In this case, :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`.\ :sip:ref:`~PyQt6.QtCore.QTimeZone.isValid` is false and a warning is output if either this method of :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone` is called.

If the backend is able to determine the correct system zone but not its name, an empty byte array is returned. For example, on Windows, the system native ID is converted to an IANA ID - if the system ID isn't known to the internal translation code, the result shall be empty. In this case, :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`.\ :sip:ref:`~PyQt6.QtCore.QTimeZone.isValid` shall be true.

This method is only available when feature ``timezone`` is enabled.

**Note:** Prior to Qt 6.7, when the result could not be determined, the misleading result "UTC" was returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone`.
