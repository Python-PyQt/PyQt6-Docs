.. sip:method-description::
    :status: todo
    :pysig: 97cf6f90f2f5952c19e0ce8d511b7e4e
    :realsig: (const QList<qreal>&,const qreal,const qreal)
    :digest: 2fcc0f1e7d227834715c49cfc2e4db55

Sets the points' sizes according to a passed list of values. Values from *sourceData* are sorted and mapped to a point size which is between *minSize* and *maxSize*.

**Note:** If *sourceData* length is smaller than number of points in the series, then size of the points at the end of the series will stay the same.

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.setPointConfiguration`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.pointConfiguration`.
