:orphan:

.. sip:class:: PyQt6.QtGraphs.QSurfaceDataProxy
    :inherits: :sip:ref:`~PyQt6.QtGraphs.QAbstractDataProxy`
    :description: QtGraphs/QSurfaceDataProxy-c.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QSurfaceDataProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.addRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]
        :returns:
            int
        :description: QtGraphs/QSurfaceDataProxy-addRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.addRows
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :returns:
            int
        :description: QtGraphs/QSurfaceDataProxy-addRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.columnCount
        :returns:
            int
        :description: QtGraphs/QSurfaceDataProxy-columnCount-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]
        :description: QtGraphs/QSurfaceDataProxy-insertRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.insertRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :description: QtGraphs/QSurfaceDataProxy-insertRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`
        :description: QtGraphs/QSurfaceDataProxy-itemAt-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`
        :description: QtGraphs/QSurfaceDataProxy-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.removeRows
        :args:
            int
            int
        :description: QtGraphs/QSurfaceDataProxy-removeRows-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.resetArray
        :description: QtGraphs/QSurfaceDataProxy-resetArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.resetArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :description: QtGraphs/QSurfaceDataProxy-resetArray-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.rowCount
        :returns:
            int
        :description: QtGraphs/QSurfaceDataProxy-rowCount-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.series
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries`
        :description: QtGraphs/QSurfaceDataProxy-series-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.setItem
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`
        :description: QtGraphs/QSurfaceDataProxy-setItem-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.setItem
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`
        :description: QtGraphs/QSurfaceDataProxy-setItem-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.setRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]
        :description: QtGraphs/QSurfaceDataProxy-setRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurfaceDataProxy.setRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :description: QtGraphs/QSurfaceDataProxy-setRows-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.arrayReset
        :description: QtGraphs/QSurfaceDataProxy-arrayReset-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.columnCountChanged
        :args:
            int
        :description: QtGraphs/QSurfaceDataProxy-columnCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.itemChanged
        :args:
            int
            int
        :description: QtGraphs/QSurfaceDataProxy-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.rowCountChanged
        :args:
            int
        :description: QtGraphs/QSurfaceDataProxy-rowCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.rowsAdded
        :args:
            int
            int
        :description: QtGraphs/QSurfaceDataProxy-rowsAdded-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.rowsChanged
        :args:
            int
            int
        :description: QtGraphs/QSurfaceDataProxy-rowsChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.rowsInserted
        :args:
            int
            int
        :description: QtGraphs/QSurfaceDataProxy-rowsInserted-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.rowsRemoved
        :args:
            int
            int
        :description: QtGraphs/QSurfaceDataProxy-rowsRemoved-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurfaceDataProxy.seriesChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries`
        :description: QtGraphs/QSurfaceDataProxy-seriesChanged-s.rst
