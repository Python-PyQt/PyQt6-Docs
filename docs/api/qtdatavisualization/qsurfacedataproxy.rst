:orphan:

.. sip:class:: PyQt6.QtDataVisualization.QSurfaceDataProxy
    :inherits: :sip:ref:`~PyQt6.QtDataVisualization.QAbstractDataProxy`
    :description: QtDataVisualization/QSurfaceDataProxy-c.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDataVisualization/QSurfaceDataProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.addRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]
        :returns:
            int
        :description: QtDataVisualization/QSurfaceDataProxy-addRow-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.addRows
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]]
        :returns:
            int
        :description: QtDataVisualization/QSurfaceDataProxy-addRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.array
        :returns:
            list[list[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]]
        :description: QtDataVisualization/QSurfaceDataProxy-array-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.columnCount
        :returns:
            int
        :description: QtDataVisualization/QSurfaceDataProxy-columnCount-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]
        :description: QtDataVisualization/QSurfaceDataProxy-insertRow-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.insertRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]]
        :description: QtDataVisualization/QSurfaceDataProxy-insertRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`
        :description: QtDataVisualization/QSurfaceDataProxy-itemAt-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`
        :description: QtDataVisualization/QSurfaceDataProxy-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.removeRows
        :args:
            int
            int
        :description: QtDataVisualization/QSurfaceDataProxy-removeRows-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.resetArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]]
        :description: QtDataVisualization/QSurfaceDataProxy-resetArray-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.rowCount
        :returns:
            int
        :description: QtDataVisualization/QSurfaceDataProxy-rowCount-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.series
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries`
        :description: QtDataVisualization/QSurfaceDataProxy-series-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.setItem
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`
        :description: QtDataVisualization/QSurfaceDataProxy-setItem-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.setItem
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`
        :description: QtDataVisualization/QSurfaceDataProxy-setItem-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.setRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]
        :description: QtDataVisualization/QSurfaceDataProxy-setRow-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurfaceDataProxy.setRows
        :args:
            int
            Iterable[Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataItem`]]
        :description: QtDataVisualization/QSurfaceDataProxy-setRows-f.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.arrayReset
        :description: QtDataVisualization/QSurfaceDataProxy-arrayReset-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.columnCountChanged
        :args:
            int
        :description: QtDataVisualization/QSurfaceDataProxy-columnCountChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.itemChanged
        :args:
            int
            int
        :description: QtDataVisualization/QSurfaceDataProxy-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.rowCountChanged
        :args:
            int
        :description: QtDataVisualization/QSurfaceDataProxy-rowCountChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.rowsAdded
        :args:
            int
            int
        :description: QtDataVisualization/QSurfaceDataProxy-rowsAdded-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.rowsChanged
        :args:
            int
            int
        :description: QtDataVisualization/QSurfaceDataProxy-rowsChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.rowsInserted
        :args:
            int
            int
        :description: QtDataVisualization/QSurfaceDataProxy-rowsInserted-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.rowsRemoved
        :args:
            int
            int
        :description: QtDataVisualization/QSurfaceDataProxy-rowsRemoved-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurfaceDataProxy.seriesChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries`
        :description: QtDataVisualization/QSurfaceDataProxy-seriesChanged-s.rst
