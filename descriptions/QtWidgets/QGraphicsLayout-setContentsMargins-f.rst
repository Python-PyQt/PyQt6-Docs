.. sip:method-description::
    :status: todo
    :pysig: 5fd70130e629f44666196fc320d4f2e1
    :realsig: (qreal,qreal,qreal,qreal)
    :digest: 61e64f7bda4a8d6215117b5b5288091b

Sets the contents margins to *left*, *top*, *right* and *bottom*. The default contents margins for toplevel layouts are style dependent (by querying the pixelMetric for :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutLeftMargin`, :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutTopMargin`, :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutRightMargin` and :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutBottomMargin`).

For sublayouts the default margins are 0.

Changing the contents margins automatically invalidates the layout.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate`.
