:orphan:

.. sip:class:: PyQt6.QtGraphs.QAbstractSeries
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject` :sip:ref:`~PyQt6.QtQml.QQmlParserStatus`
    :description: QtGraphs/QAbstractSeries-c.rst

    .. sip:enum:: PyQt6.QtGraphs.QAbstractSeries.SeriesType
        :description: QtGraphs/QAbstractSeries-SeriesType-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractSeries.SeriesType.Area
            :description: QtGraphs/QAbstractSeries-SeriesType-Area-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractSeries.SeriesType.Bar
            :description: QtGraphs/QAbstractSeries-SeriesType-Bar-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractSeries.SeriesType.Line
            :description: QtGraphs/QAbstractSeries-SeriesType-Line-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractSeries.SeriesType.Pie
            :description: QtGraphs/QAbstractSeries-SeriesType-Pie-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractSeries.SeriesType.Scatter
            :description: QtGraphs/QAbstractSeries-SeriesType-Scatter-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractSeries.SeriesType.Spline
            :description: QtGraphs/QAbstractSeries-SeriesType-Spline-v.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.classBegin
        :description: QtGraphs/QAbstractSeries-classBegin-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.componentComplete
        :description: QtGraphs/QAbstractSeries-componentComplete-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.hide
        :description: QtGraphs/QAbstractSeries-hide-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.isHoverable
        :returns:
            bool
        :description: QtGraphs/QAbstractSeries-isHoverable-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.isSelectable
        :returns:
            bool
        :description: QtGraphs/QAbstractSeries-isSelectable-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.isVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractSeries-isVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.legendData
        :returns:
            list[:sip:ref:`~PyQt6.QtGraphs.QLegendData`]
        :description: QtGraphs/QAbstractSeries-legendData-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.name
        :returns:
            str
        :description: QtGraphs/QAbstractSeries-name-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.opacity
        :returns:
            float
        :description: QtGraphs/QAbstractSeries-opacity-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.setHoverable
        :args:
            bool
        :description: QtGraphs/QAbstractSeries-setHoverable-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.setName
        :args:
            Optional[str]
        :description: QtGraphs/QAbstractSeries-setName-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.setOpacity
        :args:
            float
        :description: QtGraphs/QAbstractSeries-setOpacity-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.setSelectable
        :args:
            bool
        :description: QtGraphs/QAbstractSeries-setSelectable-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.setValuesMultiplier
        :args:
            float
        :description: QtGraphs/QAbstractSeries-setValuesMultiplier-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.setVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractSeries-setVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.show
        :description: QtGraphs/QAbstractSeries-show-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.type
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QAbstractSeries.SeriesType`
        :description: QtGraphs/QAbstractSeries-type-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractSeries.valuesMultiplier
        :returns:
            float
        :description: QtGraphs/QAbstractSeries-valuesMultiplier-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.hover
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGraphs/QAbstractSeries-hover-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.hoverableChanged
        :description: QtGraphs/QAbstractSeries-hoverableChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.hoverEnter
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGraphs/QAbstractSeries-hoverEnter-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.hoverExit
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGraphs/QAbstractSeries-hoverExit-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.legendDataChanged
        :description: QtGraphs/QAbstractSeries-legendDataChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.nameChanged
        :description: QtGraphs/QAbstractSeries-nameChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.opacityChanged
        :description: QtGraphs/QAbstractSeries-opacityChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.selectableChanged
        :description: QtGraphs/QAbstractSeries-selectableChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.valuesMultiplierChanged
        :description: QtGraphs/QAbstractSeries-valuesMultiplierChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractSeries.visibleChanged
        :description: QtGraphs/QAbstractSeries-visibleChanged-s.rst
