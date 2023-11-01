:orphan:

.. sip:class:: PyQt6.QtGui.QMovie
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QMovie-c.rst

    .. sip:enum:: PyQt6.QtGui.QMovie.CacheMode
        :description: QtGui/QMovie-CacheMode-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QMovie.CacheMode.CacheAll
            :description: QtGui/QMovie-CacheMode-CacheAll-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QMovie.CacheMode.CacheNone
            :description: QtGui/QMovie-CacheMode-CacheNone-v.rst

    .. sip:enum:: PyQt6.QtGui.QMovie.MovieState
        :description: QtGui/QMovie-MovieState-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QMovie.MovieState.NotRunning
            :description: QtGui/QMovie-MovieState-NotRunning-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QMovie.MovieState.Paused
            :description: QtGui/QMovie-MovieState-Paused-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QMovie.MovieState.Running
            :description: QtGui/QMovie-MovieState-Running-v.rst

    .. sip:method:: PyQt6.QtGui.QMovie.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QMovie-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            format: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QMovie-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QMovie.__init__
        :args:
            Optional[str]
            format: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QMovie-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QMovie.backgroundColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QMovie-backgroundColor-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.cacheMode
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMovie.CacheMode`
        :description: QtGui/QMovie-cacheMode-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.currentFrameNumber
        :returns:
            int
        :description: QtGui/QMovie-currentFrameNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.currentImage
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGui/QMovie-currentImage-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.currentPixmap
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QMovie-currentPixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QMovie-device-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.fileName
        :returns:
            str
        :description: QtGui/QMovie-fileName-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.format
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QMovie-format-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.frameCount
        :returns:
            int
        :description: QtGui/QMovie-frameCount-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.frameRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QMovie-frameRect-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.isValid
        :returns:
            bool
        :description: QtGui/QMovie-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.jumpToFrame
        :args:
            int
        :returns:
            bool
        :description: QtGui/QMovie-jumpToFrame-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.jumpToNextFrame
        :returns:
            bool
        :description: QtGui/QMovie-jumpToNextFrame-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.lastError
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImageReader.ImageReaderError`
        :description: QtGui/QMovie-lastError-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.lastErrorString
        :returns:
            str
        :description: QtGui/QMovie-lastErrorString-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.loopCount
        :returns:
            int
        :description: QtGui/QMovie-loopCount-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.nextFrameDelay
        :returns:
            int
        :description: QtGui/QMovie-nextFrameDelay-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.scaledSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QMovie-scaledSize-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setBackgroundColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtGui/QMovie-setBackgroundColor-f-2.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setCacheMode
        :args:
            :sip:ref:`~PyQt6.QtGui.QMovie.CacheMode`
        :description: QtGui/QMovie-setCacheMode-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QMovie-setDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setFileName
        :args:
            Optional[str]
        :description: QtGui/QMovie-setFileName-f-1.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setFormat
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QMovie-setFormat-f-1.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setPaused
        :args:
            bool
        :description: QtGui/QMovie-setPaused-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setScaledSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QMovie-setScaledSize-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.setSpeed
        :args:
            int
        :description: QtGui/QMovie-setSpeed-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.speed
        :returns:
            int
        :description: QtGui/QMovie-speed-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.start
        :description: QtGui/QMovie-start-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.state
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMovie.MovieState`
        :description: QtGui/QMovie-state-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.stop
        :description: QtGui/QMovie-stop-f.rst

    .. sip:method:: PyQt6.QtGui.QMovie.supportedFormats
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QMovie-supportedFormats-f.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.error
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageReader.ImageReaderError`
        :description: QtGui/QMovie-error-s.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.finished
        :description: QtGui/QMovie-finished-s.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.frameChanged
        :args:
            int
        :description: QtGui/QMovie-frameChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.resized
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QMovie-resized-s.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.started
        :description: QtGui/QMovie-started-s.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QMovie.MovieState`
        :description: QtGui/QMovie-stateChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QMovie.updated
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QMovie-updated-s.rst
