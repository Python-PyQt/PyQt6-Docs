.. sip:method-description::
    :status: todo
    :pysig: 34e3e9882007fbf7215e4e2f808d0707
    :realsig: (const QList<QPointF>&)
    :digest: a8b7a1394f8a2a8746d6c5d9570bc4b8

Replaces the current points with the points specified by *points*

**Note:** This is much faster than replacing data points one by one, or first clearing all data, and then appending the new data. Emits :sip:ref:`~PyQt6.QtGraphs.QXYSeries.pointsReplaced` when the points have been replaced.
