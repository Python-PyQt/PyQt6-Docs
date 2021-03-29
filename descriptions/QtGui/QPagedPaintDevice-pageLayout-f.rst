.. sip:method-description::
    :status: todo
    :pysig: 6ef83e7a6ea2ea55ef2fa9b26bac851e
    :realsig: () const
    :digest: 47b83fc534bf8599c2ca17f8f4e1eb3a

Returns the current page layout. Use this method to access the current :sip:ref:`~PyQt6.QtGui.QPageSize`, :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation`, :sip:ref:`~PyQt6.QtCore.QMarginsF`, fullRect() and paintRect().

Note that you cannot use the setters on the returned object, you must either call the individual :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice` setters or use :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageLayout`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageLayout`, :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageSize`, :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageOrientation`, :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageMargins`.
