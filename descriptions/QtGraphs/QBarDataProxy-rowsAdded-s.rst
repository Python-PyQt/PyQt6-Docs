.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qsizetype, qsizetype)
    :digest: eea367b15ca4cab6624b05b4a4973320

This signal is emitted when the number of rows specified by *count* is added, starting at the position *startIndex*. If rows are added to the array without calling :sip:ref:`~PyQt6.QtGraphs.QBarDataProxy.addRow` or :sip:ref:`~PyQt6.QtGraphs.QBarDataProxy.addRows`, this signal needs to be emitted to update the graph.
