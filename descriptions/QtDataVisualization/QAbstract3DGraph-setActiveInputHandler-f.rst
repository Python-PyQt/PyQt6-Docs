.. sip:method-description::
    :status: todo
    :pysig: 5fc442c544cb3bed28e2daac11185c74
    :realsig: (QAbstract3DInputHandler*)
    :digest: 8bc01da274188e9aece20767e04c9c4e

Sets *inputHandler* as the active input handler used in the graph. Implicitly calls :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.addInputHandler` to transfer ownership of *inputHandler* to this graph.

If *inputHandler* is null, no input handler will be active after this call.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.activeInputHandler`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.addInputHandler`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.releaseInputHandler`.
