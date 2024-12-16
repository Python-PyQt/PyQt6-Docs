:orphan:

.. sip:class:: PyQt6.QtDataVisualization.QBarDataProxy
    :inherits: :sip:ref:`~PyQt6.QtDataVisualization.QAbstractDataProxy`
    :description: QtDataVisualization/QBarDataProxy-c.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDataVisualization/QBarDataProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.addRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
        :returns:
            int
        :description: QtDataVisualization/QBarDataProxy-addRow-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.addRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
            Optional[str]
        :returns:
            int
        :description: QtDataVisualization/QBarDataProxy-addRow-f-2.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.addRows
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
        :returns:
            int
        :description: QtDataVisualization/QBarDataProxy-addRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.addRows
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
            Iterable[Optional[str]]
        :returns:
            int
        :description: QtDataVisualization/QBarDataProxy-addRows-f-2.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.array
        :returns:
            list[list[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
        :description: QtDataVisualization/QBarDataProxy-array-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.columnLabels
        :returns:
            list[str]
        :description: QtDataVisualization/QBarDataProxy-columnLabels-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
        :description: QtDataVisualization/QBarDataProxy-insertRow-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
            Optional[str]
        :description: QtDataVisualization/QBarDataProxy-insertRow-f-2.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.insertRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
        :description: QtDataVisualization/QBarDataProxy-insertRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.insertRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
            Iterable[Optional[str]]
        :description: QtDataVisualization/QBarDataProxy-insertRows-f-2.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`
        :description: QtDataVisualization/QBarDataProxy-itemAt-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`
        :description: QtDataVisualization/QBarDataProxy-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.removeRows
        :args:
            int
            int
            removeLabels: bool = True
        :description: QtDataVisualization/QBarDataProxy-removeRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.resetArray
        :description: QtDataVisualization/QBarDataProxy-resetArray-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.resetArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
        :description: QtDataVisualization/QBarDataProxy-resetArray-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.resetArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
            Iterable[Optional[str]]
            Iterable[Optional[str]]
        :description: QtDataVisualization/QBarDataProxy-resetArray-f-3.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.rowAt
        :args:
            int
        :returns:
            list[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
        :description: QtDataVisualization/QBarDataProxy-rowAt-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.rowCount
        :returns:
            int
        :description: QtDataVisualization/QBarDataProxy-rowCount-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.rowLabels
        :returns:
            list[str]
        :description: QtDataVisualization/QBarDataProxy-rowLabels-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.series
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QBar3DSeries`
        :description: QtDataVisualization/QBarDataProxy-series-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setColumnLabels
        :args:
            Iterable[Optional[str]]
        :description: QtDataVisualization/QBarDataProxy-setColumnLabels-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setItem
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`
        :description: QtDataVisualization/QBarDataProxy-setItem-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setItem
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`
        :description: QtDataVisualization/QBarDataProxy-setItem-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
        :description: QtDataVisualization/QBarDataProxy-setRow-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]
            Optional[str]
        :description: QtDataVisualization/QBarDataProxy-setRow-f-2.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setRowLabels
        :args:
            Iterable[Optional[str]]
        :description: QtDataVisualization/QBarDataProxy-setRowLabels-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
        :description: QtDataVisualization/QBarDataProxy-setRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QBarDataProxy.setRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QBarDataItem`]]
            Iterable[Optional[str]]
        :description: QtDataVisualization/QBarDataProxy-setRows-f-2.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.arrayReset
        :description: QtDataVisualization/QBarDataProxy-arrayReset-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.columnLabelsChanged
        :description: QtDataVisualization/QBarDataProxy-columnLabelsChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.itemChanged
        :args:
            int
            int
        :description: QtDataVisualization/QBarDataProxy-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.rowCountChanged
        :args:
            int
        :description: QtDataVisualization/QBarDataProxy-rowCountChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.rowLabelsChanged
        :description: QtDataVisualization/QBarDataProxy-rowLabelsChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.rowsAdded
        :args:
            int
            int
        :description: QtDataVisualization/QBarDataProxy-rowsAdded-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.rowsChanged
        :args:
            int
            int
        :description: QtDataVisualization/QBarDataProxy-rowsChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.rowsInserted
        :args:
            int
            int
        :description: QtDataVisualization/QBarDataProxy-rowsInserted-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.rowsRemoved
        :args:
            int
            int
        :description: QtDataVisualization/QBarDataProxy-rowsRemoved-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QBarDataProxy.seriesChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QBar3DSeries`
        :description: QtDataVisualization/QBarDataProxy-seriesChanged-s.rst
