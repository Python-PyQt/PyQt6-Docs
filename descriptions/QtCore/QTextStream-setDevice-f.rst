.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: b0fc106670ce44128f84a24312214428

Sets the current device to *device*. If a device has already been assigned, :sip:ref:`~PyQt6.QtCore.QTextStream` will call :sip:ref:`~PyQt6.QtCore.QTextStream.flush` before the old device is replaced.

**Note:** This function resets locale to the default locale ('C') and encoding to the default encoding, UTF-8.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.device`, setString().
