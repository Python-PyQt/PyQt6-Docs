:orphan:

.. sip:class:: PyQt6.QtCharts.QPolarChart
    :inherits: :sip:ref:`~PyQt6.QtCharts.QChart`
    :description: QtCharts/QPolarChart-c.rst

    .. sip:enum:: PyQt6.QtCharts.QPolarChart.PolarOrientation
        :description: QtCharts/QPolarChart-PolarOrientation-e.rst

        .. sip:enum-member:: PyQt6.QtCharts.QPolarChart.PolarOrientation.PolarOrientationAngular
            :description: QtCharts/QPolarChart-PolarOrientation-PolarOrientationAngular-v.rst

        .. sip:enum-member:: PyQt6.QtCharts.QPolarChart.PolarOrientation.PolarOrientationRadial
            :description: QtCharts/QPolarChart-PolarOrientation-PolarOrientationRadial-v.rst

    .. sip:method:: PyQt6.QtCharts.QPolarChart.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtCharts/QPolarChart-__init__-f.rst

    .. sip:method:: PyQt6.QtCharts.QPolarChart.addAxis
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis`
            :sip:ref:`~PyQt6.QtCharts.QPolarChart.PolarOrientation`
        :description: QtCharts/QPolarChart-addAxis-f.rst

    .. sip:method:: PyQt6.QtCharts.QPolarChart.axes
        :args:
            polarOrientation: :sip:ref:`~PyQt6.QtCharts.QPolarChart.PolarOrientation` = QPolarChart.PolarOrientations(QPolarChart.PolarOrientationRadial|QPolarChart.PolarOrientationAngular)
            series: :sip:ref:`~PyQt6.QtCharts.QAbstractSeries` = None
        :returns:
            List[:sip:ref:`~PyQt6.QtCharts.QAbstractAxis`]
        :description: QtCharts/QPolarChart-axes-f.rst

    .. sip:method:: PyQt6.QtCharts.QPolarChart.axisPolarOrientation
        :args:
            :sip:ref:`~PyQt6.QtCharts.QAbstractAxis`
        :returns:
            :sip:ref:`~PyQt6.QtCharts.QPolarChart.PolarOrientation`
        :static:
        :description: QtCharts/QPolarChart-axisPolarOrientation-f.rst
