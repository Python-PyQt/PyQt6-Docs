.. sip:method-description::
    :status: todo
    :pysig: c41cd744fda4680dd506214f9b6b9118
    :realsig: () const
    :digest: 289562f4c01daf3c119f591535b4fe74

Can be used to get the selected custom item after receiving ``selectedElementChanged`` signal with :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.ElementType.ElementCustomItem` type. Ownership of the item remains with the graph. Selection is valid until the next ``selectedElementChanged`` signal.

Returns the pointer to the selected custom item, or null.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.selectedElement`.
