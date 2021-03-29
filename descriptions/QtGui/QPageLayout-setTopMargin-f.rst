.. sip:method-description::
    :status: todo
    :pysig: 4c35c6b51bc2a5b1cb547d1af033255f
    :realsig: (qreal)
    :digest: 7aa29d6ad9f45db1981e16d37c009213

Sets the top page margin of the page layout to *topMargin*. Returns true if the margin was successfully set.

The units used are those currently defined for the layout. To use different units call :sip:ref:`~PyQt6.QtGui.QPageLayout.setUnits` first.

If in the default :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.StandardMode` then the new margin must fall between the minimum margin set and the maximum margin allowed by the page size, otherwise the margin will not be set.

If in :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` then any margin values will be accepted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageLayout.setMargins`, :sip:ref:`~PyQt6.QtGui.QPageLayout.margins`.
