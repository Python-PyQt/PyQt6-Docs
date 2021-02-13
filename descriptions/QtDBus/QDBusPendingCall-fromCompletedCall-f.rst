.. sip:method-description::
    :status: todo
    :pysig: 9da9eeceaf7f632487471c19c9473cc2
    :realsig: (const QDBusMessage&)
    :digest: 5bec2e3d311d7c6ec1157dbcf69d6e1a

Creates a :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall` object based on the message *msg*. The message must be of type :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.ErrorMessage` or :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.ReplyMessage` (that is, a message that is typical of a completed call).

This function is useful for code that requires simulating a pending call, but that has already finished.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall.fromError`.
