.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 60f6b8394b0d5a605c2e84fa83516335

Can be used to query the index of the selected custom item after receiving ``selectedElementChanged`` signal with :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.ElementType.ElementCustomItem` type. Selection is valid until the next ``selectedElementChanged`` signal.

Returns the index of the selected custom item, or -1.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.selectedElement`.
