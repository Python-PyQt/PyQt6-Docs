.. sip:method-description::
    :status: todo
    :pysig: 11389636bba74aeb6abbeea5cc56a11a
    :realsig: (const QList<qreal>&,const QLinearGradient&)
    :digest: 740e721ee811c5f6dfea2e0f0196672d

Sets the points' color according to a passed list of values. Values from *sourceData* are sorted and mapped to the *gradient*.

If the series has a :sip:ref:`~PyQt6.QtCharts.QColorAxis` attached, then a gradient from the axis is going to be used.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.setPointConfiguration`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.pointConfiguration`, :sip:ref:`~PyQt6.QtCharts.QColorAxis`.
