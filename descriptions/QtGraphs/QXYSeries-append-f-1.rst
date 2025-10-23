.. sip:method-description::
    :status: todo
    :pysig: 34e3e9882007fbf7215e4e2f808d0707
    :realsig: (const QList<QPointF>&)
    :digest: 95602ac1886a38f56574d546fb1c13ec

Appends points with the coordinates *points* to the series.

**Note:** This is much faster than appending data points one by one. Emits :sip:ref:`~PyQt6.QtGraphs.QXYSeries.pointsAdded` when the points have been added.
