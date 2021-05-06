:orphan:

.. sip:class:: PyQt6.QtDataVisualization.QAbstract3DInputHandler
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtDataVisualization/QAbstract3DInputHandler-c.rst

    .. sip:enum:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView
        :description: QtDataVisualization/QAbstract3DInputHandler-InputView-e.rst

        .. sip:enum-member:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView.InputViewNone
            :description: QtDataVisualization/QAbstract3DInputHandler-InputView-InputViewNone-v.rst

        .. sip:enum-member:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView.InputViewOnPrimary
            :description: QtDataVisualization/QAbstract3DInputHandler-InputView-InputViewOnPrimary-v.rst

        .. sip:enum-member:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView.InputViewOnSecondary
            :description: QtDataVisualization/QAbstract3DInputHandler-InputView-InputViewOnSecondary-v.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDataVisualization/QAbstract3DInputHandler-__init__-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.inputPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-inputPosition-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.inputView
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView`
        :description: QtDataVisualization/QAbstract3DInputHandler-inputView-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtDataVisualization/QAbstract3DInputHandler-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.prevDistance
        :returns:
            int
        :description: QtDataVisualization/QAbstract3DInputHandler-prevDistance-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.previousInputPos
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-previousInputPos-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.scene
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.Q3DScene`
        :description: QtDataVisualization/QAbstract3DInputHandler-scene-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.setInputPosition
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-setInputPosition-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.setInputView
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView`
        :description: QtDataVisualization/QAbstract3DInputHandler-setInputView-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.setPrevDistance
        :args:
            int
        :description: QtDataVisualization/QAbstract3DInputHandler-setPrevDistance-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.setPreviousInputPos
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-setPreviousInputPos-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.setScene
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.Q3DScene`
        :description: QtDataVisualization/QAbstract3DInputHandler-setScene-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.touchEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QTouchEvent`
        :description: QtDataVisualization/QAbstract3DInputHandler-touchEvent-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtDataVisualization/QAbstract3DInputHandler-wheelEvent-f.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.inputViewChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DInputHandler.InputView`
        :description: QtDataVisualization/QAbstract3DInputHandler-inputViewChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.positionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QAbstract3DInputHandler-positionChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QAbstract3DInputHandler.sceneChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.Q3DScene`
        :description: QtDataVisualization/QAbstract3DInputHandler-sceneChanged-s.rst
