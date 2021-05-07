.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 7e2c3d2be42100e054680bcb7fecce18

This signal is emitted when the number of items specified by *count* is added starting at the position *startIndex*. If items are added to the array without calling :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.addItem` or :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataProxy.addItems`, this signal needs to be emitted to update the graph.
