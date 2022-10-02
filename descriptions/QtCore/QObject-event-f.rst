.. sip:method-description::
    :status: todo
    :pysig: 78c2ee29b9f6bed2b9f05a748c095133
    :realsig: (QEvent*)
    :digest: 68469bf1cb0b6ec7a536e0cb4c7b68ce

This virtual function receives events to an object and should return true if the event *e* was recognized and processed.

The event() function can be reimplemented to customize the behavior of an object.

Make sure you call the parent event class implementation for all the events you did not handle.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 513-536

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.installEventFilter`, :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendEvent`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent`.
