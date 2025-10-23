.. sip:method-description::
    :status: todo
    :pysig: 6fb60876b5136c816ecc1a895d3012c0
    :realsig: (const QString&, const QString&)
    :digest: 85f17edec3775103390d51ea37dba9d4

Shows the given message, *message*, and returns immediately. If the user has requested for messages of type, *type*, not to be shown again, this function does nothing.

Normally, the message is displayed immediately. However, if there are pending messages, it will be queued to be displayed later.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QErrorMessage.showMessage`.
