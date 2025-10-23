:orphan:

.. sip:class:: PyQt6.QtGraphs.QScatterDataProxy
    :inherits: :sip:ref:`~PyQt6.QtGraphs.QAbstractDataProxy`
    :description: QtGraphs/QScatterDataProxy-c.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QScatterDataProxy-__init__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.addItem
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`
        :returns:
            int
        :description: QtGraphs/QScatterDataProxy-addItem-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.addItems
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`]
        :returns:
            int
        :description: QtGraphs/QScatterDataProxy-addItems-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.insertItem
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`
        :description: QtGraphs/QScatterDataProxy-insertItem-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.insertItems
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`]
        :description: QtGraphs/QScatterDataProxy-insertItems-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.itemAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`
        :description: QtGraphs/QScatterDataProxy-itemAt-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.itemCount
        :returns:
            int
        :description: QtGraphs/QScatterDataProxy-itemCount-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.removeItems
        :args:
            int
            int
        :description: QtGraphs/QScatterDataProxy-removeItems-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.resetArray
        :description: QtGraphs/QScatterDataProxy-resetArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.resetArray
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`]
        :description: QtGraphs/QScatterDataProxy-resetArray-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.resetScaleArray
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGui.QVector3D`]
        :description: QtGraphs/QScatterDataProxy-resetScaleArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.scaleAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: QtGraphs/QScatterDataProxy-scaleAt-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.series
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QScatter3DSeries`
        :description: QtGraphs/QScatterDataProxy-series-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.setItem
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`
        :description: QtGraphs/QScatterDataProxy-setItem-f.rst

    .. sip:method:: PyQt6.QtGraphs.QScatterDataProxy.setItems
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QScatterDataItem`]
        :description: QtGraphs/QScatterDataProxy-setItems-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.arrayReset
        :description: QtGraphs/QScatterDataProxy-arrayReset-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.itemCountChanged
        :args:
            int
        :description: QtGraphs/QScatterDataProxy-itemCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.itemsAdded
        :args:
            int
            int
        :description: QtGraphs/QScatterDataProxy-itemsAdded-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.itemsChanged
        :args:
            int
            int
        :description: QtGraphs/QScatterDataProxy-itemsChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.itemsInserted
        :args:
            int
            int
        :description: QtGraphs/QScatterDataProxy-itemsInserted-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.itemsRemoved
        :args:
            int
            int
        :description: QtGraphs/QScatterDataProxy-itemsRemoved-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.scaleArrayReset
        :description: QtGraphs/QScatterDataProxy-scaleArrayReset-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QScatterDataProxy.seriesChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QScatter3DSeries`
        :description: QtGraphs/QScatterDataProxy-seriesChanged-s.rst
