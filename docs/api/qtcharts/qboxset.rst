:orphan:

.. sip:class:: PyQt6.QtCharts.QBoxSet
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCharts/QBoxSet-c.rst

    .. sip:enum:: PyQt6.QtCharts.QBoxSet.ValuePositions
        :description: QtCharts/QBoxSet-ValuePositions-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QBoxSet.ValuePositions.LowerExtreme
            :description: QtCharts/QBoxSet-ValuePositions-LowerExtreme-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QBoxSet.ValuePositions.LowerQuartile
            :description: QtCharts/QBoxSet-ValuePositions-LowerQuartile-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QBoxSet.ValuePositions.Median
            :description: QtCharts/QBoxSet-ValuePositions-Median-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QBoxSet.ValuePositions.UpperExtreme
            :description: QtCharts/QBoxSet-ValuePositions-UpperExtreme-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QBoxSet.ValuePositions.UpperQuartile
            :description: QtCharts/QBoxSet-ValuePositions-UpperQuartile-v.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.__init__
        :args:
            label: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCharts/QBoxSet-__init__-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.__init__
        :args:
            float
            float
            float
            float
            float
            label: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCharts/QBoxSet-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.append
        :args:
            float
        :description: QtCharts/QBoxSet-append-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.append
        :args:
            Iterable[float]
        :description: QtCharts/QBoxSet-append-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.at
        :args:
            int
        :returns:
            float
        :description: QtCharts/QBoxSet-at-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.brush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtCharts/QBoxSet-brush-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.clear
        :description: QtCharts/QBoxSet-clear-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.count
        :returns:
            int
        :description: QtCharts/QBoxSet-count-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.__getitem__
        :args:
            int
        :returns:
            float
        :description: QtCharts/QBoxSet-__getitem__-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.label
        :returns:
            str
        :description: QtCharts/QBoxSet-label-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.__len__
        :returns:
            int
        :description: QtCharts/QBoxSet-__len__-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.__lshift__
        :args:
            float
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QBoxSet`
        :description: QtCharts/QBoxSet-__lshift__-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.pen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPen`
        :description: QtCharts/QBoxSet-pen-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.setBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtCharts/QBoxSet-setBrush-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.setLabel
        :args:
            str
        :description: QtCharts/QBoxSet-setLabel-f.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.setPen
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QPen`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtCharts/QBoxSet-setPen-f-1.rst

    .. sip:method:: PyQt6.QtCharts.QBoxSet.setValue
        :args:
            int
            float
        :description: QtCharts/QBoxSet-setValue-f.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.brushChanged
        :description: QtCharts/QBoxSet-brushChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.cleared
        :description: QtCharts/QBoxSet-cleared-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.clicked
        :description: QtCharts/QBoxSet-clicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.doubleClicked
        :description: QtCharts/QBoxSet-doubleClicked-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.hovered
        :args:
            bool
        :description: QtCharts/QBoxSet-hovered-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.penChanged
        :description: QtCharts/QBoxSet-penChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.pressed
        :description: QtCharts/QBoxSet-pressed-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.released
        :description: QtCharts/QBoxSet-released-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.valueChanged
        :args:
            int
        :description: QtCharts/QBoxSet-valueChanged-s.rst

    .. sip:signal:: PyQt6.QtCharts.QBoxSet.valuesChanged
        :description: QtCharts/QBoxSet-valuesChanged-s.rst
