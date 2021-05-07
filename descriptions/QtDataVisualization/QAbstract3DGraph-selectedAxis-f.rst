.. sip:method-description::
    :status: todo
    :pysig: 929c9801a762c543b67465c2eb7bdf15
    :realsig: () const
    :digest: 4ea4e344a1fa1d0c89bdd3b67999ca1e

Can be used to get the selected axis after receiving ``selectedElementChanged`` signal with any label type. Selection is valid until the next ``selectedElementChanged`` signal.

Returns the pointer to the selected axis, or null.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.selectedElement`.
