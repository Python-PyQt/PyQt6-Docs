.. sip:method-description::
    :status: todo
    :pysig: bdeb09887722104b83df3d8984da49da
    :realsig: ()
    :digest: 113c3cade24c18fb7c01ee6d98e34708

Returns a pointer to a :sip:ref:`~PyQt6.QtWidgets.QErrorMessage` object that outputs the default Qt messages. This function creates such an object, if there isn't one already.

The object will only output log messages of :sip:ref:`~PyQt6.QtCore.QLoggingCategory.defaultCategory`.

The object will forward all messages to the original message handler.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qInstallMessageHandler`.
