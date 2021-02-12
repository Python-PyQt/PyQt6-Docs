.. sip:method-description::
    :status: todo
    :pysig: 9481d8a0303ed273423e0a0513981d8d
    :realsig: () const
    :digest: 087c5f02e63e75272e1bd6f12b33d575

Returns the locale to use for collation.

The result is usually this locale; however, the system locale (which is commonly the default locale) will return the system collation locale. The result is suitable for passing to :sip:ref:`~PyQt6.QtCore.QCollator`'s constructor.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCollator`.
