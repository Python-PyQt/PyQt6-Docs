:orphan:

.. sip:class:: PyQt6.QtDBus.QDBusMessage
    :description: QtDBus/QDBusMessage-c.rst

    .. sip:enum:: PyQt6.QtDBus.QDBusMessage.MessageType
        :description: QtDBus/QDBusMessage-MessageType-e.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusMessage.MessageType.ErrorMessage
            :description: QtDBus/QDBusMessage-MessageType-ErrorMessage-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusMessage.MessageType.InvalidMessage
            :description: QtDBus/QDBusMessage-MessageType-InvalidMessage-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusMessage.MessageType.MethodCallMessage
            :description: QtDBus/QDBusMessage-MessageType-MethodCallMessage-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusMessage.MessageType.ReplyMessage
            :description: QtDBus/QDBusMessage-MessageType-ReplyMessage-v.rst

        .. sip:enum-member:: PyQt6.QtDBus.QDBusMessage.MessageType.SignalMessage
            :description: QtDBus/QDBusMessage-MessageType-SignalMessage-v.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.__init__
        :description: QtDBus/QDBusMessage-__init__-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.__init__
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-__init__-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.arguments
        :returns:
            List[Any]
        :description: QtDBus/QDBusMessage-arguments-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.autoStartService
        :returns:
            bool
        :description: QtDBus/QDBusMessage-autoStartService-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createError
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusError`
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :static:
        :description: QtDBus/QDBusMessage-createError-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createError
        :args:
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :static:
        :description: QtDBus/QDBusMessage-createError-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createError
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusError.ErrorType`
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :static:
        :description: QtDBus/QDBusMessage-createError-f-2.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createErrorReply
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusError`
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-createErrorReply-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createErrorReply
        :args:
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-createErrorReply-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createErrorReply
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusError.ErrorType`
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-createErrorReply-f-2.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createMethodCall
        :args:
            str
            str
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :static:
        :description: QtDBus/QDBusMessage-createMethodCall-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createReply
        :args:
            arguments: Iterable[Any] = []
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-createReply-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createReply
        :args:
            Any
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-createReply-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createSignal
        :args:
            str
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :static:
        :description: QtDBus/QDBusMessage-createSignal-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.createTargetedSignal
        :args:
            str
            str
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :static:
        :description: QtDBus/QDBusMessage-createTargetedSignal-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.errorMessage
        :returns:
            str
        :description: QtDBus/QDBusMessage-errorMessage-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.errorName
        :returns:
            str
        :description: QtDBus/QDBusMessage-errorName-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.interface
        :returns:
            str
        :description: QtDBus/QDBusMessage-interface-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.isDelayedReply
        :returns:
            bool
        :description: QtDBus/QDBusMessage-isDelayedReply-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.isInteractiveAuthorizationAllowed
        :returns:
            bool
        :description: QtDBus/QDBusMessage-isInteractiveAuthorizationAllowed-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.isReplyRequired
        :returns:
            bool
        :description: QtDBus/QDBusMessage-isReplyRequired-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.__lshift__
        :args:
            Any
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-__lshift__-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.member
        :returns:
            str
        :description: QtDBus/QDBusMessage-member-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.path
        :returns:
            str
        :description: QtDBus/QDBusMessage-path-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.service
        :returns:
            str
        :description: QtDBus/QDBusMessage-service-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.setArguments
        :args:
            Iterable[Any]
        :description: QtDBus/QDBusMessage-setArguments-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.setAutoStartService
        :args:
            bool
        :description: QtDBus/QDBusMessage-setAutoStartService-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.setDelayedReply
        :args:
            bool
        :description: QtDBus/QDBusMessage-setDelayedReply-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.setInteractiveAuthorizationAllowed
        :args:
            bool
        :description: QtDBus/QDBusMessage-setInteractiveAuthorizationAllowed-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.signature
        :returns:
            str
        :description: QtDBus/QDBusMessage-signature-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.swap
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusMessage-swap-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusMessage.type
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType`
        :description: QtDBus/QDBusMessage-type-f.rst
