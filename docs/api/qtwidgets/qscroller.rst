:orphan:

.. sip:class:: PyQt6.QtWidgets.QScroller
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QScroller-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QScroller.Input
        :description: QtWidgets/QScroller-Input-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.Input.InputMove
            :description: QtWidgets/QScroller-Input-InputMove-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.Input.InputPress
            :description: QtWidgets/QScroller-Input-InputPress-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.Input.InputRelease
            :description: QtWidgets/QScroller-Input-InputRelease-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QScroller.ScrollerGestureType
        :description: QtWidgets/QScroller-ScrollerGestureType-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.ScrollerGestureType.LeftMouseButtonGesture
            :description: QtWidgets/QScroller-ScrollerGestureType-LeftMouseButtonGesture-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.ScrollerGestureType.MiddleMouseButtonGesture
            :description: QtWidgets/QScroller-ScrollerGestureType-MiddleMouseButtonGesture-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.ScrollerGestureType.RightMouseButtonGesture
            :description: QtWidgets/QScroller-ScrollerGestureType-RightMouseButtonGesture-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.ScrollerGestureType.TouchGesture
            :description: QtWidgets/QScroller-ScrollerGestureType-TouchGesture-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QScroller.State
        :description: QtWidgets/QScroller-State-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.State.Dragging
            :description: QtWidgets/QScroller-State-Dragging-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.State.Inactive
            :description: QtWidgets/QScroller-State-Inactive-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.State.Pressed
            :description: QtWidgets/QScroller-State-Pressed-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QScroller.State.Scrolling
            :description: QtWidgets/QScroller-State-Scrolling-v.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.activeScrollers
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QScroller`]
        :static:
        :description: QtWidgets/QScroller-activeScrollers-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.ensureVisible
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            float
            float
        :description: QtWidgets/QScroller-ensureVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.ensureVisible
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            float
            float
            int
        :description: QtWidgets/QScroller-ensureVisible-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.finalPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QScroller-finalPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.grabbedGesture
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.GestureType`
        :static:
        :description: QtWidgets/QScroller-grabbedGesture-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.grabGesture
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            scrollGestureType: :sip:ref:`~PyQt6.QtWidgets.QScroller.ScrollerGestureType` = :sip:ref:`~PyQt6.QtWidgets.QScroller.ScrollerGestureType.TouchGesture`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.GestureType`
        :static:
        :description: QtWidgets/QScroller-grabGesture-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.handleInput
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QScroller.Input`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            timestamp: int = 0
        :returns:
            bool
        :description: QtWidgets/QScroller-handleInput-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.hasScroller
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            bool
        :static:
        :description: QtWidgets/QScroller-hasScroller-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.pixelPerMeter
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QScroller-pixelPerMeter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.resendPrepareEvent
        :description: QtWidgets/QScroller-resendPrepareEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.scroller
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QScroller`
        :static:
        :description: QtWidgets/QScroller-scroller-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.scrollerProperties
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties`
        :description: QtWidgets/QScroller-scrollerProperties-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QScroller-scrollTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            int
        :description: QtWidgets/QScroller-scrollTo-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.setScrollerProperties
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties`
        :description: QtWidgets/QScroller-setScrollerProperties-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.setSnapPositionsX
        :args:
            Iterable[float]
        :description: QtWidgets/QScroller-setSnapPositionsX-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.setSnapPositionsX
        :args:
            float
            float
        :description: QtWidgets/QScroller-setSnapPositionsX-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.setSnapPositionsY
        :args:
            Iterable[float]
        :description: QtWidgets/QScroller-setSnapPositionsY-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.setSnapPositionsY
        :args:
            float
            float
        :description: QtWidgets/QScroller-setSnapPositionsY-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.state
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QScroller.State`
        :description: QtWidgets/QScroller-state-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.stop
        :description: QtWidgets/QScroller-stop-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.target
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtWidgets/QScroller-target-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.ungrabGesture
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :static:
        :description: QtWidgets/QScroller-ungrabGesture-f.rst

    .. sip:method:: PyQt6.QtWidgets.QScroller.velocity
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QScroller-velocity-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QScroller.scrollerPropertiesChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties`
        :description: QtWidgets/QScroller-scrollerPropertiesChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QScroller.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QScroller.State`
        :description: QtWidgets/QScroller-stateChanged-s.rst
