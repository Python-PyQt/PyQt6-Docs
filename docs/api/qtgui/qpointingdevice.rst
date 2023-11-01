:orphan:

.. sip:class:: PyQt6.QtGui.QPointingDevice
    :inherits: :sip:ref:`~PyQt6.QtGui.QInputDevice`
    :description: QtGui/QPointingDevice-c.rst

    .. sip:enum:: PyQt6.QtGui.QPointingDevice.PointerType
        :description: QtGui/QPointingDevice-PointerType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.AllPointerTypes
            :description: QtGui/QPointingDevice-PointerType-AllPointerTypes-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.Cursor
            :description: QtGui/QPointingDevice-PointerType-Cursor-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.Eraser
            :description: QtGui/QPointingDevice-PointerType-Eraser-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.Finger
            :description: QtGui/QPointingDevice-PointerType-Finger-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.Generic
            :description: QtGui/QPointingDevice-PointerType-Generic-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.Pen
            :description: QtGui/QPointingDevice-PointerType-Pen-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerType.Unknown
            :description: QtGui/QPointingDevice-PointerType-Unknown-v.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QPointingDevice-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.__init__
        :args:
            Optional[str]
            int
            :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceType`
            :sip:ref:`~PyQt6.QtGui.QPointingDevice.PointerType`
            :sip:ref:`~PyQt6.QtGui.QInputDevice.Capability`
            int
            int
            seatName: Optional[str] = ''
            uniqueId: :sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId` = QPointingDeviceUniqueId()
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QPointingDevice-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.buttonCount
        :returns:
            int
        :description: QtGui/QPointingDevice-buttonCount-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPointingDevice`
        :returns:
            bool
        :description: QtGui/QPointingDevice-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.maximumPoints
        :returns:
            int
        :description: QtGui/QPointingDevice-maximumPoints-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPointingDevice`
        :returns:
            bool
        :description: QtGui/QPointingDevice-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.pointerType
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDevice.PointerType`
        :description: QtGui/QPointingDevice-pointerType-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.primaryPointingDevice
        :args:
            seatName: Optional[str] = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDevice`
        :static:
        :description: QtGui/QPointingDevice-primaryPointingDevice-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.uniqueId
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId`
        :description: QtGui/QPointingDevice-uniqueId-f.rst
