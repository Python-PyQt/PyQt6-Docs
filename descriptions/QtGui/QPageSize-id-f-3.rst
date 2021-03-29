.. sip:method-description::
    :status: todo
    :pysig: d503db6dd0b56d79dbd61d80219a0c7a
    :realsig: (const QSizeF&,QPageSize::Unit,QPageSize::SizeMatchPolicy)
    :digest: 595b2a6cabfb5c61cd45936456f66990

Returns the standard :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId` of the given *size* in *units* using the given *matchPolicy*.

If using :sip:ref:`~PyQt6.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch` then the unit size of the :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.PageSizeId` returned may not exactly match the *size* you passed in. You should call :sip:ref:`~PyQt6.QtGui.QPageSize.size` using the returned :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.PageSizeId` to find out the actual unit size of the :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.PageSizeId` before using it in any calculations.
