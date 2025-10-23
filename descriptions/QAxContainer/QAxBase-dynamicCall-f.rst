.. sip:method-description::
    :status: todo
    :pysig: fbe64f8f43e16f9d5e9d897299f03232
    :realsig: (const char*,QList<QVariant>&)
    :digest: dcb2fba282b55e0a91ba0b71f5e1646a

Calls the COM object's method *function*, passing the parameters in *vars*, and returns the value returned by the method. If the method does not return a value or when the function call failed this function returns an invalid :sip:ref:`~PyQt6.QtCore.QVariant` object.

The :sip:ref:`~PyQt6.QtCore.QVariant` objects in *vars* are updated when the method has out-parameters.
