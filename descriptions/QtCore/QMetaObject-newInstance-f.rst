.. sip:method-description::
    :status: todo
    :pysig: 1388053ee30c0287c94ffa372a9708c0
    :realsig: (QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument,QGenericArgument) const
    :digest: 80fe90c0900e324fbb72e16cd8aef2ab

Please use the variadic overload of this function

Constructs a new instance of this class. You can pass up to ten arguments (\ *val0*, *val1*, *val2*, *val3*, *val4*, *val5*, *val6*, *val7*, *val8*, and *val9*) to the constructor. Returns the new object, or ``nullptr`` if no suitable constructor is available.

Note that only constructors that are declared with the Q_INVOKABLE modifier are made available through the meta-object system.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Q_ARG`, :sip:ref:`~PyQt6.QtCore.QMetaObject.constructor`.
