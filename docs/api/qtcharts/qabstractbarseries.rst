:orphan:

.. sip:class:: PyQt6.QtCharts.QAbstractBarSeries
    :inherits: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries`
    :description: QtCharts/QAbstractBarSeries-c.rst

    .. sip:enum:: PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition
        :description: QtCharts/QAbstractBarSeries-LabelsPosition-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition.LabelsCenter
            :description: QtCharts/QAbstractBarSeries-LabelsPosition-LabelsCenter-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition.LabelsInsideBase
            :description: QtCharts/QAbstractBarSeries-LabelsPosition-LabelsInsideBase-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition.LabelsInsideEnd
            :description: QtCharts/QAbstractBarSeries-LabelsPosition-LabelsInsideEnd-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd
            :description: QtCharts/QAbstractBarSeries-LabelsPosition-LabelsOutsideEnd-v.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.append
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :returns:
            bool
        :description: QtCharts/QAbstractBarSeries-append-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.append
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCharts.QBarSet`]
        :returns:
            bool
        :description: QtCharts/QAbstractBarSeries-append-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.barSets
        :returns:
            List[:sip:ref:`~PyQt6.QtCharts.QBarSet`]
        :description: QtCharts/QAbstractBarSeries-barSets-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.barWidth
        :returns:
            float
        :description: QtCharts/QAbstractBarSeries-barWidth-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.clear
        :description: QtCharts/QAbstractBarSeries-clear-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.count
        :returns:
            int
        :description: QtCharts/QAbstractBarSeries-count-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.insert
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :returns:
            bool
        :description: QtCharts/QAbstractBarSeries-insert-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.isLabelsVisible
        :returns:
            bool
        :description: QtCharts/QAbstractBarSeries-isLabelsVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.labelsAngle
        :returns:
            float
        :description: QtCharts/QAbstractBarSeries-labelsAngle-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.labelsFormat
        :returns:
            str
        :description: QtCharts/QAbstractBarSeries-labelsFormat-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.labelsPosition
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition`
        :description: QtCharts/QAbstractBarSeries-labelsPosition-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.labelsPrecision
        :returns:
            int
        :description: QtCharts/QAbstractBarSeries-labelsPrecision-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.__len__
        :returns:
            int
        :description: QtCharts/QAbstractBarSeries-__len__-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.remove
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :returns:
            bool
        :description: QtCharts/QAbstractBarSeries-remove-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.setBarWidth
        :args:
            float
        :description: QtCharts/QAbstractBarSeries-setBarWidth-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.setLabelsAngle
        :args:
            float
        :description: QtCharts/QAbstractBarSeries-setLabelsAngle-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.setLabelsFormat
        :args:
            Optional[str]
        :description: QtCharts/QAbstractBarSeries-setLabelsFormat-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.setLabelsPosition
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition`
        :description: QtCharts/QAbstractBarSeries-setLabelsPosition-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.setLabelsPrecision
        :args:
            int
        :description: QtCharts/QAbstractBarSeries-setLabelsPrecision-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.setLabelsVisible
        :args:
            visible: bool = True
        :description: QtCharts/QAbstractBarSeries-setLabelsVisible-f.rst

    .. sip:method:: PyQt6.QtCharts.QAbstractBarSeries.take
        :args:
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :returns:
            bool
        :description: QtCharts/QAbstractBarSeries-take-f.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.barsetsAdded
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCharts.QBarSet`]
        :description: QtCharts/QAbstractBarSeries-barsetsAdded-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.barsetsRemoved
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCharts.QBarSet`]
        :description: QtCharts/QAbstractBarSeries-barsetsRemoved-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.clicked
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :description: QtCharts/QAbstractBarSeries-clicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.countChanged
        :description: QtCharts/QAbstractBarSeries-countChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.doubleClicked
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :description: QtCharts/QAbstractBarSeries-doubleClicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.hovered
        :args:
            bool
            int
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :description: QtCharts/QAbstractBarSeries-hovered-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.labelsAngleChanged
        :args:
            float
        :description: QtCharts/QAbstractBarSeries-labelsAngleChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.labelsFormatChanged
        :args:
            Optional[str]
        :description: QtCharts/QAbstractBarSeries-labelsFormatChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.labelsPositionChanged
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractBarSeries.LabelsPosition`
        :description: QtCharts/QAbstractBarSeries-labelsPositionChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.labelsPrecisionChanged
        :args:
            int
        :description: QtCharts/QAbstractBarSeries-labelsPrecisionChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.labelsVisibleChanged
        :description: QtCharts/QAbstractBarSeries-labelsVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.pressed
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :description: QtCharts/QAbstractBarSeries-pressed-s.rst

    .. sip:signal:: PyQt6.QtCharts.QAbstractBarSeries.released
        :args:
            int
            :sip:ref:`~PyQt6.QtCharts.QBarSet`
        :description: QtCharts/QAbstractBarSeries-released-s.rst
