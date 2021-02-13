.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&,const QString&)
    :digest: f19b5e36e7c6828ad13d0ec71f02509e

This is an overloaded function.

Shows the given message, *message*, and returns immediately. If the user has requested for messages of type, *type*, not to be shown again, this function does nothing.

Normally, the message is displayed immediately. However, if there are pending messages, it will be queued to be displayed later.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QErrorMessage.showMessage`.
