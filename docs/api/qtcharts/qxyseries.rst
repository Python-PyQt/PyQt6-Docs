:orphan:

.. sip:class:: PyQt6.QtCharts.QXYSeries
    :inherits: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries`
    :description: QtCharts/QXYSeries-c.rst

    .. sip:enum:: PyQt6.QtCharts.QXYSeries.PointConfiguration
        :description: QtCharts/QXYSeries-PointConfiguration-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QXYSeries.PointConfiguration.Color
            :description: QtCharts/QXYSeries-PointConfiguration-Color-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QXYSeries.PointConfiguration.LabelFormat
            :description: QtCharts/QXYSeries-PointConfiguration-LabelFormat-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QXYSeries.PointConfiguration.LabelVisibility
            :description: QtCharts/QXYSeries-PointConfiguration-LabelVisibility-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QXYSeries.PointConfiguration.Size
            :description: QtCharts/QXYSeries-PointConfiguration-Size-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QXYSeries.PointConfiguration.Visibility
            :description: QtCharts/QXYSeries-PointConfiguration-Visibility-v.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.append
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-append-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.append
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QPointF`]
        :description: QtCharts/QXYSeries-append-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.append
        :args:
            float
            float
        :description: QtCharts/QXYSeries-append-f-2.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.at
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-at-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.bestFitLineColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QXYSeries-bestFitLineColor-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.bestFitLineEquation
        :returns:
            Tuple[float, float]
            bool
        :description: QtCharts/QXYSeries-bestFitLineEquation-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.bestFitLinePen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QXYSeries-bestFitLinePen-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.bestFitLineVisible
        :returns:
            bool
        :description: QtCharts/QXYSeries-bestFitLineVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.brush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QXYSeries-brush-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.clear
        :description: QtCharts/QXYSeries-clear-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.clearPointConfiguration
        :args:
            int
        :description: QtCharts/QXYSeries-clearPointConfiguration-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.clearPointConfiguration
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`
        :description: QtCharts/QXYSeries-clearPointConfiguration-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.clearPointsConfiguration
        :description: QtCharts/QXYSeries-clearPointsConfiguration-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.clearPointsConfiguration
        :args:
            :sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`
        :description: QtCharts/QXYSeries-clearPointsConfiguration-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.color
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QXYSeries-color-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.colorBy
        :args:
            Iterable[float]
            gradient: :sip:ref:`~PyQt6.QtGui.QLinearGradient` = QLinearGradient()
        :description: QtCharts/QXYSeries-colorBy-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.count
        :returns:
            int
        :description: QtCharts/QXYSeries-count-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.deselectAllPoints
        :description: QtCharts/QXYSeries-deselectAllPoints-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.deselectPoint
        :args:
            int
        :description: QtCharts/QXYSeries-deselectPoint-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.deselectPoints
        :args:
            Iterable[int]
        :description: QtCharts/QXYSeries-deselectPoints-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.insert
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-insert-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.isPointSelected
        :args:
            int
        :returns:
            bool
        :description: QtCharts/QXYSeries-isPointSelected-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.__len__
        :returns:
            int
        :description: QtCharts/QXYSeries-__len__-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.lightMarker
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtCharts/QXYSeries-lightMarker-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.__lshift__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QXYSeries`
        :description: QtCharts/QXYSeries-__lshift__-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.__lshift__
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QPointF`]
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QXYSeries`
        :description: QtCharts/QXYSeries-__lshift__-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.markerSize
        :returns:
            float
        :description: QtCharts/QXYSeries-markerSize-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QXYSeries-pen-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointConfiguration
        :args:
            int
        :returns:
            Dict[:sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`, Any]
        :description: QtCharts/QXYSeries-pointConfiguration-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointLabelsClipping
        :returns:
            bool
        :description: QtCharts/QXYSeries-pointLabelsClipping-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointLabelsColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QXYSeries-pointLabelsColor-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointLabelsFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QXYSeries-pointLabelsFont-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointLabelsFormat
        :returns:
            str
        :description: QtCharts/QXYSeries-pointLabelsFormat-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointLabelsVisible
        :returns:
            bool
        :description: QtCharts/QXYSeries-pointLabelsVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.points
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QPointF`]
        :description: QtCharts/QXYSeries-points-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointsConfiguration
        :returns:
            Dict[int, Dict[:sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`, Any]]
        :description: QtCharts/QXYSeries-pointsConfiguration-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.pointsVisible
        :returns:
            bool
        :description: QtCharts/QXYSeries-pointsVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.remove
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-remove-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.remove
        :args:
            int
        :description: QtCharts/QXYSeries-remove-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.remove
        :args:
            float
            float
        :description: QtCharts/QXYSeries-remove-f-2.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.removePoints
        :args:
            int
            int
        :description: QtCharts/QXYSeries-removePoints-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.replace
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QPointF`]
        :description: QtCharts/QXYSeries-replace-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.replace
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-replace-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.replace
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-replace-f-2.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.replace
        :args:
            int
            float
            float
        :description: QtCharts/QXYSeries-replace-f-3.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.replace
        :args:
            float
            float
            float
            float
        :description: QtCharts/QXYSeries-replace-f-4.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.selectAllPoints
        :description: QtCharts/QXYSeries-selectAllPoints-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.selectedColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QXYSeries-selectedColor-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.selectedLightMarker
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtCharts/QXYSeries-selectedLightMarker-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.selectedPoints
        :returns:
            List[int]
        :description: QtCharts/QXYSeries-selectedPoints-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.selectPoint
        :args:
            int
        :description: QtCharts/QXYSeries-selectPoint-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.selectPoints
        :args:
            Iterable[int]
        :description: QtCharts/QXYSeries-selectPoints-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setBestFitLineColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-setBestFitLineColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setBestFitLinePen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtCharts/QXYSeries-setBestFitLinePen-f-2.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setBestFitLineVisible
        :args:
            visible: bool = True
        :description: QtCharts/QXYSeries-setBestFitLineVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QXYSeries-setBrush-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-setColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setLightMarker
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtCharts/QXYSeries-setLightMarker-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setMarkerSize
        :args:
            float
        :description: QtCharts/QXYSeries-setMarkerSize-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtCharts/QXYSeries-setPen-f-2.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointConfiguration
        :args:
            int
            Dict[:sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`, Any]
        :description: QtCharts/QXYSeries-setPointConfiguration-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointConfiguration
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`
            Any
        :description: QtCharts/QXYSeries-setPointConfiguration-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointLabelsClipping
        :args:
            enable: bool = True
        :description: QtCharts/QXYSeries-setPointLabelsClipping-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointLabelsColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-setPointLabelsColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointLabelsFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QXYSeries-setPointLabelsFont-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointLabelsFormat
        :args:
            Optional[str]
        :description: QtCharts/QXYSeries-setPointLabelsFormat-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointLabelsVisible
        :args:
            visible: bool = True
        :description: QtCharts/QXYSeries-setPointLabelsVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointsConfiguration
        :args:
            Dict[int, Dict[:sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`, Any]]
        :description: QtCharts/QXYSeries-setPointsConfiguration-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointSelected
        :args:
            int
            bool
        :description: QtCharts/QXYSeries-setPointSelected-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setPointsVisible
        :args:
            visible: bool = True
        :description: QtCharts/QXYSeries-setPointsVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setSelectedColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-setSelectedColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.setSelectedLightMarker
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtCharts/QXYSeries-setSelectedLightMarker-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.sizeBy
        :args:
            Iterable[float]
            float
            float
        :description: QtCharts/QXYSeries-sizeBy-f.rst

    .. sip:method:: PyQt6.QtCharts.QXYSeries.toggleSelection
        :args:
            Iterable[int]
        :description: QtCharts/QXYSeries-toggleSelection-f.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.bestFitLineColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-bestFitLineColorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.bestFitLinePenChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtCharts/QXYSeries-bestFitLinePenChanged-s-2.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.bestFitLineVisibilityChanged
        :args:
            bool
        :description: QtCharts/QXYSeries-bestFitLineVisibilityChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.clicked
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-clicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.colorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-colorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.doubleClicked
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-doubleClicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.hovered
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            bool
        :description: QtCharts/QXYSeries-hovered-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.lightMarkerChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtCharts/QXYSeries-lightMarkerChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.markerSizeChanged
        :args:
            float
        :description: QtCharts/QXYSeries-markerSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.penChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtCharts/QXYSeries-penChanged-s-2.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointAdded
        :args:
            int
        :description: QtCharts/QXYSeries-pointAdded-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointLabelsClippingChanged
        :args:
            bool
        :description: QtCharts/QXYSeries-pointLabelsClippingChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointLabelsColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-pointLabelsColorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointLabelsFontChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QXYSeries-pointLabelsFontChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointLabelsFormatChanged
        :args:
            Optional[str]
        :description: QtCharts/QXYSeries-pointLabelsFormatChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointLabelsVisibilityChanged
        :args:
            bool
        :description: QtCharts/QXYSeries-pointLabelsVisibilityChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointRemoved
        :args:
            int
        :description: QtCharts/QXYSeries-pointRemoved-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointReplaced
        :args:
            int
        :description: QtCharts/QXYSeries-pointReplaced-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointsConfigurationChanged
        :args:
            Dict[int, Dict[:sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration`, Any]]
        :description: QtCharts/QXYSeries-pointsConfigurationChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointsRemoved
        :args:
            int
            int
        :description: QtCharts/QXYSeries-pointsRemoved-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pointsReplaced
        :description: QtCharts/QXYSeries-pointsReplaced-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.pressed
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-pressed-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.released
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtCharts/QXYSeries-released-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.selectedColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QXYSeries-selectedColorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.selectedLightMarkerChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtCharts/QXYSeries-selectedLightMarkerChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QXYSeries.selectedPointsChanged
        :description: QtCharts/QXYSeries-selectedPointsChanged-s.rst
