.. sip:method-description::
    :status: todo
    :pysig: 1e45c6b484a140812602aa3e2fef374a
    :realsig: () const
    :digest: fb6a3ed5b0303f0f7c861125293895d8

Returns the keyboard modifier flags that existed immediately after the event occurred.

**Warning:** This function cannot always be trusted. The user can confuse it by pressing both Shift keys simultaneously and releasing one of them, for example.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`.
