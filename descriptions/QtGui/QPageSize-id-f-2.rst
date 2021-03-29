.. sip:method-description::
    :status: todo
    :pysig: b5439b6410662804f11d41fae4d9d5ee
    :realsig: (const QSize&,QPageSize::SizeMatchPolicy)
    :digest: 3c3b865e8aa4f0f827c1c49ad3b938df

Returns the standard :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId` of the given *pointSize* in points using the given *matchPolicy*.

If using :sip:ref:`~PyQt6.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch` then the point size of the :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.PageSizeId` returned may not exactly match the *pointSize* you passed in. You should call :sip:ref:`~PyQt6.QtGui.QPageSize.sizePoints` using the returned :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.PageSizeId` to find out the actual point size of the :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.PageSizeId` before using it in any calculations.
