.. sip:method-description::
    :status: todo
    :pysig: 2e6e788a3c4e6f79922dd351a668dc52
    :realsig: (int,QBar3DSeries*)
    :digest: 885ad8e541eba451b3c7722404e65a3d

Inserts the *series* into the position *index* in the series list. If the *series* has already been added to the list, it is moved to the new *index*.

**Note:** When moving a series to a new *index* that is after its old index, the new position in list is calculated as if the series was still in its old index, so the final index is actually the *index* decremented by one.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.addSeries`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.seriesList`.
