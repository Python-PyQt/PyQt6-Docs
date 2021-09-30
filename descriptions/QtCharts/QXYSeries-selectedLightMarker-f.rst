.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: () const
    :digest: 6d535925d88bdf8f85b5d10449add986

Returns the image used for drawing markers on selected series' points.

The default value is QImage(), meaning usual :sip:ref:`~PyQt6.QtCharts.QXYSeries.lightMarker` will be painted.

This is equivalent to selectedColor if you prefer light markers over normal points, but still want to distinguish selected points.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.setSelectedLightMarker`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.lightMarker`, selectedColor, :sip:ref:`~PyQt6.QtCharts.QXYSeries.setPointSelected`.
