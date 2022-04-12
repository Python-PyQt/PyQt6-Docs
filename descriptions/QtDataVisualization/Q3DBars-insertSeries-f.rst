.. sip:method-description::
    :status: todo
    :pysig: 2e6e788a3c4e6f79922dd351a668dc52
    :realsig: (int,QBar3DSeries*)
    :digest: 30a39c88984830d7a428cd91cfb5f2de

Inserts the *series* into the position *index* in the series list. If the *series* has already been added to the list, it is moved to the new *index*.

**Note:** When moving a series to a new *index* that is after its old index, the new position in list is calculated as if the series was still in its old index, so the final index is actually the *index* decremented by one.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addSeries`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.seriesList`, :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.hasSeries`.
