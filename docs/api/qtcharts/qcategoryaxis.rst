:orphan:

.. sip:class:: PyQt6.QtCharts.QCategoryAxis
    :inherits: :sip:ref:`~PyQt6.QtCharts.QValueAxis`
    :description: QtCharts/QCategoryAxis-c.rst

    .. sip:enum:: PyQt6.QtCharts.QCategoryAxis.AxisLabelsPosition
        :description: QtCharts/QCategoryAxis-AxisLabelsPosition-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QCategoryAxis.AxisLabelsPosition.AxisLabelsPositionCenter
            :description: QtCharts/QCategoryAxis-AxisLabelsPosition-AxisLabelsPositionCenter-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QCategoryAxis.AxisLabelsPosition.AxisLabelsPositionOnValue
            :description: QtCharts/QCategoryAxis-AxisLabelsPosition-AxisLabelsPositionOnValue-v.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCharts/QCategoryAxis-__init__-f.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.append
        :args:
            Optional[str]
            float
        :description: QtCharts/QCategoryAxis-append-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.categoriesLabels
        :returns:
            list[str]
        :description: QtCharts/QCategoryAxis-categoriesLabels-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.count
        :returns:
            int
        :description: QtCharts/QCategoryAxis-count-f.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.endValue
        :args:
            Optional[str]
        :returns:
            float
        :description: QtCharts/QCategoryAxis-endValue-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.labelsPosition
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QCategoryAxis.AxisLabelsPosition`
        :description: QtCharts/QCategoryAxis-labelsPosition-f.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.__len__
        :returns:
            int
        :description: QtCharts/QCategoryAxis-__len__-f.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.remove
        :args:
            Optional[str]
        :description: QtCharts/QCategoryAxis-remove-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.replaceLabel
        :args:
            Optional[str]
            Optional[str]
        :description: QtCharts/QCategoryAxis-replaceLabel-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.setLabelsPosition
        :args:
            :sip:ref:`~PyQt6.QtCharts.QCategoryAxis.AxisLabelsPosition`
        :description: QtCharts/QCategoryAxis-setLabelsPosition-f.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.setStartValue
        :args:
            float
        :description: QtCharts/QCategoryAxis-setStartValue-f.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.startValue
        :args:
            categoryLabel: Optional[str] = ''
        :returns:
            float
        :description: QtCharts/QCategoryAxis-startValue-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QCategoryAxis.type
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis.AxisType`
        :description: QtCharts/QCategoryAxis-type-f.rst

    .. sip:signal:: PyQt6.QtCharts.QCategoryAxis.categoriesChanged
        :description: QtCharts/QCategoryAxis-categoriesChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QCategoryAxis.labelsPositionChanged
        :args:
            :sip:ref:`~PyQt6.QtCharts.QCategoryAxis.AxisLabelsPosition`
        :description: QtCharts/QCategoryAxis-labelsPositionChanged-s.rst
