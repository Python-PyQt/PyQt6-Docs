.. sip:method-description::
    :status: todo
    :pysig: 7f1beef864c2ca014548a738e695f1dd
    :realsig: (const QString&)
    :digest: 863ee4a9ba4029bb33265ef20176f132

Parses the string form *text* and returns the corresponding :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`. String representations are useful to inform other processes of the key this process created and they should attach to.

If the string could not be parsed, this function returns an :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.isValid` object.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.toString`, :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.isValid`.
