:orphan:

.. sip:class:: PyQt6.QtMultimedia.QScreenCapture
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QScreenCapture-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QScreenCapture.Error
        :description: QtMultimedia/QScreenCapture-Error-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QScreenCapture.Error.CaptureFailed
            :description: QtMultimedia/QScreenCapture-Error-CaptureFailed-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QScreenCapture.Error.CapturingNotSupported
            :description: QtMultimedia/QScreenCapture-Error-CapturingNotSupported-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QScreenCapture.Error.InternalError
            :description: QtMultimedia/QScreenCapture-Error-InternalError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QScreenCapture.Error.NoError
            :description: QtMultimedia/QScreenCapture-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QScreenCapture.Error.NotFound
            :description: QtMultimedia/QScreenCapture-Error-NotFound-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QScreenCapture-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.captureSession
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`
        :description: QtMultimedia/QScreenCapture-captureSession-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.error
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QScreenCapture.Error`
        :description: QtMultimedia/QScreenCapture-error-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.errorString
        :returns:
            str
        :description: QtMultimedia/QScreenCapture-errorString-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.isActive
        :returns:
            bool
        :description: QtMultimedia/QScreenCapture-isActive-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.screen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtMultimedia/QScreenCapture-screen-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.setActive
        :args:
            bool
        :description: QtMultimedia/QScreenCapture-setActive-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.setScreen
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtMultimedia/QScreenCapture-setScreen-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.start
        :description: QtMultimedia/QScreenCapture-start-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QScreenCapture.stop
        :description: QtMultimedia/QScreenCapture-stop-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QScreenCapture.activeChanged
        :args:
            bool
        :description: QtMultimedia/QScreenCapture-activeChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QScreenCapture.errorChanged
        :description: QtMultimedia/QScreenCapture-errorChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QScreenCapture.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QScreenCapture.Error`
            str
        :description: QtMultimedia/QScreenCapture-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QScreenCapture.screenChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtMultimedia/QScreenCapture-screenChanged-s.rst
