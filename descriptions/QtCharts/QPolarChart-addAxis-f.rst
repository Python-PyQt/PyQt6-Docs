.. sip:method-description::
    :status: todo
    :pysig: 26cfa158b1ad0ab9b27dcc9374f67b4b
    :realsig: (QAbstractAxis*,QPolarChart::PolarOrientation)
    :digest: 288ad80d9a99529bd61440e1ca76224c

This convenience method adds the axis *axis* to the polar chart with the polar orientation *polarOrientation*. The chart takes the ownership of the axis.

**Note:** Axes can be added to a polar chart also with :sip:ref:`~PyQt6.QtCharts.QChart.addAxis`. The specified alignment determines the polar orientation: horizontal alignments indicate an angular axis and vertical alignments indicate a radial axis.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QChart.removeAxis`, :sip:ref:`~PyQt6.QtCharts.QChart.createDefaultAxes`, :sip:ref:`~PyQt6.QtCharts.QAbstractSeries.attachAxis`, :sip:ref:`~PyQt6.QtCharts.QChart.addAxis`.
