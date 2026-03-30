:orphan:

.. sip:class:: PyQt6.QtGraphs.QLineSeries
    :inherits: :sip:ref:`~PyQt6.QtGraphs.QXYSeries`
    :description: QtGraphs/QLineSeries-c.rst

    .. sip:enum:: PyQt6.QtGraphs.QLineSeries.LineStyle
        :description: QtGraphs/QLineSeries-LineStyle-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QLineSeries.LineStyle.StepCenter
            :description: QtGraphs/QLineSeries-LineStyle-StepCenter-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QLineSeries.LineStyle.StepLeft
            :description: QtGraphs/QLineSeries-LineStyle-StepLeft-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QLineSeries.LineStyle.StepRight
            :description: QtGraphs/QLineSeries-LineStyle-StepRight-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QLineSeries.LineStyle.Straight
            :description: QtGraphs/QLineSeries-LineStyle-Straight-v.rst

    .. sip:enum:: PyQt6.QtGraphs.QLineSeries.StrokeStyle
        :description: QtGraphs/QLineSeries-StrokeStyle-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QLineSeries.StrokeStyle.DashLine
            :description: QtGraphs/QLineSeries-StrokeStyle-DashLine-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QLineSeries.StrokeStyle.SolidLine
            :description: QtGraphs/QLineSeries-StrokeStyle-SolidLine-v.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QLineSeries-__init__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.capStyle
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.PenCapStyle`
        :description: QtGraphs/QLineSeries-capStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.componentComplete
        :description: QtGraphs/QLineSeries-componentComplete-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.dashOffset
        :returns:
            float
        :description: QtGraphs/QLineSeries-dashOffset-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.dashPattern
        :returns:
            list[float]
        :description: QtGraphs/QLineSeries-dashPattern-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.dataPointCoordinatesAt
        :args:
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGraphs/QLineSeries-dataPointCoordinatesAt-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.joinStyle
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.PenJoinStyle`
        :description: QtGraphs/QLineSeries-joinStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.lineStyle
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QLineSeries.LineStyle`
        :description: QtGraphs/QLineSeries-lineStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setCapStyle
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.PenCapStyle`
        :description: QtGraphs/QLineSeries-setCapStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setDashOffset
        :args:
            float
        :description: QtGraphs/QLineSeries-setDashOffset-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setDashPattern
        :args:
            Iterable[float]
        :description: QtGraphs/QLineSeries-setDashPattern-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setJoinStyle
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.PenJoinStyle`
        :description: QtGraphs/QLineSeries-setJoinStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setLineStyle
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QLineSeries.LineStyle`
        :description: QtGraphs/QLineSeries-setLineStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setStrokeStyle
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QLineSeries.StrokeStyle`
        :description: QtGraphs/QLineSeries-setStrokeStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.setWidth
        :args:
            float
        :description: QtGraphs/QLineSeries-setWidth-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.strokeStyle
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QLineSeries.StrokeStyle`
        :description: QtGraphs/QLineSeries-strokeStyle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.type
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QAbstractSeries.SeriesType`
        :description: QtGraphs/QLineSeries-type-f.rst

    .. sip:method:: PyQt6.QtGraphs.QLineSeries.width
        :returns:
            float
        :description: QtGraphs/QLineSeries-width-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.capStyleChanged
        :description: QtGraphs/QLineSeries-capStyleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.dashOffsetChanged
        :args:
            float
        :description: QtGraphs/QLineSeries-dashOffsetChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.dashPatternChanged
        :args:
            Iterable[float]
        :description: QtGraphs/QLineSeries-dashPatternChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.joinStyleChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.PenJoinStyle`
        :description: QtGraphs/QLineSeries-joinStyleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.lineStyleChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QLineSeries.LineStyle`
        :description: QtGraphs/QLineSeries-lineStyleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.strokeStyleChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QLineSeries.StrokeStyle`
        :description: QtGraphs/QLineSeries-strokeStyleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QLineSeries.widthChanged
        :description: QtGraphs/QLineSeries-widthChanged-s.rst
