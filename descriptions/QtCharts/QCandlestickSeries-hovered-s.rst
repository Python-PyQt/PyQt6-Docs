.. sip:signal-description::
    :status: todo
    :pysig: 05ecee6d4ae8881a7cc137889e120f69
    :realsig: (bool,QCandlestickSet*)
    :digest: 72e45f339476dfa43908f593b6546444

This signal is emitted when a mouse is hovered over the candlestick item specified by *set* in a chart.

When the mouse moves over the item, *status* turns ``true``, and when the mouse moves away again, it turns ``false``.
