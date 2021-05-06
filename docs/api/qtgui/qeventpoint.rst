:orphan:

.. sip:class:: PyQt6.QtGui.QEventPoint
    :description: QtGui/QEventPoint-c.rst

    .. sip:enum:: PyQt6.QtGui.QEventPoint.State
        :description: QtGui/QEventPoint-State-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QEventPoint.State.Pressed
            :description: QtGui/QEventPoint-State-Pressed-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QEventPoint.State.Released
            :description: QtGui/QEventPoint-State-Released-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QEventPoint.State.Stationary
            :description: QtGui/QEventPoint-State-Stationary-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QEventPoint.State.Unknown
            :description: QtGui/QEventPoint-State-Unknown-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QEventPoint.State.Updated
            :description: QtGui/QEventPoint-State-Updated-v.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QEventPoint`
        :description: QtGui/QEventPoint-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.__init__
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QEventPoint.State`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.device
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDevice`
        :description: QtGui/QEventPoint-device-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.ellipseDiameters
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QEventPoint-ellipseDiameters-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QEventPoint`
        :returns:
            bool
        :description: QtGui/QEventPoint-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.globalGrabPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-globalGrabPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.globalLastPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-globalLastPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.globalPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-globalPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.globalPressPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-globalPressPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.grabPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-grabPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.id
        :returns:
            int
        :description: QtGui/QEventPoint-id-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.isAccepted
        :returns:
            bool
        :description: QtGui/QEventPoint-isAccepted-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.lastPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-lastPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.lastTimestamp
        :returns:
            int
        :description: QtGui/QEventPoint-lastTimestamp-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QEventPoint`
        :returns:
            bool
        :description: QtGui/QEventPoint-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.normalizedPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-normalizedPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.position
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-position-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.pressPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-pressPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.pressTimestamp
        :returns:
            int
        :description: QtGui/QEventPoint-pressTimestamp-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.pressure
        :returns:
            float
        :description: QtGui/QEventPoint-pressure-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.rotation
        :returns:
            float
        :description: QtGui/QEventPoint-rotation-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.sceneGrabPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-sceneGrabPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.sceneLastPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-sceneLastPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.scenePosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-scenePosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.scenePressPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QEventPoint-scenePressPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.setAccepted
        :args:
            accepted: bool = True
        :description: QtGui/QEventPoint-setAccepted-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.state
        :returns:
            :sip:ref:`~PyQt6.QtGui.QEventPoint.State`
        :description: QtGui/QEventPoint-state-f-1.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.swap
        :args:
            :sip:ref:`~PyQt6.QtGui.QEventPoint`
        :description: QtGui/QEventPoint-swap-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.timeHeld
        :returns:
            float
        :description: QtGui/QEventPoint-timeHeld-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.timestamp
        :returns:
            int
        :description: QtGui/QEventPoint-timestamp-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.uniqueId
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId`
        :description: QtGui/QEventPoint-uniqueId-f.rst

    .. sip:method:: PyQt6.QtGui.QEventPoint.velocity
        :returns:
            :sip:ref:`~PyQt6.QtGui.QVector2D`
        :description: QtGui/QEventPoint-velocity-f.rst
