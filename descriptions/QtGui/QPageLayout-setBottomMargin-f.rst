.. sip:method-description::
    :status: todo
    :pysig: 4c35c6b51bc2a5b1cb547d1af033255f
    :realsig: (qreal)
    :digest: ffe171eb29f544497f0925ecc81b288b

Sets the bottom page margin of the page layout to *bottomMargin*. Returns true if the margin was successfully set.

The units used are those currently defined for the layout. To use different units call :sip:ref:`~PyQt6.QtGui.QPageLayout.setUnits` first.

If in the default :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.StandardMode` then the new margin must fall between the minimum margin set and the maximum margin allowed by the page size, otherwise the margin will not be set.

If in :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode.FullPageMode` then any margin values will be accepted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageLayout.setMargins`, :sip:ref:`~PyQt6.QtGui.QPageLayout.margins`.
