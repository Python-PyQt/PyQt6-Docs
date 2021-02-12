:orphan:

.. sip:class:: PyQt6.QtCore.QIODevice
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject` :sip:ref:`~PyQt6.QtCore.QIODeviceBase`
    :description: QtCore/QIODevice-c.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.__init__
        :description: QtCore/QIODevice-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QIODevice-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.atEnd
        :returns:
            bool
        :description: QtCore/QIODevice-atEnd-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.bytesAvailable
        :returns:
            int
        :description: QtCore/QIODevice-bytesAvailable-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.bytesToWrite
        :returns:
            int
        :description: QtCore/QIODevice-bytesToWrite-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.canReadLine
        :returns:
            bool
        :description: QtCore/QIODevice-canReadLine-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.close
        :description: QtCore/QIODevice-close-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.commitTransaction
        :description: QtCore/QIODevice-commitTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.currentReadChannel
        :returns:
            int
        :description: QtCore/QIODevice-currentReadChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.currentWriteChannel
        :returns:
            int
        :description: QtCore/QIODevice-currentWriteChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.errorString
        :returns:
            str
        :description: QtCore/QIODevice-errorString-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.getChar
        :returns:
            bool
            str
        :description: QtCore/QIODevice-getChar-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.isOpen
        :returns:
            bool
        :description: QtCore/QIODevice-isOpen-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.isReadable
        :returns:
            bool
        :description: QtCore/QIODevice-isReadable-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.isSequential
        :returns:
            bool
        :description: QtCore/QIODevice-isSequential-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.isTextModeEnabled
        :returns:
            bool
        :description: QtCore/QIODevice-isTextModeEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.isTransactionStarted
        :returns:
            bool
        :description: QtCore/QIODevice-isTransactionStarted-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.isWritable
        :returns:
            bool
        :description: QtCore/QIODevice-isWritable-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.open
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode`
        :returns:
            bool
        :description: QtCore/QIODevice-open-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.openMode
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode`
        :description: QtCore/QIODevice-openMode-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.peek
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QIODevice-peek-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.pos
        :returns:
            int
        :description: QtCore/QIODevice-pos-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.putChar
        :args:
            str
        :returns:
            bool
        :description: QtCore/QIODevice-putChar-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.read
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QIODevice-read-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.readAll
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QIODevice-readAll-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.readChannelCount
        :returns:
            int
        :description: QtCore/QIODevice-readChannelCount-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.readData
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QIODevice-readData-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.readLine
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtCore/QIODevice-readLine-f-1.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.readLine
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QIODevice-readLine-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.readLineData
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QIODevice-readLineData-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.reset
        :returns:
            bool
        :description: QtCore/QIODevice-reset-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.rollbackTransaction
        :description: QtCore/QIODevice-rollbackTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.seek
        :args:
            int
        :returns:
            bool
        :description: QtCore/QIODevice-seek-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.setCurrentReadChannel
        :args:
            int
        :description: QtCore/QIODevice-setCurrentReadChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.setCurrentWriteChannel
        :args:
            int
        :description: QtCore/QIODevice-setCurrentWriteChannel-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.setErrorString
        :args:
            str
        :description: QtCore/QIODevice-setErrorString-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.setOpenMode
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode`
        :description: QtCore/QIODevice-setOpenMode-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.setTextModeEnabled
        :args:
            bool
        :description: QtCore/QIODevice-setTextModeEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.size
        :returns:
            int
        :description: QtCore/QIODevice-size-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.skip
        :args:
            int
        :returns:
            int
        :description: QtCore/QIODevice-skip-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.skipData
        :args:
            int
        :returns:
            int
        :description: QtCore/QIODevice-skipData-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.startTransaction
        :description: QtCore/QIODevice-startTransaction-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.ungetChar
        :args:
            str
        :description: QtCore/QIODevice-ungetChar-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.waitForBytesWritten
        :args:
            int
        :returns:
            bool
        :description: QtCore/QIODevice-waitForBytesWritten-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.waitForReadyRead
        :args:
            int
        :returns:
            bool
        :description: QtCore/QIODevice-waitForReadyRead-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.write
        :args:
            buffer
        :returns:
            int
        :description: QtCore/QIODevice-write-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.writeChannelCount
        :returns:
            int
        :description: QtCore/QIODevice-writeChannelCount-f.rst

    .. sip:method:: PyQt6.QtCore.QIODevice.writeData
        :args:
            buffer
        :returns:
            int
        :description: QtCore/QIODevice-writeData-f.rst

    .. sip:signal:: PyQt6.QtCore.QIODevice.aboutToClose
        :description: QtCore/QIODevice-aboutToClose-s.rst

    .. sip:signal:: PyQt6.QtCore.QIODevice.bytesWritten
        :args:
            int
        :description: QtCore/QIODevice-bytesWritten-s.rst

    .. sip:signal:: PyQt6.QtCore.QIODevice.channelBytesWritten
        :args:
            int
            int
        :description: QtCore/QIODevice-channelBytesWritten-s.rst

    .. sip:signal:: PyQt6.QtCore.QIODevice.channelReadyRead
        :args:
            int
        :description: QtCore/QIODevice-channelReadyRead-s.rst

    .. sip:signal:: PyQt6.QtCore.QIODevice.readChannelFinished
        :description: QtCore/QIODevice-readChannelFinished-s.rst

    .. sip:signal:: PyQt6.QtCore.QIODevice.readyRead
        :description: QtCore/QIODevice-readyRead-s.rst
