:orphan:

.. sip:class:: PyQt6.QtGui.QInputDevice
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QInputDevice-c.rst

    .. sip:enum:: PyQt6.QtGui.QInputDevice.Capability
        :description: QtGui/QInputDevice-Capability-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.All
            :description: QtGui/QInputDevice-Capability-All-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Area
            :description: QtGui/QInputDevice-Capability-Area-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Hover
            :description: QtGui/QInputDevice-Capability-Hover-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.MouseEmulation
            :description: QtGui/QInputDevice-Capability-MouseEmulation-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.None_
            :description: QtGui/QInputDevice-Capability-None_-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.NormalizedPosition
            :description: QtGui/QInputDevice-Capability-NormalizedPosition-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Position
            :description: QtGui/QInputDevice-Capability-Position-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Pressure
            :description: QtGui/QInputDevice-Capability-Pressure-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Rotation
            :description: QtGui/QInputDevice-Capability-Rotation-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Scroll
            :description: QtGui/QInputDevice-Capability-Scroll-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.TangentialPressure
            :description: QtGui/QInputDevice-Capability-TangentialPressure-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.Velocity
            :description: QtGui/QInputDevice-Capability-Velocity-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.XTilt
            :description: QtGui/QInputDevice-Capability-XTilt-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.YTilt
            :description: QtGui/QInputDevice-Capability-YTilt-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capability.ZPosition
            :description: QtGui/QInputDevice-Capability-ZPosition-v.rst

    .. sip:enum:: PyQt6.QtGui.QInputDevice.DeviceType
        :description: QtGui/QInputDevice-DeviceType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.Airbrush
            :description: QtGui/QInputDevice-DeviceType-Airbrush-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.AllDevices
            :description: QtGui/QInputDevice-DeviceType-AllDevices-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.Keyboard
            :description: QtGui/QInputDevice-DeviceType-Keyboard-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.Mouse
            :description: QtGui/QInputDevice-DeviceType-Mouse-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.Puck
            :description: QtGui/QInputDevice-DeviceType-Puck-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.Stylus
            :description: QtGui/QInputDevice-DeviceType-Stylus-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.TouchPad
            :description: QtGui/QInputDevice-DeviceType-TouchPad-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.TouchScreen
            :description: QtGui/QInputDevice-DeviceType-TouchScreen-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceType.Unknown
            :description: QtGui/QInputDevice-DeviceType-Unknown-v.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QInputDevice-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.__init__
        :args:
            str
            int
            :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceType`
            seatName: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QInputDevice-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.availableVirtualGeometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QInputDevice-availableVirtualGeometry-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.capabilities
        :returns:
            :sip:ref:`~PyQt6.QtGui.QInputDevice.Capability`
        :description: QtGui/QInputDevice-capabilities-f-1.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.devices
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QInputDevice`]
        :static:
        :description: QtGui/QInputDevice-devices-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputDevice`
        :returns:
            bool
        :description: QtGui/QInputDevice-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.hasCapability
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputDevice.Capability`
        :returns:
            bool
        :description: QtGui/QInputDevice-hasCapability-f-1.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.name
        :returns:
            str
        :description: QtGui/QInputDevice-name-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputDevice`
        :returns:
            bool
        :description: QtGui/QInputDevice-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.primaryKeyboard
        :args:
            seatName: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QInputDevice`
        :static:
        :description: QtGui/QInputDevice-primaryKeyboard-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.seatName
        :returns:
            str
        :description: QtGui/QInputDevice-seatName-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.systemId
        :returns:
            int
        :description: QtGui/QInputDevice-systemId-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.type
        :returns:
            :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceType`
        :description: QtGui/QInputDevice-type-f-1.rst

    .. sip:signal:: PyQt6.QtGui.QInputDevice.availableVirtualGeometryChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QInputDevice-availableVirtualGeometryChanged-s.rst
