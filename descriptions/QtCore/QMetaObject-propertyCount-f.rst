.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 61773dd949ea825310c195823d77fb24

Returns the number of properties in this class, including the number of properties provided by each base class.

Use code like the following to obtain a QStringList containing the properties specific to a given class:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 111-114

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.property`, :sip:ref:`~PyQt6.QtCore.QMetaObject.propertyOffset`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfProperty`.
