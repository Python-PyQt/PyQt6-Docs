.. sip:method-description::
    :status: todo
    :pysig: b4c80c5a80cc29c6bcb56487d2b3efe6
    :realsig: (QSurface3DSeries*)
    :digest: 4836d0acb9378effd15e5b022e51b22e

Adds the *series* to the graph. A graph can contain multiple series, but has only one set of axes. If the newly added series has specified a selected item, it will be highlighted and any existing selection will be cleared. Only one added series can have an active selection.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.hasSeries`.
