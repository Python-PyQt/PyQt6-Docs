.. sip:method-description::
    :status: todo
    :pysig: eb52e02d20fc8287fb17099bbada8bd0
    :realsig: (QObject*,Qt::ConnectionType,QGenericReturnArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument) const
    :digest: 176eee4c70b34454208b166936d6ac47

Invokes this method on the object *object*. Returns ``true`` if the member could be invoked. Returns ``false`` if there is no such member or the parameters did not match.

The invocation can be either synchronous or asynchronous, depending on the *connectionType*:

* If *connectionType* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection`, the member will be invoked immediately.

* If *connectionType* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection`, a :sip:ref:`~PyQt6.QtCore.QEvent` will be posted and the member is invoked as soon as the application enters the main event loop.

* If *connectionType* is :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection`, the member is invoked synchronously if *object* lives in the same thread as the caller; otherwise it will invoke the member asynchronously.

The return value of this method call is placed in *returnValue*. If the invocation is asynchronous, the return value cannot be evaluated. You can pass up to ten arguments (\ *val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8*, and *val9*) to this method call.

:sip:ref:`~PyQt6.QtCore.QGenericArgument` and :sip:ref:`~PyQt6.QtCore.QGenericReturnArgument` are internal helper classes. Because signals and slots can be dynamically invoked, you must enclose the arguments using the :sip:ref:`~PyQt6.QtCore.Q_ARG` and :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG` macros. :sip:ref:`~PyQt6.QtCore.Q_ARG` takes a type name and a const reference of that type; :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG` takes a type name and a non-const reference.

To asynchronously invoke the animateClick() slot on a QPushButton:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 126-128

With asynchronous method invocations, the parameters must be of types that are known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to use a queued connection and get the error message

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 132-132

call qRegisterMetaType() to register the data type before you call .

To synchronously invoke the ``compute(QString, int, double)`` slot on some arbitrary object ``obj`` retrieve its return value:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 136-145

:sip:ref:`~PyQt6.QtCore.QMetaObject.normalizedSignature` is used here to ensure that the format of the signature is what  expects. E.g. extra whitespace is removed.

If the "compute" slot does not take exactly one QString, one int and one double in the specified order, the call will fail.

**Warning:** this method will not test the validity of the arguments: *object* must be an instance of the class of the :sip:ref:`~PyQt6.QtCore.QMetaObject` of which this :sip:ref:`~PyQt6.QtCore.QMetaMethod` has been constructed with. The arguments must have the same type as the ones expected by the method, else, the behaviour is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Q_ARG`, :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG`, qRegisterMetaType(), :sip:ref:`~PyQt6.QtCore.QMetaObject.invokeMethod`.
