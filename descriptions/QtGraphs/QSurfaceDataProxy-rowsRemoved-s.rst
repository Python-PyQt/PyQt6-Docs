.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qsizetype, qsizetype)
    :digest: aa71cbbad3f9a580fc037905bc54d0cc

This signal is emitted when the number of rows specified by *count* is removed, starting at the position *startIndex*.

The index is the current array size if the rows were removed from the end of the array. If rows are removed from the array without calling :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy.removeRows`, this signal needs to be emitted to update the graph.
