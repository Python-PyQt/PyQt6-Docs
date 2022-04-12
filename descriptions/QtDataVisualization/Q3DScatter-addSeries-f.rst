.. sip:method-description::
    :status: todo
    :pysig: 52c323f408de49fb2c86cc7d485c9522
    :realsig: (QScatter3DSeries*)
    :digest: 4836d0acb9378effd15e5b022e51b22e

Adds the *series* to the graph. A graph can contain multiple series, but has only one set of axes. If the newly added series has specified a selected item, it will be highlighted and any existing selection will be cleared. Only one added series can have an active selection.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.hasSeries`.
