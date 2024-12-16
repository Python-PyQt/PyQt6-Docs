:orphan:

.. sip:class:: PyQt6.QtDataVisualization.QScatterDataProxy
    :inherits: :sip:ref:`~PyQt6.QtDataVisualization.QAbstractDataProxy`
    :description: QtDataVisualization/QScatterDataProxy-c.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDataVisualization/QScatterDataProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.addItem
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`
        :returns:
            int
        :description: QtDataVisualization/QScatterDataProxy-addItem-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.addItems
        :args:
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`]
        :returns:
            int
        :description: QtDataVisualization/QScatterDataProxy-addItems-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.array
        :returns:
            list[:sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`]
        :description: QtDataVisualization/QScatterDataProxy-array-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.insertItem
        :args:
            int
            :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`
        :description: QtDataVisualization/QScatterDataProxy-insertItem-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.insertItems
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`]
        :description: QtDataVisualization/QScatterDataProxy-insertItems-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.itemAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`
        :description: QtDataVisualization/QScatterDataProxy-itemAt-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.itemCount
        :returns:
            int
        :description: QtDataVisualization/QScatterDataProxy-itemCount-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.removeItems
        :args:
            int
            int
        :description: QtDataVisualization/QScatterDataProxy-removeItems-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.resetArray
        :args:
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`]
        :description: QtDataVisualization/QScatterDataProxy-resetArray-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.series
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries`
        :description: QtDataVisualization/QScatterDataProxy-series-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.setItem
        :args:
            int
            :sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`
        :description: QtDataVisualization/QScatterDataProxy-setItem-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QScatterDataProxy.setItems
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtDataVisualization.QScatterDataItem`]
        :description: QtDataVisualization/QScatterDataProxy-setItems-f.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.arrayReset
        :description: QtDataVisualization/QScatterDataProxy-arrayReset-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.itemCountChanged
        :args:
            int
        :description: QtDataVisualization/QScatterDataProxy-itemCountChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.itemsAdded
        :args:
            int
            int
        :description: QtDataVisualization/QScatterDataProxy-itemsAdded-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.itemsChanged
        :args:
            int
            int
        :description: QtDataVisualization/QScatterDataProxy-itemsChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.itemsInserted
        :args:
            int
            int
        :description: QtDataVisualization/QScatterDataProxy-itemsInserted-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.itemsRemoved
        :args:
            int
            int
        :description: QtDataVisualization/QScatterDataProxy-itemsRemoved-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QScatterDataProxy.seriesChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QScatter3DSeries`
        :description: QtDataVisualization/QScatterDataProxy-seriesChanged-s.rst
