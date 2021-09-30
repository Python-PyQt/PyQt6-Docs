.. sip:method-description::
    :status: todo
    :pysig: 36ed6a62b151e46023a1d7fed9c481d3
    :realsig: (const int,const QXYSeries::PointConfiguration)
    :digest: 5ba24259ff689d5ce779758b8c0688de

Removes the configuration property identified by *key* from the point at *index* and restores the default look derived from the series' settings.

Removes the configuration type, such as color or size, specified by *key* from the point at *index* with configuration customizations, allowing that configuration property to be rendered as the default specified in the series' properties.

**Note:** It doesn't affect the configuration of other points.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.clearPointsConfiguration`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.setPointConfiguration`.
