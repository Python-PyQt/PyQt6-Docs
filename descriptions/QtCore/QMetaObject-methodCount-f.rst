.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 933ba27597b4e7885684668b1e6665b0

Returns the number of methods in this class, including the number of methods provided by each base class. These include signals and slots as well as normal member functions.

Use code like the following to obtain a QStringList containing the methods specific to a given class:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 119-122

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.method`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodOffset`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`.
