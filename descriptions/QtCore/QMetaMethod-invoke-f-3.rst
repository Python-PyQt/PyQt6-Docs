.. sip:method-description::
    :status: todo
    :pysig: eb52e02d20fc8287fb17099bbada8bd0
    :realsig: (QObject*,Qt::ConnectionType,QGenericReturnArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument) const
    :digest: ed516b81db1a71dea3f5546d503f95ec

Please use the variadic overload of this function

Invokes this method on the object *object*. Returns ``true`` if the member could be invoked. Returns ``false`` if there is no such member or the parameters did not match.

See the variadic invokeMethod() function for more information. This function should behave the same way as that one, with the following limitations:

* The number of parameters is limited to 10.

* Parameter names may need to be an exact string match.

* Meta types are not automatically registered.

With asynchronous method invocations, the parameters must be of types that are known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to use a queued connection and get the error message

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 132-132

call qRegisterMetaType() to register the data type before you call QMetaMethod::invoke().

**Warning:** In addition to the limitations of the variadic invoke() overload, the arguments must have the same type as the ones expected by the method, else, the behavior is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Q_ARG`, :sip:ref:`~PyQt6.QtCore.Q_RETURN_ARG`, qRegisterMetaType(), :sip:ref:`~PyQt6.QtCore.QMetaObject.invokeMethod`.
