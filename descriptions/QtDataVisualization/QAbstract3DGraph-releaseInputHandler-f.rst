.. sip:method-description::
    :status: todo
    :pysig: 5fc442c544cb3bed28e2daac11185c74
    :realsig: (QAbstract3DInputHandler*)
    :digest: 958cdd3c5e89ac55fa44862d2437b466

Releases the ownership of the *inputHandler* back to the caller, if it was added to this graph. If the released *inputHandler* is in use there will be no input handler active after this call.

If the default input handler is released and added back later, it behaves as any other input handler would.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.addInputHandler`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.setActiveInputHandler`.
