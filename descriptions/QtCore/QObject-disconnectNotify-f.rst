.. sip:method-description::
    :status: todo
    :pysig: c567edb399b702bd49a6f5ea4ea59c51
    :realsig: (const QMetaMethod&)
    :digest: b2490970ff636f1560899144b22ccbac

This virtual function is called when something has been disconnected from *signal* in this object.

See :sip:ref:`~PyQt6.QtCore.QObject.connectNotify` for an example of how to compare *signal* with a specific signal.

If all signals were disconnected from this object (e.g., the signal argument to :sip:ref:`~PyQt6.QtCore.QObject.disconnect` was ``nullptr``), disconnectNotify() is only called once, and the *signal* will be an invalid :sip:ref:`~PyQt6.QtCore.QMetaMethod` (\ :sip:ref:`~PyQt6.QtCore.QMetaMethod.isValid` returns ``false``).

**Warning:** This function violates the object-oriented principle of modularity. However, it might be useful for optimizing access to expensive resources.

**Warning:** This function is called from the thread which performs the disconnection, which may be a different thread from the thread in which this object lives. This function may also be called with a :sip:ref:`~PyQt6.QtCore.QObject` internal mutex locked. It is therefore not allowed to re-enter any :sip:ref:`~PyQt6.QtCore.QObject` functions, including :sip:ref:`~PyQt6.QtCore.QObject.isSignalConnected`, from your reimplementation. If you lock a mutex in your reimplementation, make sure that you don't call :sip:ref:`~PyQt6.QtCore.QObject` functions with that mutex held in other places or it will result in a deadlock.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.disconnect`, :sip:ref:`~PyQt6.QtCore.QObject.connectNotify`.
