:orphan:

.. sip:class:: PyQt6.QtGraphs.QBarSeries
    :inherits: :sip:ref:`~PyQt6.QtGraphs.QAbstractSeries`
    :description: QtGraphs/QBarSeries-c.rst

    .. sip:enum:: PyQt6.QtGraphs.QBarSeries.BarsType
        :description: QtGraphs/QBarSeries-BarsType-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.BarsType.Groups
            :description: QtGraphs/QBarSeries-BarsType-Groups-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.BarsType.Stacked
            :description: QtGraphs/QBarSeries-BarsType-Stacked-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.BarsType.StackedPercent
            :description: QtGraphs/QBarSeries-BarsType-StackedPercent-v.rst

    .. sip:enum:: PyQt6.QtGraphs.QBarSeries.LabelsPosition
        :description: QtGraphs/QBarSeries-LabelsPosition-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.LabelsPosition.Center
            :description: QtGraphs/QBarSeries-LabelsPosition-Center-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.LabelsPosition.InsideBase
            :description: QtGraphs/QBarSeries-LabelsPosition-InsideBase-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.LabelsPosition.InsideEnd
            :description: QtGraphs/QBarSeries-LabelsPosition-InsideEnd-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QBarSeries.LabelsPosition.OutsideEnd
            :description: QtGraphs/QBarSeries-LabelsPosition-OutsideEnd-v.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QBarSeries-__init__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.append
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :returns:
            bool
        :description: QtGraphs/QBarSeries-append-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.append
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarSet`]
        :returns:
            bool
        :description: QtGraphs/QBarSeries-append-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.at
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-at-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.barDelegate
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlComponent`
        :description: QtGraphs/QBarSeries-barDelegate-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.barSets
        :returns:
            list[:sip:ref:`~PyQt6.QtGraphs.QBarSet`]
        :description: QtGraphs/QBarSeries-barSets-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.barsType
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QBarSeries.BarsType`
        :description: QtGraphs/QBarSeries-barsType-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.barWidth
        :returns:
            float
        :description: QtGraphs/QBarSeries-barWidth-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.borderColors
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QColor`]
        :description: QtGraphs/QBarSeries-borderColors-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.clear
        :description: QtGraphs/QBarSeries-clear-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.componentComplete
        :description: QtGraphs/QBarSeries-componentComplete-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.count
        :returns:
            int
        :description: QtGraphs/QBarSeries-count-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.find
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :returns:
            int
        :description: QtGraphs/QBarSeries-find-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.insert
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :returns:
            bool
        :description: QtGraphs/QBarSeries-insert-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.labelsAngle
        :returns:
            float
        :description: QtGraphs/QBarSeries-labelsAngle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.labelsFormat
        :returns:
            str
        :description: QtGraphs/QBarSeries-labelsFormat-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.labelsMargin
        :returns:
            float
        :description: QtGraphs/QBarSeries-labelsMargin-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.labelsPosition
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QBarSeries.LabelsPosition`
        :description: QtGraphs/QBarSeries-labelsPosition-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.labelsPrecision
        :returns:
            int
        :description: QtGraphs/QBarSeries-labelsPrecision-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.labelsVisible
        :returns:
            bool
        :description: QtGraphs/QBarSeries-labelsVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.__len__
        :returns:
            int
        :description: QtGraphs/QBarSeries-__len__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.remove
        :args:
            int
        :returns:
            bool
        :description: QtGraphs/QBarSeries-remove-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.remove
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :returns:
            bool
        :description: QtGraphs/QBarSeries-remove-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.removeMultiple
        :args:
            int
            int
        :description: QtGraphs/QBarSeries-removeMultiple-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.replace
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarSet`]
        :returns:
            bool
        :description: QtGraphs/QBarSeries-replace-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.replace
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-replace-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.replace
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :returns:
            bool
        :description: QtGraphs/QBarSeries-replace-f-2.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.seriesColors
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QColor`]
        :description: QtGraphs/QBarSeries-seriesColors-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setBarDelegate
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlComponent`
        :description: QtGraphs/QBarSeries-setBarDelegate-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setBarsType
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSeries.BarsType`
        :description: QtGraphs/QBarSeries-setBarsType-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setBarWidth
        :args:
            float
        :description: QtGraphs/QBarSeries-setBarWidth-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setBorderColors
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtGraphs/QBarSeries-setBorderColors-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setLabelsAngle
        :args:
            float
        :description: QtGraphs/QBarSeries-setLabelsAngle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setLabelsFormat
        :args:
            Optional[str]
        :description: QtGraphs/QBarSeries-setLabelsFormat-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setLabelsMargin
        :args:
            float
        :description: QtGraphs/QBarSeries-setLabelsMargin-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setLabelsPosition
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSeries.LabelsPosition`
        :description: QtGraphs/QBarSeries-setLabelsPosition-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setLabelsPrecision
        :args:
            int
        :description: QtGraphs/QBarSeries-setLabelsPrecision-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setLabelsVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QBarSeries-setLabelsVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.setSeriesColors
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]]
        :description: QtGraphs/QBarSeries-setSeriesColors-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.take
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :returns:
            bool
        :description: QtGraphs/QBarSeries-take-f.rst

    .. sip:method:: PyQt6.QtGraphs.QBarSeries.type
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QAbstractSeries.SeriesType`
        :description: QtGraphs/QBarSeries-type-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barDelegateChanged
        :description: QtGraphs/QBarSeries-barDelegateChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barsetsAdded
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarSet`]
        :description: QtGraphs/QBarSeries-barsetsAdded-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barSetsChanged
        :description: QtGraphs/QBarSeries-barSetsChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barsetsRemoved
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarSet`]
        :description: QtGraphs/QBarSeries-barsetsRemoved-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barsetsReplaced
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGraphs.QBarSet`]
        :description: QtGraphs/QBarSeries-barsetsReplaced-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barsTypeChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSeries.BarsType`
        :description: QtGraphs/QBarSeries-barsTypeChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.barWidthChanged
        :description: QtGraphs/QBarSeries-barWidthChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.borderColorsChanged
        :description: QtGraphs/QBarSeries-borderColorsChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.clicked
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-clicked-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.countChanged
        :description: QtGraphs/QBarSeries-countChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.doubleClicked
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-doubleClicked-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.labelsAngleChanged
        :args:
            float
        :description: QtGraphs/QBarSeries-labelsAngleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.labelsFormatChanged
        :args:
            Optional[str]
        :description: QtGraphs/QBarSeries-labelsFormatChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.labelsMarginChanged
        :args:
            float
        :description: QtGraphs/QBarSeries-labelsMarginChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.labelsPositionChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QBarSeries.LabelsPosition`
        :description: QtGraphs/QBarSeries-labelsPositionChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.labelsPrecisionChanged
        :args:
            int
        :description: QtGraphs/QBarSeries-labelsPrecisionChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.labelsVisibleChanged
        :args:
            bool
        :description: QtGraphs/QBarSeries-labelsVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.pressed
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-pressed-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.released
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-released-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.seriesColorsChanged
        :description: QtGraphs/QBarSeries-seriesColorsChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.setValueAdded
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-setValueAdded-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.setValueChanged
        :args:
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-setValueChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.setValueRemoved
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtGraphs.QBarSet`
        :description: QtGraphs/QBarSeries-setValueRemoved-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QBarSeries.updatedBars
        :description: QtGraphs/QBarSeries-updatedBars-s.rst
