:orphan:

.. sip:module:: PyQt6.QtWidgets
    :description: QtWidgets/QtWidgets-m.rst

    .. sip:attribute:: PyQt6.QtWidgets.QWIDGETSIZE_MAX
        :type: int
        :const:
        :description: QtWidgets/QWIDGETSIZE_MAX-a.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawBorderPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QMargins`
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/qDrawBorderPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawPlainRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
            lineWidth: int = 1
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawPlainRect-f-4.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawPlainRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
            lineWidth: int = 1
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawPlainRect-f-5.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawShadeLine
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = True
            lineWidth: int = 1
            midLineWidth: int = 0
        :description: QtWidgets/qDrawShadeLine-f.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawShadeLine
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = True
            lineWidth: int = 1
            midLineWidth: int = 0
        :description: QtWidgets/qDrawShadeLine-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawShadePanel
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            lineWidth: int = 1
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawShadePanel-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawShadePanel
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            lineWidth: int = 1
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawShadePanel-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawShadeRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            lineWidth: int = 1
            midLineWidth: int = 0
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawShadeRect-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawShadeRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            lineWidth: int = 1
            midLineWidth: int = 0
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawShadeRect-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawWinButton
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawWinButton-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawWinButton
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawWinButton-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawWinPanel
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawWinPanel-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.qDrawWinPanel
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            int
            int
            int
            int
            :sip:ref:`~PyQt6.QtGui.QPalette`
            sunken: bool = False
            fill: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`] = None
        :description: QtWidgets/qDrawWinPanel-f-3.rst
