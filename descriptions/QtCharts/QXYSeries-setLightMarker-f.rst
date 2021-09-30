.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: (const QImage&)
    :digest: 0c026f37f42b537970d2d4f09eaecaba

Sets the image used for drawing markers on each point of the series as the value of *lightMarker*.

The default value is a default-QImage() (\ :sip:ref:`~PyQt6.QtGui.QImage.isNull` == true), meaning no light marker will be painted. You can reset back to default (disabled) by calling this function with a null :sip:ref:`~PyQt6.QtGui.QImage` (QImage()).

The light markers visualize the data points of this series and as such are an alternative to ``setPointsVisible(true)``. If a light marker is set with this method, visible points as set with ``setPointsVisible(true)`` are not displayed.

Unlike the elements of :sip:ref:`~PyQt6.QtCharts.QScatterSeries` the light markers are not represented by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, but are just painted (no objects created). However, the mouse-event-signals of :sip:ref:`~PyQt6.QtCharts.QXYSeries` behave the same way, meaning that you'll get the exact domain value of the point if you click/press/hover the light marker. You'll still get the in between domain value if you click on the line. The light markers are above the line in terms of painting as well as events.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.lightMarker`.
