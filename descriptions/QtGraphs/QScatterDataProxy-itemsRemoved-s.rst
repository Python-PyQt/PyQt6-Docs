.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qsizetype, qsizetype)
    :digest: dcc09fbcf40734b51a513eb2005fb98f

This signal is emitted when the number of rows specified by *count* are removed, starting at the position *startIndex*. The index may be larger than the current array size if items are removed from the end. If items are removed from the array without calling :sip:ref:`~PyQt6.QtGraphs.QScatterDataProxy.removeItems`, this signal needs to be emitted to update the graph.
