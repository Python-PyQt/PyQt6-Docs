.. sip:method-description::
    :status: todo
    :pysig: 72edab45cf68200664895e02d71a54ff
    :realsig: (qreal, QPageLayout::OutOfBoundsPolicy)
    :digest: 4331dda271d05e680299513e5caa67a6

Sets the top page margin of the page layout to *topMargin*. Returns true if the margin was successfully set.

The units used are those currently defined for the layout. To use different units call :sip:ref:`~PyQt6.QtGui.QPageLayout.setUnits` first.

Since Qt 6.8, the optional *outOfBoundsPolicy* can be used to specify how margins that are out of bounds are handled.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageLayout.setMargins`, :sip:ref:`~PyQt6.QtGui.QPageLayout.margins`.
