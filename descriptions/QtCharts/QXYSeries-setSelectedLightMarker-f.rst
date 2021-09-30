.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: (const QImage&)
    :digest: 3f15a7ea7a0e0242593971007bd4e815

Sets the image used for drawing markers on selected series's points to *selectedLightMarker*.

The default value is QImage(), meaning usual :sip:ref:`~PyQt6.QtCharts.QXYSeries.lightMarker` will be painted.

This is an equivalent for selectedColor if you prefer light markers over normal points, but still want to distinguish selected points.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.selectedLightMarker`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.lightMarker`, selectedColor, :sip:ref:`~PyQt6.QtCharts.QXYSeries.setPointSelected`.
