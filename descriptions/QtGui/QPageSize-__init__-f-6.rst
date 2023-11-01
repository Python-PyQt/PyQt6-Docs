.. sip:method-description::
    :status: todo
    :pysig: ad07c069f51aa5cf1a8602c37e16b45f
    :realsig: (const QSizeF&, QPageSize::Unit, const QString&, QPageSize::SizeMatchPolicy)
    :digest: 85006f5658b9896e99d18ffe57dba100

Creates a custom page of the given *size* in *units*.

If the given *size* matches a standard :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId`, then that page size will be used. Note that if the *matchPolicy* is :sip:ref:`~PyQt6.QtGui.QPageSize.SizeMatchPolicy.FuzzyMatch` this may result in the *size* being adjusted to the standard size. To prevent this happening use a *matchPolicy* of :sip:ref:`~PyQt6.QtGui.QPageSize.SizeMatchPolicy.ExactMatch` instead.

If the given *size* is not a standard :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId` then a :sip:ref:`~PyQt6.QtGui.QPageSize.PageSizeId.Custom` size will be created. The original unit size will be preserved and used as the base for all other unit size calculations.

If *name* is null then a custom name will be created in the form "Custom (width x height)" where the size is expressed in units provided.
