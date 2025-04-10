:orphan:

.. sip:class:: PyQt6.QtSerialPort.QSerialPort
    :inherits: :sip:ref:`~PyQt6.QtCore.QIODevice`
    :description: QtSerialPort/QSerialPort-c.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.BaudRate
        :description: QtSerialPort/QSerialPort-BaudRate-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud115200
            :description: QtSerialPort/QSerialPort-BaudRate-Baud115200-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud1200
            :description: QtSerialPort/QSerialPort-BaudRate-Baud1200-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud19200
            :description: QtSerialPort/QSerialPort-BaudRate-Baud19200-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud2400
            :description: QtSerialPort/QSerialPort-BaudRate-Baud2400-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud38400
            :description: QtSerialPort/QSerialPort-BaudRate-Baud38400-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud4800
            :description: QtSerialPort/QSerialPort-BaudRate-Baud4800-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud57600
            :description: QtSerialPort/QSerialPort-BaudRate-Baud57600-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.BaudRate.Baud9600
            :description: QtSerialPort/QSerialPort-BaudRate-Baud9600-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.DataBits
        :description: QtSerialPort/QSerialPort-DataBits-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.DataBits.Data5
            :description: QtSerialPort/QSerialPort-DataBits-Data5-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.DataBits.Data6
            :description: QtSerialPort/QSerialPort-DataBits-Data6-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.DataBits.Data7
            :description: QtSerialPort/QSerialPort-DataBits-Data7-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.DataBits.Data8
            :description: QtSerialPort/QSerialPort-DataBits-Data8-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.Direction
        :description: QtSerialPort/QSerialPort-Direction-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Direction.AllDirections
            :description: QtSerialPort/QSerialPort-Direction-AllDirections-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Direction.Input
            :description: QtSerialPort/QSerialPort-Direction-Input-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Direction.Output
            :description: QtSerialPort/QSerialPort-Direction-Output-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.FlowControl
        :description: QtSerialPort/QSerialPort-FlowControl-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.FlowControl.HardwareControl
            :description: QtSerialPort/QSerialPort-FlowControl-HardwareControl-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.FlowControl.NoFlowControl
            :description: QtSerialPort/QSerialPort-FlowControl-NoFlowControl-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.FlowControl.SoftwareControl
            :description: QtSerialPort/QSerialPort-FlowControl-SoftwareControl-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.Parity
        :description: QtSerialPort/QSerialPort-Parity-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Parity.EvenParity
            :description: QtSerialPort/QSerialPort-Parity-EvenParity-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Parity.MarkParity
            :description: QtSerialPort/QSerialPort-Parity-MarkParity-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Parity.NoParity
            :description: QtSerialPort/QSerialPort-Parity-NoParity-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Parity.OddParity
            :description: QtSerialPort/QSerialPort-Parity-OddParity-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.Parity.SpaceParity
            :description: QtSerialPort/QSerialPort-Parity-SpaceParity-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal
        :description: QtSerialPort/QSerialPort-PinoutSignal-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.ClearToSendSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-ClearToSendSignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.DataCarrierDetectSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-DataCarrierDetectSignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.DataSetReadySignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-DataSetReadySignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.DataTerminalReadySignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-DataTerminalReadySignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.NoSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-NoSignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.RequestToSendSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-RequestToSendSignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.RingIndicatorSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-RingIndicatorSignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.SecondaryReceivedDataSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-SecondaryReceivedDataSignal-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.PinoutSignal.SecondaryTransmittedDataSignal
            :description: QtSerialPort/QSerialPort-PinoutSignal-SecondaryTransmittedDataSignal-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.SerialPortError
        :description: QtSerialPort/QSerialPort-SerialPortError-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.DeviceNotFoundError
            :description: QtSerialPort/QSerialPort-SerialPortError-DeviceNotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.NoError
            :description: QtSerialPort/QSerialPort-SerialPortError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.NotOpenError
            :description: QtSerialPort/QSerialPort-SerialPortError-NotOpenError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.OpenError
            :description: QtSerialPort/QSerialPort-SerialPortError-OpenError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.PermissionError
            :description: QtSerialPort/QSerialPort-SerialPortError-PermissionError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.ReadError
            :description: QtSerialPort/QSerialPort-SerialPortError-ReadError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.ResourceError
            :description: QtSerialPort/QSerialPort-SerialPortError-ResourceError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.TimeoutError
            :description: QtSerialPort/QSerialPort-SerialPortError-TimeoutError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.UnknownError
            :description: QtSerialPort/QSerialPort-SerialPortError-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.UnsupportedOperationError
            :description: QtSerialPort/QSerialPort-SerialPortError-UnsupportedOperationError-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.SerialPortError.WriteError
            :description: QtSerialPort/QSerialPort-SerialPortError-WriteError-v.rst

    .. sip:enum:: PyQt6.QtSerialPort.QSerialPort.StopBits
        :description: QtSerialPort/QSerialPort-StopBits-e.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.StopBits.OneAndHalfStop
            :description: QtSerialPort/QSerialPort-StopBits-OneAndHalfStop-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.StopBits.OneStop
            :description: QtSerialPort/QSerialPort-StopBits-OneStop-v.rst

        .. sip:enum-member:: PyQt6.QtSerialPort.QSerialPort.StopBits.TwoStop
            :description: QtSerialPort/QSerialPort-StopBits-TwoStop-v.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtSerialPort/QSerialPort-__init__-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.__init__
        :args:
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtSerialPort/QSerialPort-__init__-f-3.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.__init__
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtSerialPort/QSerialPort-__init__-f-2.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.baudRate
        :args:
            dir: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction` = :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction.AllDirections`
        :returns:
            int
        :description: QtSerialPort/QSerialPort-baudRate-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.bytesAvailable
        :returns:
            int
        :description: QtSerialPort/QSerialPort-bytesAvailable-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.bytesToWrite
        :returns:
            int
        :description: QtSerialPort/QSerialPort-bytesToWrite-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.canReadLine
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-canReadLine-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.clear
        :args:
            dir: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction` = :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction.AllDirections`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-clear-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.clearError
        :description: QtSerialPort/QSerialPort-clearError-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.close
        :description: QtSerialPort/QSerialPort-close-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.dataBits
        :returns:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.DataBits`
        :description: QtSerialPort/QSerialPort-dataBits-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.error
        :returns:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.SerialPortError`
        :description: QtSerialPort/QSerialPort-error-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.flowControl
        :returns:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.FlowControl`
        :description: QtSerialPort/QSerialPort-flowControl-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.flush
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-flush-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.handle
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtSerialPort/QSerialPort-handle-f-2.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.handle
        :returns:
            int
        :description: QtSerialPort/QSerialPort-handle-f-1.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.isBreakEnabled
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-isBreakEnabled-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.isDataTerminalReady
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-isDataTerminalReady-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.isRequestToSend
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-isRequestToSend-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.isSequential
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-isSequential-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.open
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-open-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.parity
        :returns:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Parity`
        :description: QtSerialPort/QSerialPort-parity-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.pinoutSignals
        :returns:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.PinoutSignal`
        :description: QtSerialPort/QSerialPort-pinoutSignals-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.portName
        :returns:
            str
        :description: QtSerialPort/QSerialPort-portName-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.readBufferSize
        :returns:
            int
        :description: QtSerialPort/QSerialPort-readBufferSize-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.readData
        :args:
            int
        :returns:
            bytes
        :description: QtSerialPort/QSerialPort-readData-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.readLineData
        :args:
            int
        :returns:
            bytes
        :description: QtSerialPort/QSerialPort-readLineData-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setBaudRate
        :args:
            int
            dir: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction` = :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction.AllDirections`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setBaudRate-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setBreakEnabled
        :args:
            enabled: bool = True
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setBreakEnabled-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setDataBits
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.DataBits`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setDataBits-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setDataTerminalReady
        :args:
            bool
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setDataTerminalReady-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setFlowControl
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.FlowControl`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setFlowControl-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setParity
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Parity`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setParity-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setPort
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo`
        :description: QtSerialPort/QSerialPort-setPort-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setPortName
        :args:
            Optional[str]
        :description: QtSerialPort/QSerialPort-setPortName-f-1.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setReadBufferSize
        :args:
            int
        :description: QtSerialPort/QSerialPort-setReadBufferSize-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setRequestToSend
        :args:
            bool
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setRequestToSend-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setSettingsRestoredOnClose
        :args:
            bool
        :description: QtSerialPort/QSerialPort-setSettingsRestoredOnClose-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.setStopBits
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.StopBits`
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-setStopBits-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.settingsRestoredOnClose
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-settingsRestoredOnClose-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.stopBits
        :returns:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.StopBits`
        :description: QtSerialPort/QSerialPort-stopBits-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.waitForBytesWritten
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-waitForBytesWritten-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.waitForReadyRead
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtSerialPort/QSerialPort-waitForReadyRead-f.rst

    .. sip:method:: PyQt6.QtSerialPort.QSerialPort.writeData
        :args:
            bytes
        :returns:
            int
        :description: QtSerialPort/QSerialPort-writeData-f.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.baudRateChanged
        :args:
            int
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Direction`
        :description: QtSerialPort/QSerialPort-baudRateChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.breakEnabledChanged
        :args:
            bool
        :description: QtSerialPort/QSerialPort-breakEnabledChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.dataBitsChanged
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.DataBits`
        :description: QtSerialPort/QSerialPort-dataBitsChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.dataTerminalReadyChanged
        :args:
            bool
        :description: QtSerialPort/QSerialPort-dataTerminalReadyChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.SerialPortError`
        :description: QtSerialPort/QSerialPort-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.flowControlChanged
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.FlowControl`
        :description: QtSerialPort/QSerialPort-flowControlChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.parityChanged
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.Parity`
        :description: QtSerialPort/QSerialPort-parityChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.requestToSendChanged
        :args:
            bool
        :description: QtSerialPort/QSerialPort-requestToSendChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.settingsRestoredOnCloseChanged
        :args:
            bool
        :description: QtSerialPort/QSerialPort-settingsRestoredOnCloseChanged-s.rst

    .. sip:signal:: PyQt6.QtSerialPort.QSerialPort.stopBitsChanged
        :args:
            :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.StopBits`
        :description: QtSerialPort/QSerialPort-stopBitsChanged-s.rst
