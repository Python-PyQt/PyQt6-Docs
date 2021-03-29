.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 9ee60f156852d9d8c90fdb898cb86760

Returns the Windows DMPAPER enum value for the page size.

Not all valid PPD page sizes have a Windows equivalent, in which case 0 will be returned.

If the :sip:ref:`~PyQt6.QtGui.QPageSize` is invalid then the Windows ID will be 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageSize.id`.
