:orphan:

.. sip:class:: PyQt6.QtCharts.QLegend
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget`
    :description: QtCharts/QLegend-c.rst

    .. sip:enum:: PyQt6.QtCharts.QLegend.MarkerShape
        :description: QtCharts/QLegend-MarkerShape-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeCircle
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeCircle-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeDefault
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeDefault-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeFromSeries
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeFromSeries-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapePentagon
            :description: QtCharts/QLegend-MarkerShape-MarkerShapePentagon-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeRectangle
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeRectangle-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeRotatedRectangle
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeRotatedRectangle-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeStar
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeStar-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QLegend.MarkerShape.MarkerShapeTriangle
            :description: QtCharts/QLegend-MarkerShape-MarkerShapeTriangle-v.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.alignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtCharts/QLegend-alignment-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.attachToChart
        :description: QtCharts/QLegend-attachToChart-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.borderColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QLegend-borderColor-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.brush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QLegend-brush-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.color
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QLegend-color-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.detachFromChart
        :description: QtCharts/QLegend-detachFromChart-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QLegend-font-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.hideEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHideEvent`
        :description: QtCharts/QLegend-hideEvent-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.isAttachedToChart
        :returns:
            bool
        :description: QtCharts/QLegend-isAttachedToChart-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.isBackgroundVisible
        :returns:
            bool
        :description: QtCharts/QLegend-isBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.isInteractive
        :returns:
            bool
        :description: QtCharts/QLegend-isInteractive-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.labelBrush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QLegend-labelBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.labelColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtCharts/QLegend-labelColor-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.markers
        :args:
            series: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries` = None
        :returns:
            list[:sip:ref:`~PyQt6.QtCharts.QLegendMarker`]
        :description: QtCharts/QLegend-markers-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.markerShape
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QLegend.MarkerShape`
        :description: QtCharts/QLegend-markerShape-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionGraphicsItem`
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtCharts/QLegend-paint-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.pen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QLegend-pen-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.reverseMarkers
        :returns:
            bool
        :description: QtCharts/QLegend-reverseMarkers-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtCharts/QLegend-setAlignment-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setBackgroundVisible
        :args:
            visible: bool = True
        :description: QtCharts/QLegend-setBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setBorderColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QLegend-setBorderColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QLegend-setBrush-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QLegend-setColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QLegend-setFont-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setInteractive
        :args:
            bool
        :description: QtCharts/QLegend-setInteractive-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setLabelBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QLegend-setLabelBrush-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setLabelColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QLegend-setLabelColor-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setMarkerShape
        :args:
            :sip:ref:`~PyQt6.QtCharts.QLegend.MarkerShape`
        :description: QtCharts/QLegend-setMarkerShape-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setPen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtCharts/QLegend-setPen-f-2.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setReverseMarkers
        :args:
            reverseMarkers: bool = True
        :description: QtCharts/QLegend-setReverseMarkers-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.setShowToolTips
        :args:
            bool
        :description: QtCharts/QLegend-setShowToolTips-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtCharts/QLegend-showEvent-f.rst

    .. sip:method:: PyQt6.QtCharts.QLegend.showToolTips
        :returns:
            bool
        :description: QtCharts/QLegend-showToolTips-f.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.attachedToChartChanged
        :args:
            bool
        :description: QtCharts/QLegend-attachedToChartChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.backgroundVisibleChanged
        :args:
            bool
        :description: QtCharts/QLegend-backgroundVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.borderColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QLegend-borderColorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.colorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QLegend-colorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.fontChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtCharts/QLegend-fontChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.interactiveChanged
        :args:
            bool
        :description: QtCharts/QLegend-interactiveChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.labelColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QLegend-labelColorChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.markerShapeChanged
        :args:
            :sip:ref:`~PyQt6.QtCharts.QLegend.MarkerShape`
        :description: QtCharts/QLegend-markerShapeChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.reverseMarkersChanged
        :args:
            bool
        :description: QtCharts/QLegend-reverseMarkersChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QLegend.showToolTipsChanged
        :args:
            bool
        :description: QtCharts/QLegend-showToolTipsChanged-s.rst
