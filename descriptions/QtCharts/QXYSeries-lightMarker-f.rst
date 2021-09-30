.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: () const
    :digest: 01cb28347ac004bccefa71b559bfe555

Gets the image used for drawing markers on each point of the series.

The default value is QImage(), meaning no light marker will be painted.

The light markers visualize the data points of this series and as such are an alternative to :sip:ref:`~PyQt6.QtCharts.QXYSeries.setPointsVisible`\ (true). Both features can be enabled independently from each other.

Unlike the elements of :sip:ref:`~PyQt6.QtCharts.QScatterSeries` the light markers are not represented by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, but are just painted (no objects created). However, the mouse-event-signals of :sip:ref:`~PyQt6.QtCharts.QXYSeries` behave the same way, meaning that you'll get the exact domain value of the point if you click/press/hover the light marker. You'll still get the in between domain value if you click on the line. The light markers are above the line in terms of painting as well as events.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.setLightMarker`.
