.. sip:method-description::
    :status: todo
    :pysig: 0bf91c4c39bee100351ba767a48c9477
    :realsig: (QObject*,const char*,Qt::ConnectionType,QGenericReturnArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument)
    :digest: 8d2ea6a282a9d1ec828dd8df52d2384a

Invokes the *member* (a signal or a slot name) on the object *obj*. Returns ``true`` if the member could be invoked. Returns ``false`` if there is no such member or the parameters did not match.

The invocation can be either synchronous or asynchronous, depending on *type*:

* If *type* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection`, the member will be invoked immediately.

* If *type* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection`, a :sip:ref:`~PyQt6.QtCore.QEvent` will be sent and the member is invoked as soon as the application enters the main event loop.

* If *type* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.BlockingQueuedConnection`, the method will be invoked in the same way as for :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection`, except that the current thread will block until the event is delivered. Using this connection type to communicate between objects in the same thread will lead to deadlocks.

* If *type* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection`, the member is invoked synchronously if *obj* lives in the same thread as the caller; otherwise it will invoke the member asynchronously.

The return value of the *member* function call is placed in *ret*. If the invocation is asynchronous, the return value cannot be evaluated. You can pass up to ten arguments (\ *val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8*, and *val9*) to the *member* function.

:sip:ref:`~PyQt6.QtCore.QGenericArgument` and :sip:ref:`~PyQt6.QtCore.QGenericReturnArgument` are internal helper classes. Because signals and slots can be dynamically invoked, you must enclose the arguments using the :sip:ref:`~PyQt6.QtCore.Q_ARG` and :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG` macros. :sip:ref:`~PyQt6.QtCore.Q_ARG` takes a type name and a const reference of that type; :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG` takes a type name and a non-const reference.

You only need to pass the name of the signal or slot to this function, not the entire signature. For example, to asynchronously invoke the :sip:ref:`~PyQt6.QtCore.QThread.quit` slot on a :sip:ref:`~PyQt6.QtCore.QThread`, use the following code:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 77-78

With asynchronous method invocations, the parameters must be of types that are known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to use a queued connection and get the error message

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 83-83

call qRegisterMetaType() to register the data type before you call invokeMethod().

To synchronously invoke the ``compute(QString, int, double)`` slot on some arbitrary object ``obj`` retrieve its return value:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 88-93

If the "compute" slot does not take exactly one QString, one int and one double in the specified order, the call will fail.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Q_ARG`, :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG`, qRegisterMetaType(), :sip:ref:`~PyQt6.QtCore.QMetaMethod.invoke`.
