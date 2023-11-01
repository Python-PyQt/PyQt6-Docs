:orphan:

.. sip:class:: PyQt6.QtMultimedia.QWindowCapture
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QWindowCapture-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QWindowCapture.Error
        :description: QtMultimedia/QWindowCapture-Error-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QWindowCapture.Error.CaptureFailed
            :description: QtMultimedia/QWindowCapture-Error-CaptureFailed-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QWindowCapture.Error.CapturingNotSupported
            :description: QtMultimedia/QWindowCapture-Error-CapturingNotSupported-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QWindowCapture.Error.InternalError
            :description: QtMultimedia/QWindowCapture-Error-InternalError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QWindowCapture.Error.NoError
            :description: QtMultimedia/QWindowCapture-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QWindowCapture.Error.NotFound
            :description: QtMultimedia/QWindowCapture-Error-NotFound-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QWindowCapture-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.capturableWindows
        :returns:
            List[:sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow`]
        :static:
        :description: QtMultimedia/QWindowCapture-capturableWindows-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.error
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture.Error`
        :description: QtMultimedia/QWindowCapture-error-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.errorString
        :returns:
            str
        :description: QtMultimedia/QWindowCapture-errorString-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.isActive
        :returns:
            bool
        :description: QtMultimedia/QWindowCapture-isActive-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.setActive
        :args:
            bool
        :description: QtMultimedia/QWindowCapture-setActive-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.setWindow
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow`
        :description: QtMultimedia/QWindowCapture-setWindow-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.start
        :description: QtMultimedia/QWindowCapture-start-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.stop
        :description: QtMultimedia/QWindowCapture-stop-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QWindowCapture.window
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow`
        :description: QtMultimedia/QWindowCapture-window-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QWindowCapture.activeChanged
        :args:
            bool
        :description: QtMultimedia/QWindowCapture-activeChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QWindowCapture.errorChanged
        :description: QtMultimedia/QWindowCapture-errorChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QWindowCapture.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture.Error`
            Optional[str]
        :description: QtMultimedia/QWindowCapture-errorOccurred-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QWindowCapture.windowChanged
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow`
        :description: QtMultimedia/QWindowCapture-windowChanged-s.rst
