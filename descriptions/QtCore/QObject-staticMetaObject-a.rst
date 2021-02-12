.. sip:attribute-description::
    :status: todo
    :digest: 1b849f755c35b2dd2d2116f50dd02b22

This variable stores the meta-object for the class.

A meta-object contains information about a class that inherits :sip:ref:`~PyQt6.QtCore.QObject`, e.g. class name, superclass name, properties, signals and slots. Every class that contains the Q_OBJECT macro will also have a meta-object.

The meta-object information is required by the signal/slot connection mechanism and the property system. The :sip:ref:`~PyQt6.QtCore.QObject.inherits` function also makes use of the meta-object.

If you have a pointer to an object, you can use :sip:ref:`~PyQt6.QtCore.QObject.metaObject` to retrieve the meta-object associated with that object.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 62-65

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.metaObject`.
