.. sip:method-description::
    :status: todo
    :pysig: 2a53c32b7367689680e9e0639e3209f0
    :realsig: (QBar3DSeries*)
    :digest: 801bb95ac0e12eaa3bb9cab5188e197c

Adds the *series* to the graph. A graph can contain multiple series, but only one set of axes, so the rows and columns of all series must match for the visualized data to be meaningful. If the graph has multiple visible series, only the primary series will generate the row or column labels on the axes in cases where the labels are not explicitly set to the axes. If the newly added series has specified a selected bar, it will be highlighted and any existing selection will be cleared. Only one added series can have an active selection.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.seriesList`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars.primarySeries`.
