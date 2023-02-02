:orphan:

.. sip:class:: PyQt6.QtCore.QProcess
    :inherits: :sip:ref:`~PyQt6.QtCore.QIODevice`
    :description: QtCore/QProcess-c.rst

    .. sip:enum:: PyQt6.QtCore.QProcess.ExitStatus
        :description: QtCore/QProcess-ExitStatus-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ExitStatus.CrashExit
            :description: QtCore/QProcess-ExitStatus-CrashExit-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ExitStatus.NormalExit
            :description: QtCore/QProcess-ExitStatus-NormalExit-v.rst

    .. sip:enum:: PyQt6.QtCore.QProcess.InputChannelMode
        :description: QtCore/QProcess-InputChannelMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.InputChannelMode.ForwardedInputChannel
            :description: QtCore/QProcess-InputChannelMode-ForwardedInputChannel-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.InputChannelMode.ManagedInputChannel
            :description: QtCore/QProcess-InputChannelMode-ManagedInputChannel-v.rst

    .. sip:enum:: PyQt6.QtCore.QProcess.ProcessChannel
        :description: QtCore/QProcess-ProcessChannel-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannel.StandardError
            :description: QtCore/QProcess-ProcessChannel-StandardError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannel.StandardOutput
            :description: QtCore/QProcess-ProcessChannel-StandardOutput-v.rst

    .. sip:enum:: PyQt6.QtCore.QProcess.ProcessChannelMode
        :description: QtCore/QProcess-ProcessChannelMode-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedChannels
            :description: QtCore/QProcess-ProcessChannelMode-ForwardedChannels-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedErrorChannel
            :description: QtCore/QProcess-ProcessChannelMode-ForwardedErrorChannel-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedOutputChannel
            :description: QtCore/QProcess-ProcessChannelMode-ForwardedOutputChannel-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannelMode.MergedChannels
            :description: QtCore/QProcess-ProcessChannelMode-MergedChannels-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessChannelMode.SeparateChannels
            :description: QtCore/QProcess-ProcessChannelMode-SeparateChannels-v.rst

    .. sip:enum:: PyQt6.QtCore.QProcess.ProcessError
        :description: QtCore/QProcess-ProcessError-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessError.Crashed
            :description: QtCore/QProcess-ProcessError-Crashed-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessError.FailedToStart
            :description: QtCore/QProcess-ProcessError-FailedToStart-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessError.ReadError
            :description: QtCore/QProcess-ProcessError-ReadError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessError.Timedout
            :description: QtCore/QProcess-ProcessError-Timedout-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessError.UnknownError
            :description: QtCore/QProcess-ProcessError-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessError.WriteError
            :description: QtCore/QProcess-ProcessError-WriteError-v.rst

    .. sip:enum:: PyQt6.QtCore.QProcess.ProcessState
        :description: QtCore/QProcess-ProcessState-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessState.NotRunning
            :description: QtCore/QProcess-ProcessState-NotRunning-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessState.Running
            :description: QtCore/QProcess-ProcessState-Running-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QProcess.ProcessState.Starting
            :description: QtCore/QProcess-ProcessState-Starting-v.rst

    .. sip:method:: PyQt6.QtCore.QProcess.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QProcess-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.arguments
        :returns:
            List[str]
        :description: QtCore/QProcess-arguments-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.bytesToWrite
        :returns:
            int
        :description: QtCore/QProcess-bytesToWrite-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.close
        :description: QtCore/QProcess-close-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.closeReadChannel
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannel`
        :description: QtCore/QProcess-closeReadChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.closeWriteChannel
        :description: QtCore/QProcess-closeWriteChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessError`
        :description: QtCore/QProcess-error-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.execute
        :args:
            str
            arguments: Iterable[str] = []
        :returns:
            int
        :static:
        :description: QtCore/QProcess-execute-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.exitCode
        :returns:
            int
        :description: QtCore/QProcess-exitCode-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.exitStatus
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcess.ExitStatus`
        :description: QtCore/QProcess-exitStatus-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.inputChannelMode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcess.InputChannelMode`
        :description: QtCore/QProcess-inputChannelMode-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.isSequential
        :returns:
            bool
        :description: QtCore/QProcess-isSequential-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.kill
        :description: QtCore/QProcess-kill-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.nullDevice
        :returns:
            str
        :static:
        :description: QtCore/QProcess-nullDevice-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.open
        :args:
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :returns:
            bool
        :description: QtCore/QProcess-open-f-1.rst

    .. sip:method:: PyQt6.QtCore.QProcess.processChannelMode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode`
        :description: QtCore/QProcess-processChannelMode-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.processEnvironment
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcessEnvironment`
        :description: QtCore/QProcess-processEnvironment-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.processId
        :returns:
            int
        :description: QtCore/QProcess-processId-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.program
        :returns:
            str
        :description: QtCore/QProcess-program-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.readAllStandardError
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QProcess-readAllStandardError-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.readAllStandardOutput
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QProcess-readAllStandardOutput-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.readChannel
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannel`
        :description: QtCore/QProcess-readChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.readData
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QProcess-readData-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setArguments
        :args:
            Iterable[str]
        :description: QtCore/QProcess-setArguments-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setInputChannelMode
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.InputChannelMode`
        :description: QtCore/QProcess-setInputChannelMode-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setProcessChannelMode
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode`
        :description: QtCore/QProcess-setProcessChannelMode-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setProcessEnvironment
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcessEnvironment`
        :description: QtCore/QProcess-setProcessEnvironment-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setProcessState
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState`
        :description: QtCore/QProcess-setProcessState-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setProgram
        :args:
            str
        :description: QtCore/QProcess-setProgram-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setReadChannel
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannel`
        :description: QtCore/QProcess-setReadChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setStandardErrorFile
        :args:
            str
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.Truncate`
        :description: QtCore/QProcess-setStandardErrorFile-f-1.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setStandardInputFile
        :args:
            str
        :description: QtCore/QProcess-setStandardInputFile-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setStandardOutputFile
        :args:
            str
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.Truncate`
        :description: QtCore/QProcess-setStandardOutputFile-f-1.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setStandardOutputProcess
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess`
        :description: QtCore/QProcess-setStandardOutputProcess-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.setWorkingDirectory
        :args:
            str
        :description: QtCore/QProcess-setWorkingDirectory-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.start
        :args:
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :description: QtCore/QProcess-start-f-2.rst

    .. sip:method:: PyQt6.QtCore.QProcess.start
        :args:
            str
            arguments: Iterable[str] = []
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :description: QtCore/QProcess-start-f-3.rst

    .. sip:method:: PyQt6.QtCore.QProcess.startCommand
        :args:
            str
            mode: :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag` = :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag.ReadWrite`
        :description: QtCore/QProcess-startCommand-f-1.rst

    .. sip:method:: PyQt6.QtCore.QProcess.startDetached
        :returns:
            bool
            int
        :description: QtCore/QProcess-startDetached-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.startDetached
        :args:
            str
            arguments: Iterable[str] = []
            workingDirectory: str = ''
        :returns:
            bool
            int
        :static:
        :description: QtCore/QProcess-startDetached-f-1.rst

    .. sip:method:: PyQt6.QtCore.QProcess.state
        :returns:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState`
        :description: QtCore/QProcess-state-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.systemEnvironment
        :returns:
            List[str]
        :static:
        :description: QtCore/QProcess-systemEnvironment-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.terminate
        :description: QtCore/QProcess-terminate-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.waitForBytesWritten
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtCore/QProcess-waitForBytesWritten-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.waitForFinished
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtCore/QProcess-waitForFinished-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.waitForReadyRead
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtCore/QProcess-waitForReadyRead-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.waitForStarted
        :args:
            msecs: int = 30000
        :returns:
            bool
        :description: QtCore/QProcess-waitForStarted-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.workingDirectory
        :returns:
            str
        :description: QtCore/QProcess-workingDirectory-f.rst

    .. sip:method:: PyQt6.QtCore.QProcess.writeData
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
        :returns:
            int
        :description: QtCore/QProcess-writeData-f-1.rst

    .. sip:signal:: PyQt6.QtCore.QProcess.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessError`
        :description: QtCore/QProcess-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtCore.QProcess.finished
        :args:
            int
            exitStatus: :sip:ref:`~PyQt6.QtCore.QProcess.ExitStatus` = :sip:ref:`~PyQt6.QtCore.QProcess.ExitStatus.NormalExit`
        :description: QtCore/QProcess-finished-s.rst

    .. sip:signal:: PyQt6.QtCore.QProcess.readyReadStandardError
        :description: QtCore/QProcess-readyReadStandardError-s.rst

    .. sip:signal:: PyQt6.QtCore.QProcess.readyReadStandardOutput
        :description: QtCore/QProcess-readyReadStandardOutput-s.rst

    .. sip:signal:: PyQt6.QtCore.QProcess.started
        :description: QtCore/QProcess-started-s.rst

    .. sip:signal:: PyQt6.QtCore.QProcess.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState`
        :description: QtCore/QProcess-stateChanged-s.rst
