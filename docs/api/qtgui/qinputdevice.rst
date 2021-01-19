:orphan:

.. sip:class:: PyQt6.QtGui.QInputDevice
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QInputDevice-c.rst

    .. sip:enum:: PyQt6.QtGui.QInputDevice.Capabilities
        :description: QtGui/QInputDevice-Capabilities-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.All
            :description: QtGui/QInputDevice-Capabilities-All-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Area
            :description: QtGui/QInputDevice-Capabilities-Area-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Hover
            :description: QtGui/QInputDevice-Capabilities-Hover-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.MouseEmulation
            :description: QtGui/QInputDevice-Capabilities-MouseEmulation-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.None_
            :description: QtGui/QInputDevice-Capabilities-None_-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.NormalizedPosition
            :description: QtGui/QInputDevice-Capabilities-NormalizedPosition-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Position
            :description: QtGui/QInputDevice-Capabilities-Position-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Pressure
            :description: QtGui/QInputDevice-Capabilities-Pressure-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Rotation
            :description: QtGui/QInputDevice-Capabilities-Rotation-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Scroll
            :description: QtGui/QInputDevice-Capabilities-Scroll-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.TangentialPressure
            :description: QtGui/QInputDevice-Capabilities-TangentialPressure-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.Velocity
            :description: QtGui/QInputDevice-Capabilities-Velocity-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.XTilt
            :description: QtGui/QInputDevice-Capabilities-XTilt-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.YTilt
            :description: QtGui/QInputDevice-Capabilities-YTilt-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.Capabilities.ZPosition
            :description: QtGui/QInputDevice-Capabilities-ZPosition-v.rst

    .. sip:enum:: PyQt6.QtGui.QInputDevice.DeviceTypes
        :description: QtGui/QInputDevice-DeviceTypes-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.Airbrush
            :description: QtGui/QInputDevice-DeviceTypes-Airbrush-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.AllDevices
            :description: QtGui/QInputDevice-DeviceTypes-AllDevices-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.Keyboard
            :description: QtGui/QInputDevice-DeviceTypes-Keyboard-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.Mouse
            :description: QtGui/QInputDevice-DeviceTypes-Mouse-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.Puck
            :description: QtGui/QInputDevice-DeviceTypes-Puck-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.Stylus
            :description: QtGui/QInputDevice-DeviceTypes-Stylus-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.TouchPad
            :description: QtGui/QInputDevice-DeviceTypes-TouchPad-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.TouchScreen
            :description: QtGui/QInputDevice-DeviceTypes-TouchScreen-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QInputDevice.DeviceTypes.Unknown
            :description: QtGui/QInputDevice-DeviceTypes-Unknown-v.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QInputDevice-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.__init__
        :args:
            str
            int
            :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes`
            seatName: str = ''
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QInputDevice-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.availableVirtualGeometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QInputDevice-availableVirtualGeometry-f.rst

    .. sip:method:: PyQt6.QtGui.QInputDevice.capabilities
        :returns:
            :sip:ref:`~PyQt6.QtGui.QInputDevice.Capabilities`
        :description: QtGui/QInputDevice-capabilities-f.rst

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
            :sip:ref:`~PyQt6.QtGui.QInputDevice.Capabilities`
        :returns:
            bool
        :description: QtGui/QInputDevice-hasCapability-f.rst

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
            :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes`
        :description: QtGui/QInputDevice-type-f.rst

    .. sip:signal:: PyQt6.QtGui.QInputDevice.availableVirtualGeometryChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QInputDevice-availableVirtualGeometryChanged-s.rst
