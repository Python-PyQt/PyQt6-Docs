:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLDebugLogger
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtOpenGL/QOpenGLDebugLogger-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode
        :description: QtOpenGL/QOpenGLDebugLogger-LoggingMode-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode.AsynchronousLogging
            :description: QtOpenGL/QOpenGLDebugLogger-LoggingMode-AsynchronousLogging-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode.SynchronousLogging
            :description: QtOpenGL/QOpenGLDebugLogger-LoggingMode-SynchronousLogging-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtOpenGL/QOpenGLDebugLogger-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.disableMessages
        :args:
            sources: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source.AnySource`
            types: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type.AnyType`
            severities: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severity` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severity.AnySeverity`
        :description: QtOpenGL/QOpenGLDebugLogger-disableMessages-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.disableMessages
        :args:
            Iterable[int]
            sources: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source.AnySource`
            types: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type.AnyType`
        :description: QtOpenGL/QOpenGLDebugLogger-disableMessages-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.enableMessages
        :args:
            sources: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source.AnySource`
            types: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type.AnyType`
            severities: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severity` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severity.AnySeverity`
        :description: QtOpenGL/QOpenGLDebugLogger-enableMessages-f-2.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.enableMessages
        :args:
            Iterable[int]
            sources: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source.AnySource`
            types: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Type.AnyType`
        :description: QtOpenGL/QOpenGLDebugLogger-enableMessages-f-3.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.initialize
        :returns:
            bool
        :description: QtOpenGL/QOpenGLDebugLogger-initialize-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.isLogging
        :returns:
            bool
        :description: QtOpenGL/QOpenGLDebugLogger-isLogging-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.loggedMessages
        :returns:
            List[:sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`]
        :description: QtOpenGL/QOpenGLDebugLogger-loggedMessages-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.loggingMode
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode`
        :description: QtOpenGL/QOpenGLDebugLogger-loggingMode-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.logMessage
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :description: QtOpenGL/QOpenGLDebugLogger-logMessage-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.maximumMessageLength
        :returns:
            int
        :description: QtOpenGL/QOpenGLDebugLogger-maximumMessageLength-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.popGroup
        :description: QtOpenGL/QOpenGLDebugLogger-popGroup-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.pushGroup
        :args:
            str
            id: int = 0
            source: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Source.ApplicationSource`
        :description: QtOpenGL/QOpenGLDebugLogger-pushGroup-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.startLogging
        :args:
            loggingMode: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugLogger.LoggingMode.AsynchronousLogging`
        :description: QtOpenGL/QOpenGLDebugLogger-startLogging-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugLogger.stopLogging
        :description: QtOpenGL/QOpenGLDebugLogger-stopLogging-f.rst

    .. sip:signal:: PyQt6.QtOpenGL.QOpenGLDebugLogger.messageLogged
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :description: QtOpenGL/QOpenGLDebugLogger-messageLogged-s.rst
