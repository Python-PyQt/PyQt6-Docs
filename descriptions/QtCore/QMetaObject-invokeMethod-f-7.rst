.. sip:method-description::
    :status: todo
    :pysig: 0bf91c4c39bee100351ba767a48c9477
    :realsig: (QObject*,const char*,Qt::ConnectionType,QGenericReturnArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument)
    :digest: 041b4821d06910df80d00bfa8a6634b2

This is an overloaded function.

Please use the variadic overload of this function

Invokes the *member* (a signal or a slot name) on the object *obj*. Returns ``true`` if the member could be invoked. Returns ``false`` if there is no such member or the parameters did not match.

See the variadic :sip:ref:`~PyQt6.QtCore.QMetaObject.invokeMethod` function for more information. This function should behave the same way as that one, with the following limitations:

* The number of parameters is limited to 10.

* Parameter names may need to be an exact string match.

* Meta types are not automatically registered.

With asynchronous method invocations, the parameters must be of types that are already known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to use a queued connection and get the error message

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 83-83

call qRegisterMetaType() to register the data type before you call :sip:ref:`~PyQt6.QtCore.QMetaObject.invokeMethod`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Q_ARG`, :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG`, qRegisterMetaType(), :sip:ref:`~PyQt6.QtCore.QMetaMethod.invoke`.
