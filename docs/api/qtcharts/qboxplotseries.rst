:orphan:

.. sip:class:: PyQt6.QtCharts.QBoxPlotSeries
    :inherits: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries`
    :description: QtCharts/QBoxPlotSeries-c.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCharts/QBoxPlotSeries-__init__-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.append
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :returns:
            bool
        :description: QtCharts/QBoxPlotSeries-append-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.append
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCharts.QBoxSet`]
        :returns:
            bool
        :description: QtCharts/QBoxPlotSeries-append-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.boxOutlineVisible
        :returns:
            bool
        :description: QtCharts/QBoxPlotSeries-boxOutlineVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.boxSets
        :returns:
            List[:sip:ref:`~PyQt6.QtCharts.QBoxSet`]
        :description: QtCharts/QBoxPlotSeries-boxSets-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.boxWidth
        :returns:
            float
        :description: QtCharts/QBoxPlotSeries-boxWidth-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.brush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QBoxPlotSeries-brush-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.clear
        :description: QtCharts/QBoxPlotSeries-clear-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.count
        :returns:
            int
        :description: QtCharts/QBoxPlotSeries-count-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.insert
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :returns:
            bool
        :description: QtCharts/QBoxPlotSeries-insert-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.__len__
        :returns:
            int
        :description: QtCharts/QBoxPlotSeries-__len__-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.pen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QBoxPlotSeries-pen-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.remove
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :returns:
            bool
        :description: QtCharts/QBoxPlotSeries-remove-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.setBoxOutlineVisible
        :args:
            bool
        :description: QtCharts/QBoxPlotSeries-setBoxOutlineVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.setBoxWidth
        :args:
            float
        :description: QtCharts/QBoxPlotSeries-setBoxWidth-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.setBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QBoxPlotSeries-setBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.setPen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QBoxPlotSeries-setPen-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.take
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :returns:
            bool
        :description: QtCharts/QBoxPlotSeries-take-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxPlotSeries.type
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QAbstractSeries.SeriesType`
        :description: QtCharts/QBoxPlotSeries-type-f.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.boxOutlineVisibilityChanged
        :description: QtCharts/QBoxPlotSeries-boxOutlineVisibilityChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.boxsetsAdded
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCharts.QBoxSet`]
        :description: QtCharts/QBoxPlotSeries-boxsetsAdded-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.boxsetsRemoved
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCharts.QBoxSet`]
        :description: QtCharts/QBoxPlotSeries-boxsetsRemoved-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.boxWidthChanged
        :description: QtCharts/QBoxPlotSeries-boxWidthChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.brushChanged
        :description: QtCharts/QBoxPlotSeries-brushChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.clicked
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :description: QtCharts/QBoxPlotSeries-clicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.countChanged
        :description: QtCharts/QBoxPlotSeries-countChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.doubleClicked
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :description: QtCharts/QBoxPlotSeries-doubleClicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.hovered
        :args:
            bool
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :description: QtCharts/QBoxPlotSeries-hovered-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.penChanged
        :description: QtCharts/QBoxPlotSeries-penChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.pressed
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :description: QtCharts/QBoxPlotSeries-pressed-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxPlotSeries.released
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :description: QtCharts/QBoxPlotSeries-released-s.rst
