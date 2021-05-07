.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 161aa675e5682ba11bce0686dbc097a6

This signal is emitted when the number of rows specified by *count* is changed starting at the position *startIndex*. If rows are changed in the array without calling :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy.setRow` or :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy.setRows`, this signal needs to be emitted to update the graph.
