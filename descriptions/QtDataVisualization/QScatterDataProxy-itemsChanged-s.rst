.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 1d6c03e73706b28f1ef85edb93547986

This signal is emitted when the number of items specified by *count* is changed starting at the position *startIndex*. If items are changed in the array without calling :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.setItem` or :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.setItems`, this signal needs to be emitted to update the graph.
