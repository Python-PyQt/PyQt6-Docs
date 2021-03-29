.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int*,int*,int*,int*) const
    :digest: ac051768bfe5570adfd5f5d27b315ebe

For each of *left*, *top*, *right* and *bottom* that is not ``nullptr``, stores the size of the margin named in the location the pointer refers to.

By default, :sip:ref:`~PyQt6.QtWidgets.QLayout` uses the values provided by the style. On most platforms, the margin is 11 pixels in all directions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout.setContentsMargins`, :sip:ref:`~PyQt6.QtWidgets.QStyle.pixelMetric`, :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutLeftMargin`, :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutTopMargin`, :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutRightMargin`, :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutBottomMargin`.
