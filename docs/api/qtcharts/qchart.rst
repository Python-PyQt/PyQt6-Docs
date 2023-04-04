:orphan:

.. sip:class:: PyQt6.QtCharts.QChart
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget`
    :description: QtCharts/QChart-c.rst

    .. sip:enum:: PyQt6.QtCharts.QChart.AnimationOption
        :description: QtCharts/QChart-AnimationOption-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.AnimationOption.AllAnimations
            :description: QtCharts/QChart-AnimationOption-AllAnimations-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.AnimationOption.GridAxisAnimations
            :description: QtCharts/QChart-AnimationOption-GridAxisAnimations-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.AnimationOption.NoAnimation
            :description: QtCharts/QChart-AnimationOption-NoAnimation-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.AnimationOption.SeriesAnimations
            :description: QtCharts/QChart-AnimationOption-SeriesAnimations-v.rst

    .. sip:enum:: PyQt6.QtCharts.QChart.ChartTheme
        :description: QtCharts/QChart-ChartTheme-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeBlueCerulean
            :description: QtCharts/QChart-ChartTheme-ChartThemeBlueCerulean-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeBlueIcy
            :description: QtCharts/QChart-ChartTheme-ChartThemeBlueIcy-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeBlueNcs
            :description: QtCharts/QChart-ChartTheme-ChartThemeBlueNcs-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeBrownSand
            :description: QtCharts/QChart-ChartTheme-ChartThemeBrownSand-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeDark
            :description: QtCharts/QChart-ChartTheme-ChartThemeDark-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeHighContrast
            :description: QtCharts/QChart-ChartTheme-ChartThemeHighContrast-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeLight
            :description: QtCharts/QChart-ChartTheme-ChartThemeLight-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartTheme.ChartThemeQt
            :description: QtCharts/QChart-ChartTheme-ChartThemeQt-v.rst

    .. sip:enum:: PyQt6.QtCharts.QChart.ChartType
        :description: QtCharts/QChart-ChartType-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartType.ChartTypeCartesian
            :description: QtCharts/QChart-ChartType-ChartTypeCartesian-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartType.ChartTypePolar
            :description: QtCharts/QChart-ChartType-ChartTypePolar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QChart.ChartType.ChartTypeUndefined
            :description: QtCharts/QChart-ChartType-ChartTypeUndefined-v.rst

    .. sip:method:: PyQt6.QtCharts.QChart.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtCharts/QChart-__init__-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.addAxis
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis`
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtCharts/QChart-addAxis-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.addSeries
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractSeries`
        :description: QtCharts/QChart-addSeries-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.animationDuration
        :returns:
            int
        :description: QtCharts/QChart-animationDuration-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.animationEasingCurve
        :returns:
            :sip:ref:`~PyQt6.QtCore.QEasingCurve`
        :description: QtCharts/QChart-animationEasingCurve-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.animationOptions
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QChart.AnimationOption`
        :description: QtCharts/QChart-animationOptions-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.axes
        :args:
            orientation: :sip:ref:`~PyQt6.QtCore.Qt.Orientation` = Qt.Horizontal|Qt.Vertical
            series: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries` = None
        :returns:
            List[:sip:ref:`~PyQt6.QtCharts.QAbstractAxis`]
        :description: QtCharts/QChart-axes-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.backgroundBrush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QChart-backgroundBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.backgroundPen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QChart-backgroundPen-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.backgroundRoundness
        :returns:
            float
        :description: QtCharts/QChart-backgroundRoundness-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.chartType
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QChart.ChartType`
        :description: QtCharts/QChart-chartType-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.createDefaultAxes
        :description: QtCharts/QChart-createDefaultAxes-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.isBackgroundVisible
        :returns:
            bool
        :description: QtCharts/QChart-isBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.isDropShadowEnabled
        :returns:
            bool
        :description: QtCharts/QChart-isDropShadowEnabled-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.isPlotAreaBackgroundVisible
        :returns:
            bool
        :description: QtCharts/QChart-isPlotAreaBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.isZoomed
        :returns:
            bool
        :description: QtCharts/QChart-isZoomed-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.legend
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QLegend`
        :description: QtCharts/QChart-legend-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtCharts/QChart-locale-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.localizeNumbers
        :returns:
            bool
        :description: QtCharts/QChart-localizeNumbers-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.mapToPosition
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            series: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries` = None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QChart-mapToPosition-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.mapToValue
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            series: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries` = None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QChart-mapToValue-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.margins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtCharts/QChart-margins-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.plotArea
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtCharts/QChart-plotArea-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.plotAreaBackgroundBrush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QChart-plotAreaBackgroundBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.plotAreaBackgroundPen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QChart-plotAreaBackgroundPen-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.removeAllSeries
        :description: QtCharts/QChart-removeAllSeries-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.removeAxis
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis`
        :description: QtCharts/QChart-removeAxis-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.removeSeries
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractSeries`
        :description: QtCharts/QChart-removeSeries-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.scroll
        :args:
            float
            float
        :description: QtCharts/QChart-scroll-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.series
        :returns:
            List[:sip:ref:`~PyQt6.QtCharts.QAbstractSeries`]
        :description: QtCharts/QChart-series-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setAnimationDuration
        :args:
            int
        :description: QtCharts/QChart-setAnimationDuration-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setAnimationEasingCurve
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QEasingCurve`, :sip:ref:`~PyQt6.QtCore.QEasingCurve.Type`]
        :description: QtCharts/QChart-setAnimationEasingCurve-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setAnimationOptions
        :args:
            :sip:ref:`~PyQt6.QtCharts.QChart.AnimationOption`
        :description: QtCharts/QChart-setAnimationOptions-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setBackgroundBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QChart-setBackgroundBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setBackgroundPen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QChart-setBackgroundPen-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setBackgroundRoundness
        :args:
            float
        :description: QtCharts/QChart-setBackgroundRoundness-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setBackgroundVisible
        :args:
            visible: bool = True
        :description: QtCharts/QChart-setBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setDropShadowEnabled
        :args:
            enabled: bool = True
        :description: QtCharts/QChart-setDropShadowEnabled-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setLocale
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtCharts/QChart-setLocale-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setLocalizeNumbers
        :args:
            bool
        :description: QtCharts/QChart-setLocalizeNumbers-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtCharts/QChart-setMargins-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setPlotArea
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtCharts/QChart-setPlotArea-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setPlotAreaBackgroundBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QChart-setPlotAreaBackgroundBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setPlotAreaBackgroundPen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QChart-setPlotAreaBackgroundPen-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setPlotAreaBackgroundVisible
        :args:
            visible: bool = True
        :description: QtCharts/QChart-setPlotAreaBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setTheme
        :args:
            :sip:ref:`~PyQt6.QtCharts.QChart.ChartTheme`
        :description: QtCharts/QChart-setTheme-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setTitle
        :args:
            str
        :description: QtCharts/QChart-setTitle-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setTitleBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QChart-setTitleBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.setTitleFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QChart-setTitleFont-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.theme
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QChart.ChartTheme`
        :description: QtCharts/QChart-theme-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.title
        :returns:
            str
        :description: QtCharts/QChart-title-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.titleBrush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QChart-titleBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.titleFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QChart-titleFont-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.zoom
        :args:
            float
        :description: QtCharts/QChart-zoom-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.zoomIn
        :description: QtCharts/QChart-zoomIn-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.zoomIn
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtCharts/QChart-zoomIn-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QChart.zoomOut
        :description: QtCharts/QChart-zoomOut-f.rst

    .. sip:method:: PyQt6.QtCharts.QChart.zoomReset
        :description: QtCharts/QChart-zoomReset-f.rst

    .. sip:signal:: PyQt6.QtCharts.QChart.plotAreaChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtCharts/QChart-plotAreaChanged-s.rst
