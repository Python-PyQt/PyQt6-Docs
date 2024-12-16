:orphan:

.. sip:class:: PyQt6.QtCharts.QAbstractSeries
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCharts/QAbstractSeries-c.rst

    .. sip:enum:: PyQt6.QtCharts.QAbstractSeries.SeriesType
        :description: QtCharts/QAbstractSeries-SeriesType-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeArea
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeArea-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeBar
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeBar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeBoxPlot
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeBoxPlot-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeCandlestick
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeCandlestick-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeHorizontalBar
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeHorizontalBar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeHorizontalPercentBar
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeHorizontalPercentBar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeHorizontalStackedBar
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeHorizontalStackedBar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeLine
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeLine-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypePercentBar
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypePercentBar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypePie
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypePie-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeScatter
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeScatter-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeSpline
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeSpline-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractSeries.SeriesType.SeriesTypeStackedBar
            :description: QtCharts/QAbstractSeries-SeriesType-SeriesTypeStackedBar-v.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.attachAxis
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis`
        :returns:
            bool
        :description: QtCharts/QAbstractSeries-attachAxis-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.attachedAxes
        :returns:
            list[:sip:ref:`~PyQt6.QtCharts.QAbstractAxis`]
        :description: QtCharts/QAbstractSeries-attachedAxes-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.chart
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QChart`
        :description: QtCharts/QAbstractSeries-chart-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.detachAxis
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis`
        :returns:
            bool
        :description: QtCharts/QAbstractSeries-detachAxis-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.hide
        :description: QtCharts/QAbstractSeries-hide-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.isVisible
        :returns:
            bool
        :description: QtCharts/QAbstractSeries-isVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.name
        :returns:
            str
        :description: QtCharts/QAbstractSeries-name-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.opacity
        :returns:
            float
        :description: QtCharts/QAbstractSeries-opacity-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.setName
        :args:
            Optional[str]
        :description: QtCharts/QAbstractSeries-setName-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.setOpacity
        :args:
            float
        :description: QtCharts/QAbstractSeries-setOpacity-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.setUseOpenGL
        :args:
            enable: bool = True
        :description: QtCharts/QAbstractSeries-setUseOpenGL-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.setVisible
        :args:
            visible: bool = True
        :description: QtCharts/QAbstractSeries-setVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.show
        :description: QtCharts/QAbstractSeries-show-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.type
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QAbstractSeries.SeriesType`
        :description: QtCharts/QAbstractSeries-type-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractSeries.useOpenGL
        :returns:
            bool
        :description: QtCharts/QAbstractSeries-useOpenGL-f.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractSeries.nameChanged
        :description: QtCharts/QAbstractSeries-nameChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractSeries.opacityChanged
        :description: QtCharts/QAbstractSeries-opacityChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractSeries.useOpenGLChanged
        :description: QtCharts/QAbstractSeries-useOpenGLChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractSeries.visibleChanged
        :description: QtCharts/QAbstractSeries-visibleChanged-s.rst
