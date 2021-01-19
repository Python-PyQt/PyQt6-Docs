:orphan:

.. sip:class:: PyQt6.QtGui.QPointingDevice
    :inherits: :sip:ref:`~PyQt6.QtGui.QInputDevice`
    :description: QtGui/QPointingDevice-c.rst

    .. sip:enum:: PyQt6.QtGui.QPointingDevice.PointerTypes
        :description: QtGui/QPointingDevice-PointerTypes-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.AllPointerTypes
            :description: QtGui/QPointingDevice-PointerTypes-AllPointerTypes-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.Cursor
            :description: QtGui/QPointingDevice-PointerTypes-Cursor-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.Eraser
            :description: QtGui/QPointingDevice-PointerTypes-Eraser-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.Finger
            :description: QtGui/QPointingDevice-PointerTypes-Finger-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.Generic
            :description: QtGui/QPointingDevice-PointerTypes-Generic-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.Pen
            :description: QtGui/QPointingDevice-PointerTypes-Pen-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPointingDevice.PointerTypes.Unknown
            :description: QtGui/QPointingDevice-PointerTypes-Unknown-v.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QPointingDevice-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.__init__
        :args:
            str
            int
            :sip:ref:`~PyQt6.QtGui.QInputDevice.DeviceTypes`
            :sip:ref:`~PyQt6.QtGui.QPointingDevice.PointerTypes`
            :sip:ref:`~PyQt6.QtGui.QInputDevice.Capabilities`
            int
            int
            seatName: str = ''
            uniqueId: :sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId` = QPointingDeviceUniqueId()
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QPointingDevice-__init__-f-1.rst

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
            :sip:ref:`~PyQt6.QtGui.QPointingDevice.PointerTypes`
        :description: QtGui/QPointingDevice-pointerType-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.primaryPointingDevice
        :args:
            seatName: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDevice`
        :static:
        :description: QtGui/QPointingDevice-primaryPointingDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QPointingDevice.uniqueId
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPointingDeviceUniqueId`
        :description: QtGui/QPointingDevice-uniqueId-f.rst
