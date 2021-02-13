.. sip:method-description::
    :status: todo
    :pysig: 60613d939bb95fe167128162c17be7e1
    :realsig: () const
    :digest: fb6a3ed5b0303f0f7c861125293895d8

Returns the keyboard modifier flags that existed immediately after the event occurred.

**Warning:** This function cannot always be trusted. The user can confuse it by pressing both Shift keys simultaneously and releasing one of them, for example.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.keyboardModifiers`.
