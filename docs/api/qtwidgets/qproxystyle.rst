:orphan:

.. sip:class:: PyQt6.QtWidgets.QProxyStyle
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QCommonStyle`
    :description: QtWidgets/QProxyStyle-c.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.__init__
        :args:
            style: :sip:ref:`~PyQt6.QtWidgets.QStyle` = None
        :description: QtWidgets/QProxyStyle-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.__init__
        :args:
            Optional[str]
        :description: QtWidgets/QProxyStyle-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.baseStyle
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :description: QtWidgets/QProxyStyle-baseStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.drawComplexControl
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.ComplexControl`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComplex`
            :sip:ref:`~PyQt6.QtGui.QPainter`
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QProxyStyle-drawComplexControl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.drawControl
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.ControlElement`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOption`
            :sip:ref:`~PyQt6.QtGui.QPainter`
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QProxyStyle-drawControl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.drawItemPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QProxyStyle-drawItemPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.drawItemText
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
            :sip:ref:`~PyQt6.QtGui.QPalette`
            bool
            Optional[str]
            textRole: :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole` = :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.NoRole`
        :description: QtWidgets/QProxyStyle-drawItemText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.drawPrimitive
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.PrimitiveElement`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOption`
            :sip:ref:`~PyQt6.QtGui.QPainter`
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QProxyStyle-drawPrimitive-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QProxyStyle-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.generatedIconPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon.Mode`
            :sip:ref:`~PyQt6.QtGui.QPixmap`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOption`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QProxyStyle-generatedIconPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.hitTestComplexControl
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.ComplexControl`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComplex`
            :sip:ref:`~PyQt6.QtCore.QPoint`
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.SubControl`
        :description: QtWidgets/QProxyStyle-hitTestComplexControl-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.itemPixmapRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QProxyStyle-itemPixmapRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.itemTextRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QFontMetrics`
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
            bool
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QProxyStyle-itemTextRect-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.layoutSpacing
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.ControlType`
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.ControlType`
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            option: :sip:ref:`~PyQt6.QtWidgets.QStyleOption` = None
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :returns:
            int
        :description: QtWidgets/QProxyStyle-layoutSpacing-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.pixelMetric
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric`
            option: :sip:ref:`~PyQt6.QtWidgets.QStyleOption` = None
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :returns:
            int
        :description: QtWidgets/QProxyStyle-pixelMetric-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.polish
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QProxyStyle-polish-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.polish
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :description: QtWidgets/QProxyStyle-polish-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.polish
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QApplication`
        :description: QtWidgets/QProxyStyle-polish-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.setBaseStyle
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :description: QtWidgets/QProxyStyle-setBaseStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.sizeFromContents
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.ContentsType`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOption`
            :sip:ref:`~PyQt6.QtCore.QSize`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QProxyStyle-sizeFromContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.standardIcon
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.StandardPixmap`
            option: :sip:ref:`~PyQt6.QtWidgets.QStyleOption` = None
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QProxyStyle-standardIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.standardPalette
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :description: QtWidgets/QProxyStyle-standardPalette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.standardPixmap
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.StandardPixmap`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOption`
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QProxyStyle-standardPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.styleHint
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.StyleHint`
            option: :sip:ref:`~PyQt6.QtWidgets.QStyleOption` = None
            widget: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            returnData: :sip:ref:`~PyQt6.QtWidgets.QStyleHintReturn` = None
        :returns:
            int
        :description: QtWidgets/QProxyStyle-styleHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.subControlRect
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.ComplexControl`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComplex`
            :sip:ref:`~PyQt6.QtWidgets.QStyle.SubControl`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QProxyStyle-subControlRect-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.subElementRect
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle.SubElement`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOption`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QProxyStyle-subElementRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.unpolish
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QProxyStyle-unpolish-f.rst

    .. sip:method:: PyQt6.QtWidgets.QProxyStyle.unpolish
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QApplication`
        :description: QtWidgets/QProxyStyle-unpolish-f-1.rst
