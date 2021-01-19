:orphan:

.. sip:class:: PyQt6.QtGui.QTouchEvent
    :inherits: :sip:ref:`~PyQt6.QtGui.QPointerEvent`
    :description: QtGui/QTouchEvent-c.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent.Type`
            device: :sip:ref:`~PyQt6.QtGui.QPointingDevice` = None
            modifiers: :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers` = :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers.NoModifier`
            touchPoints: Iterable[:sip:ref:`~PyQt6.QtGui.QEventPoint`] = []
        :description: QtGui/QTouchEvent-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.clone
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTouchEvent`
        :description: QtGui/QTouchEvent-clone-f.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.isBeginEvent
        :returns:
            bool
        :description: QtGui/QTouchEvent-isBeginEvent-f.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.isEndEvent
        :returns:
            bool
        :description: QtGui/QTouchEvent-isEndEvent-f.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.isUpdateEvent
        :returns:
            bool
        :description: QtGui/QTouchEvent-isUpdateEvent-f.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.target
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtGui/QTouchEvent-target-f.rst

    .. sip:method:: PyQt6.QtGui.QTouchEvent.touchPointStates
        :returns:
            :sip:ref:`~PyQt6.QtGui.QEventPoint.States`
        :description: QtGui/QTouchEvent-touchPointStates-f.rst
