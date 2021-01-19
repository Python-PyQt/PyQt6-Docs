:orphan:

.. sip:class:: PyQt6.QtOpenGL.QOpenGLDebugMessage
    :description: QtOpenGL/QOpenGLDebugMessage-c.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities
        :description: QtOpenGL/QOpenGLDebugMessage-Severities-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.AnySeverity
            :description: QtOpenGL/QOpenGLDebugMessage-Severities-AnySeverity-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.HighSeverity
            :description: QtOpenGL/QOpenGLDebugMessage-Severities-HighSeverity-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.InvalidSeverity
            :description: QtOpenGL/QOpenGLDebugMessage-Severities-InvalidSeverity-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.LowSeverity
            :description: QtOpenGL/QOpenGLDebugMessage-Severities-LowSeverity-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.MediumSeverity
            :description: QtOpenGL/QOpenGLDebugMessage-Severities-MediumSeverity-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.NotificationSeverity
            :description: QtOpenGL/QOpenGLDebugMessage-Severities-NotificationSeverity-v.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources
        :description: QtOpenGL/QOpenGLDebugMessage-Sources-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.AnySource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-AnySource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.APISource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-APISource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ApplicationSource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-ApplicationSource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.InvalidSource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-InvalidSource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.OtherSource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-OtherSource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ShaderCompilerSource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-ShaderCompilerSource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.ThirdPartySource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-ThirdPartySource-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources.WindowSystemSource
            :description: QtOpenGL/QOpenGLDebugMessage-Sources-WindowSystemSource-v.rst

    .. sip:enum:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types
        :description: QtOpenGL/QOpenGLDebugMessage-Types-e.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.AnyType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-AnyType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.DeprecatedBehaviorType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-DeprecatedBehaviorType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.ErrorType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-ErrorType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.GroupPopType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-GroupPopType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.GroupPushType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-GroupPushType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.InvalidType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-InvalidType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.MarkerType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-MarkerType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.OtherType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-OtherType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.PerformanceType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-PerformanceType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.PortabilityType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-PortabilityType-v.rst

        .. sip:enum-member:: PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.UndefinedBehaviorType
            :description: QtOpenGL/QOpenGLDebugMessage-Types-UndefinedBehaviorType-v.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.__init__
        :description: QtOpenGL/QOpenGLDebugMessage-__init__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.__init__
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :description: QtOpenGL/QOpenGLDebugMessage-__init__-f-1.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.createApplicationMessage
        :args:
            str
            id: int = 0
            severity: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.NotificationSeverity`
            type: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.OtherType`
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :static:
        :description: QtOpenGL/QOpenGLDebugMessage-createApplicationMessage-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.createThirdPartyMessage
        :args:
            str
            id: int = 0
            severity: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities.NotificationSeverity`
            type: :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types` = :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types.OtherType`
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :static:
        :description: QtOpenGL/QOpenGLDebugMessage-createThirdPartyMessage-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.__eq__
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :returns:
            bool
        :description: QtOpenGL/QOpenGLDebugMessage-__eq__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.id
        :returns:
            int
        :description: QtOpenGL/QOpenGLDebugMessage-id-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.message
        :returns:
            str
        :description: QtOpenGL/QOpenGLDebugMessage-message-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.__ne__
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :returns:
            bool
        :description: QtOpenGL/QOpenGLDebugMessage-__ne__-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.severity
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Severities`
        :description: QtOpenGL/QOpenGLDebugMessage-severity-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.source
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Sources`
        :description: QtOpenGL/QOpenGLDebugMessage-source-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.swap
        :args:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage`
        :description: QtOpenGL/QOpenGLDebugMessage-swap-f.rst

    .. sip:method:: PyQt6.QtOpenGL.QOpenGLDebugMessage.type
        :returns:
            :sip:ref:`~PyQt6.QtOpenGL.QOpenGLDebugMessage.Types`
        :description: QtOpenGL/QOpenGLDebugMessage-type-f.rst
