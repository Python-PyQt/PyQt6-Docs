.. sip:method-description::
    :status: todo
    :pysig: c0d078a852006e405769f0df7de63e27
    :realsig: (QAbstractAxis*)
    :digest: 703f8b15236af1d2f2202dca51428903

Attaches the axis specified by *axis* to the series.

Returns ``true`` if the axis was attached successfully, ``false`` otherwise.

**Note:** If multiple axes of the same orientation are attached to the same series, they will have the same minimum and maximum values.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QChart.addAxis`, :sip:ref:`~PyQt6.QtCharts.QChart.createDefaultAxes`.
