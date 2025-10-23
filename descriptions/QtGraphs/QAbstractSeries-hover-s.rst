.. sip:signal-description::
    :status: todo
    :pysig: 00cefd2ce748e08ee7fe7f53fced0a2e
    :realsig: (const QString&, QPointF, QPointF)
    :digest: 2f642c65bfe5a6705de51c24f408c641

This signal is emitted when the series hovering changes. The name of the series is in *seriesName*, the mouse/touch position in *position*, and the series value in *value*.

**Note:** This signal is only emitted when hoverable is set to true.

**Note:** For Pie graph, the value represents (angle of position, start angle of hovering slice)
