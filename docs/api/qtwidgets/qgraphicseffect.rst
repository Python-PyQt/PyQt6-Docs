:orphan:

.. sip:class:: PyQt6.QtWidgets.QGraphicsEffect
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QGraphicsEffect-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QGraphicsEffect.ChangeFlag
        :description: QtWidgets/QGraphicsEffect-ChangeFlag-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.ChangeFlag.SourceAttached
            :description: QtWidgets/QGraphicsEffect-ChangeFlag-SourceAttached-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.ChangeFlag.SourceBoundingRectChanged
            :description: QtWidgets/QGraphicsEffect-ChangeFlag-SourceBoundingRectChanged-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.ChangeFlag.SourceDetached
            :description: QtWidgets/QGraphicsEffect-ChangeFlag-SourceDetached-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.ChangeFlag.SourceInvalidated
            :description: QtWidgets/QGraphicsEffect-ChangeFlag-SourceInvalidated-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QGraphicsEffect.PixmapPadMode
        :description: QtWidgets/QGraphicsEffect-PixmapPadMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.PixmapPadMode.NoPad
            :description: QtWidgets/QGraphicsEffect-PixmapPadMode-NoPad-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect
            :description: QtWidgets/QGraphicsEffect-PixmapPadMode-PadToEffectiveBoundingRect-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsEffect.PixmapPadMode.PadToTransparentBorder
            :description: QtWidgets/QGraphicsEffect-PixmapPadMode-PadToTransparentBorder-v.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QGraphicsEffect-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.boundingRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsEffect-boundingRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.boundingRectFor
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsEffect-boundingRectFor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.draw
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
        :description: QtWidgets/QGraphicsEffect-draw-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.drawSource
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
        :description: QtWidgets/QGraphicsEffect-drawSource-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.isEnabled
        :returns:
            bool
        :description: QtWidgets/QGraphicsEffect-isEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.setEnabled
        :args:
            bool
        :description: QtWidgets/QGraphicsEffect-setEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.sourceBoundingRect
        :args:
            system: :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem` = :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem.LogicalCoordinates`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsEffect-sourceBoundingRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.sourceChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.ChangeFlag`
        :description: QtWidgets/QGraphicsEffect-sourceChanged-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.sourceIsPixmap
        :returns:
            bool
        :description: QtWidgets/QGraphicsEffect-sourceIsPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.sourcePixmap
        :args:
            system: :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem` = :sip:ref:`~PyQt6.QtCore.Qt.CoordinateSystem.LogicalCoordinates`
            mode: :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.PixmapPadMode` = :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QGraphicsEffect-sourcePixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.update
        :description: QtWidgets/QGraphicsEffect-update-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsEffect.updateBoundingRect
        :description: QtWidgets/QGraphicsEffect-updateBoundingRect-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QGraphicsEffect.enabledChanged
        :args:
            bool
        :description: QtWidgets/QGraphicsEffect-enabledChanged-s.rst
