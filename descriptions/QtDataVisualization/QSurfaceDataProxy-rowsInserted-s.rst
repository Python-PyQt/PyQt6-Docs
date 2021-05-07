.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 4e38e3c7d6711fe5fc9e69354b0dae34

This signal is emitted when the number of rows specified by *count* is inserted at the position *startIndex*.

If rows are inserted into the array without calling :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy.insertRow` or :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy.insertRows`, this signal needs to be emitted to update the graph.
