:orphan:

.. sip:class:: PyQt6.QtGraphs.QAbstractAxis
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGraphs/QAbstractAxis-c.rst

    .. sip:enum:: PyQt6.QtGraphs.QAbstractAxis.AxisType
        :description: QtGraphs/QAbstractAxis-AxisType-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractAxis.AxisType.BarCategory
            :description: QtGraphs/QAbstractAxis-AxisType-BarCategory-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractAxis.AxisType.DateTime
            :description: QtGraphs/QAbstractAxis-AxisType-DateTime-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QAbstractAxis.AxisType.Value
            :description: QtGraphs/QAbstractAxis-AxisType-Value-v.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.hide
        :description: QtGraphs/QAbstractAxis-hide-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.isGridVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractAxis-isGridVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.isLineVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractAxis-isLineVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.isSubGridVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractAxis-isSubGridVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.isTitleVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractAxis-isTitleVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.isVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractAxis-isVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.labelDelegate
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlComponent`
        :description: QtGraphs/QAbstractAxis-labelDelegate-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.labelsAngle
        :returns:
            float
        :description: QtGraphs/QAbstractAxis-labelsAngle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.labelsVisible
        :returns:
            bool
        :description: QtGraphs/QAbstractAxis-labelsVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setGridVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractAxis-setGridVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setLabelDelegate
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlComponent`
        :description: QtGraphs/QAbstractAxis-setLabelDelegate-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setLabelsAngle
        :args:
            float
        :description: QtGraphs/QAbstractAxis-setLabelsAngle-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setLabelsVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractAxis-setLabelsVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setLineVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractAxis-setLineVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setMax
        :args:
            Any
        :description: QtGraphs/QAbstractAxis-setMax-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setMin
        :args:
            Any
        :description: QtGraphs/QAbstractAxis-setMin-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setRange
        :args:
            Any
            Any
        :description: QtGraphs/QAbstractAxis-setRange-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setSubGridVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractAxis-setSubGridVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setTitleColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtGraphs/QAbstractAxis-setTitleColor-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setTitleFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGraphs/QAbstractAxis-setTitleFont-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setTitleText
        :args:
            Optional[str]
        :description: QtGraphs/QAbstractAxis-setTitleText-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setTitleVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractAxis-setTitleVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.setVisible
        :args:
            visible: bool = True
        :description: QtGraphs/QAbstractAxis-setVisible-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.show
        :description: QtGraphs/QAbstractAxis-show-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.titleColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGraphs/QAbstractAxis-titleColor-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.titleFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGraphs/QAbstractAxis-titleFont-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.titleText
        :returns:
            str
        :description: QtGraphs/QAbstractAxis-titleText-f.rst

    .. sip:method:: PyQt6.QtGraphs.QAbstractAxis.type
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QAbstractAxis.AxisType`
        :description: QtGraphs/QAbstractAxis-type-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.gridVisibleChanged
        :args:
            bool
        :description: QtGraphs/QAbstractAxis-gridVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.labelDelegateChanged
        :description: QtGraphs/QAbstractAxis-labelDelegateChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.labelsAngleChanged
        :args:
            float
        :description: QtGraphs/QAbstractAxis-labelsAngleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.labelsVisibleChanged
        :args:
            bool
        :description: QtGraphs/QAbstractAxis-labelsVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.lineVisibleChanged
        :args:
            bool
        :description: QtGraphs/QAbstractAxis-lineVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.subGridVisibleChanged
        :args:
            bool
        :description: QtGraphs/QAbstractAxis-subGridVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.titleColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtGraphs/QAbstractAxis-titleColorChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.titleFontChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGraphs/QAbstractAxis-titleFontChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.titleTextChanged
        :args:
            Optional[str]
        :description: QtGraphs/QAbstractAxis-titleTextChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.titleVisibleChanged
        :args:
            bool
        :description: QtGraphs/QAbstractAxis-titleVisibleChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.update
        :description: QtGraphs/QAbstractAxis-update-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QAbstractAxis.visibleChanged
        :args:
            bool
        :description: QtGraphs/QAbstractAxis-visibleChanged-s.rst
