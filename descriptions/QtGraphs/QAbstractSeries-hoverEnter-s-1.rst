.. sip:signal-description::
    :status: todo
    :pysig: 05cbc2bcdf797e394aa777bd92ad8da1
    :realsig: (const QString&, QPointF, QPointF)
    :digest: 878ac1e9deb618d4fccba032d6e8b081

This signal is emitted when the series hovering starts. The name of the series is in *seriesName*, the mouse/touch position in *position*, and the series value in *value*.

**Note:** This signal is only emitted when hoverable is set to true.

**Note:** For Pie graph, the value represents (angle of position, start angle of hovering slice)
