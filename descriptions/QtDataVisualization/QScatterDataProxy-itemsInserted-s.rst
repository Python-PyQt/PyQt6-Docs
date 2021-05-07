.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 3d401f64253a9fb2a51f270ae742e9d6

This signal is emitted when the number of items specified by *count* is inserted starting at the position *startIndex*. If items are inserted into the array without calling :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.insertItem` or :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.insertItems`, this signal needs to be emitted to update the graph.
