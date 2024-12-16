:orphan:

.. sip:class:: PyQt6.QtGraphs.QBarDataProxy
    :inherits: :sip:ref:`~PyQt6.QtGraphs.QAbstractDataProxy`
    :description: QtGraphs/QBarDataProxy-c.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QBarDataProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.addRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
        :returns:
            int
        :description: QtGraphs/QBarDataProxy-addRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.addRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
            Optional[str]
        :returns:
            int
        :description: QtGraphs/QBarDataProxy-addRow-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.addRows
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
        :returns:
            int
        :description: QtGraphs/QBarDataProxy-addRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.addRows
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
            Iterable[Optional[str]]
        :returns:
            int
        :description: QtGraphs/QBarDataProxy-addRows-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.colCount
        :returns:
            int
        :description: QtGraphs/QBarDataProxy-colCount-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
        :description: QtGraphs/QBarDataProxy-insertRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
            Optional[str]
        :description: QtGraphs/QBarDataProxy-insertRow-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.insertRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
        :description: QtGraphs/QBarDataProxy-insertRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.insertRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
            Iterable[Optional[str]]
        :description: QtGraphs/QBarDataProxy-insertRows-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QBarDataItem`
        :description: QtGraphs/QBarDataProxy-itemAt-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QBarDataItem`
        :description: QtGraphs/QBarDataProxy-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.removeRows
        :args:
            int
            int
            removeLabels: bool = False
        :description: QtGraphs/QBarDataProxy-removeRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.resetArray
        :description: QtGraphs/QBarDataProxy-resetArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.resetArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
        :description: QtGraphs/QBarDataProxy-resetArray-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.resetArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
            Iterable[Optional[str]]
            Iterable[Optional[str]]
        :description: QtGraphs/QBarDataProxy-resetArray-f-2.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.rowAt
        :args:
            int
        :returns:
            list[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
        :description: QtGraphs/QBarDataProxy-rowAt-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.rowCount
        :returns:
            int
        :description: QtGraphs/QBarDataProxy-rowCount-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.series
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QBar3DSeries`
        :description: QtGraphs/QBarDataProxy-series-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.setItem
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtGraphs.QBarDataItem`
        :description: QtGraphs/QBarDataProxy-setItem-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.setItem
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarDataItem`
        :description: QtGraphs/QBarDataProxy-setItem-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.setRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
        :description: QtGraphs/QBarDataProxy-setRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.setRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]
            Optional[str]
        :description: QtGraphs/QBarDataProxy-setRow-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.setRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
        :description: QtGraphs/QBarDataProxy-setRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarDataProxy.setRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarDataItem`]]
            Iterable[Optional[str]]
        :description: QtGraphs/QBarDataProxy-setRows-f-1.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.arrayReset
        :description: QtGraphs/QBarDataProxy-arrayReset-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.colCountChanged
        :args:
            int
        :description: QtGraphs/QBarDataProxy-colCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.itemChanged
        :args:
            int
            int
        :description: QtGraphs/QBarDataProxy-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.rowCountChanged
        :args:
            int
        :description: QtGraphs/QBarDataProxy-rowCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.rowsAdded
        :args:
            int
            int
        :description: QtGraphs/QBarDataProxy-rowsAdded-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.rowsChanged
        :args:
            int
            int
        :description: QtGraphs/QBarDataProxy-rowsChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.rowsInserted
        :args:
            int
            int
        :description: QtGraphs/QBarDataProxy-rowsInserted-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.rowsRemoved
        :args:
            int
            int
        :description: QtGraphs/QBarDataProxy-rowsRemoved-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarDataProxy.seriesChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBar3DSeries`
        :description: QtGraphs/QBarDataProxy-seriesChanged-s.rst
