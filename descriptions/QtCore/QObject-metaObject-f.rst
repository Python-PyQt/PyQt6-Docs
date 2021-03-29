.. sip:method-description::
    :status: todo
    :pysig: dcb157b095ed75dc56e69b125cbb12b0
    :realsig: () const
    :digest: eaaaffa44914f2959f87a0f41e45e1ea

Returns a pointer to the meta-object of this object.

A meta-object contains information about a class that inherits :sip:ref:`~PyQt6.QtCore.QObject`, e.g. class name, superclass name, properties, signals and slots. Every :sip:ref:`~PyQt6.QtCore.QObject` subclass that contains the Q_OBJECT macro will have a meta-object.

The meta-object information is required by the signal/slot connection mechanism and the property system. The :sip:ref:`~PyQt6.QtCore.QObject.inherits` function also makes use of the meta-object.

If you have no pointer to an actual object instance but still want to access the meta-object of a class, you can use staticMetaObject.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 54-57

.. seealso:: staticMetaObject.
