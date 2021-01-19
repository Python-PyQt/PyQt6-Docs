:orphan:

.. sip:class:: PyQt6.Qt3DInput.QMouseDevice
    :inherits: :sip:ref:`~PyQt6.Qt3DInput.QAbstractPhysicalDevice`
    :description: Qt3DInput/QMouseDevice-c.rst

    .. sip:enum:: PyQt6.Qt3DInput.QMouseDevice.Axis
        :description: Qt3DInput/QMouseDevice-Axis-e.rst

        .. sip:enum-member:: PyQt6.Qt3DInput.QMouseDevice.Axis.WheelX
            :description: Qt3DInput/QMouseDevice-Axis-WheelX-v.rst

        .. sip:enum-member:: PyQt6.Qt3DInput.QMouseDevice.Axis.WheelY
            :description: Qt3DInput/QMouseDevice-Axis-WheelY-v.rst

        .. sip:enum-member:: PyQt6.Qt3DInput.QMouseDevice.Axis.X
            :description: Qt3DInput/QMouseDevice-Axis-X-v.rst

        .. sip:enum-member:: PyQt6.Qt3DInput.QMouseDevice.Axis.Y
            :description: Qt3DInput/QMouseDevice-Axis-Y-v.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DInput/QMouseDevice-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.axisCount
        :returns:
            int
        :description: Qt3DInput/QMouseDevice-axisCount-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.axisIdentifier
        :args:
            str
        :returns:
            int
        :description: Qt3DInput/QMouseDevice-axisIdentifier-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.axisNames
        :returns:
            List[str]
        :description: Qt3DInput/QMouseDevice-axisNames-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.buttonCount
        :returns:
            int
        :description: Qt3DInput/QMouseDevice-buttonCount-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.buttonIdentifier
        :args:
            str
        :returns:
            int
        :description: Qt3DInput/QMouseDevice-buttonIdentifier-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.buttonNames
        :returns:
            List[str]
        :description: Qt3DInput/QMouseDevice-buttonNames-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.sensitivity
        :returns:
            float
        :description: Qt3DInput/QMouseDevice-sensitivity-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.setSensitivity
        :args:
            float
        :description: Qt3DInput/QMouseDevice-setSensitivity-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.setUpdateAxesContinuously
        :args:
            bool
        :description: Qt3DInput/QMouseDevice-setUpdateAxesContinuously-f.rst

    .. sip:method:: PyQt6.Qt3DInput.QMouseDevice.updateAxesContinuously
        :returns:
            bool
        :description: Qt3DInput/QMouseDevice-updateAxesContinuously-f.rst

    .. sip:signal:: PyQt6.Qt3DInput.QMouseDevice.sensitivityChanged
        :args:
            float
        :description: Qt3DInput/QMouseDevice-sensitivityChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DInput.QMouseDevice.updateAxesContinuouslyChanged
        :args:
            bool
        :description: Qt3DInput/QMouseDevice-updateAxesContinuouslyChanged-s.rst
