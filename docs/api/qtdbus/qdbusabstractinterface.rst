:orphan:

.. sip:class:: PyQt6.QtDBus.QDBusAbstractInterface
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtDBus/QDBusAbstractInterface-c.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.__init__
        :args:
            str
            str
            str
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtDBus/QDBusAbstractInterface-__init__-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.asyncCall
        :args:
            str
            *
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall`
        :description: QtDBus/QDBusAbstractInterface-asyncCall-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.asyncCallWithArgumentList
        :args:
            str
            Iterable[Any]
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall`
        :description: QtDBus/QDBusAbstractInterface-asyncCallWithArgumentList-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.call
        :args:
            str
            *
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusAbstractInterface-call-f-2.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.call
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBus.CallMode`
            str
            *
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusAbstractInterface-call-f-3.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.callWithArgumentList
        :args:
            :sip:ref:`~PyQt6.QtDBus.QDBus.CallMode`
            str
            Iterable[Any]
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusMessage`
        :description: QtDBus/QDBusAbstractInterface-callWithArgumentList-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.callWithCallback
        :args:
            str
            Iterable[Any]
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusAbstractInterface-callWithCallback-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.callWithCallback
        :args:
            str
            Iterable[Any]
            PYQT_SLOT
            PYQT_SLOT
        :returns:
            bool
        :description: QtDBus/QDBusAbstractInterface-callWithCallback-f-1.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.connection
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusConnection`
        :description: QtDBus/QDBusAbstractInterface-connection-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.connectNotify
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaMethod`
        :description: QtDBus/QDBusAbstractInterface-connectNotify-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.disconnectNotify
        :args:
            :sip:ref:`~PyQt6.QtCore.QMetaMethod`
        :description: QtDBus/QDBusAbstractInterface-disconnectNotify-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.interface
        :returns:
            str
        :description: QtDBus/QDBusAbstractInterface-interface-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.isValid
        :returns:
            bool
        :description: QtDBus/QDBusAbstractInterface-isValid-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.lastError
        :returns:
            :sip:ref:`~PyQt6.QtDBus.QDBusError`
        :description: QtDBus/QDBusAbstractInterface-lastError-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.path
        :returns:
            str
        :description: QtDBus/QDBusAbstractInterface-path-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.service
        :returns:
            str
        :description: QtDBus/QDBusAbstractInterface-service-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.setTimeout
        :args:
            int
        :description: QtDBus/QDBusAbstractInterface-setTimeout-f.rst

    .. sip:method:: PyQt6.QtDBus.QDBusAbstractInterface.timeout
        :returns:
            int
        :description: QtDBus/QDBusAbstractInterface-timeout-f.rst
