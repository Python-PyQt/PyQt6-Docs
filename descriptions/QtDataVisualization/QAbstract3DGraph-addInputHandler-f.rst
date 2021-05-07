.. sip:method-description::
    :status: todo
    :pysig: 5fc442c544cb3bed28e2daac11185c74
    :realsig: (QAbstract3DInputHandler*)
    :digest: d0809bdaf001280b5675ac02ab436304

Adds the given *inputHandler* to the graph. The input handlers added via  are not taken in to use directly. Only the ownership of the *inputHandler* is given to the graph. The *inputHandler* must not be null or already added to another graph.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.releaseInputHandler`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.setActiveInputHandler`.
