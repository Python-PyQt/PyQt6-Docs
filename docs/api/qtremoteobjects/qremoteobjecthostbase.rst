:orphan:

.. sip:class:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase
    :inherits: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode`
    :description: QtRemoteObjects/QRemoteObjectHostBase-c.rst

    .. sip:enum:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas
        :description: QtRemoteObjects/QRemoteObjectHostBase-AllowedSchemas-e.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.AllowExternalRegistration
            :description: QtRemoteObjects/QRemoteObjectHostBase-AllowedSchemas-AllowExternalRegistration-v.rst

        .. sip:enum-member:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly
            :description: QtRemoteObjects/QRemoteObjectHostBase-AllowedSchemas-BuiltInSchemasOnly-v.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.addHostSideConnection
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtRemoteObjects/QRemoteObjectHostBase-addHostSideConnection-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.disableRemoting
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectHostBase-disableRemoting-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            name: str = ''
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectHostBase-enableRemoting-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            str
            Iterable[int]
            selectionModel: :sip:ref:`~PyQt6.QtCore.QItemSelectionModel` = None
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectHostBase-enableRemoting-f-1.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.proxy
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            hostUrl: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectHostBase-proxy-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.reverseProxy
        :returns:
            bool
        :description: QtRemoteObjects/QRemoteObjectHostBase-reverseProxy-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QRemoteObjectHostBase.setName
        :args:
            str
        :description: QtRemoteObjects/QRemoteObjectHostBase-setName-f.rst
