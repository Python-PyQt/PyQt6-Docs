:orphan:

.. sip:class:: PyQt6.QtNetwork.QNetworkCookie
    :description: QtNetwork/QNetworkCookie-c.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkCookie.RawForm
        :description: QtNetwork/QNetworkCookie-RawForm-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkCookie.RawForm.Full
            :description: QtNetwork/QNetworkCookie-RawForm-Full-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkCookie.RawForm.NameAndValueOnly
            :description: QtNetwork/QNetworkCookie-RawForm-NameAndValueOnly-v.rst

    .. sip:enum:: PyQt6.QtNetwork.QNetworkCookie.SameSite
        :description: QtNetwork/QNetworkCookie-SameSite-e.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkCookie.SameSite.Default
            :description: QtNetwork/QNetworkCookie-SameSite-Default-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkCookie.SameSite.Lax
            :description: QtNetwork/QNetworkCookie-SameSite-Lax-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkCookie.SameSite.None_
            :description: QtNetwork/QNetworkCookie-SameSite-None_-v.rst

        .. sip:enum-member:: PyQt6.QtNetwork.QNetworkCookie.SameSite.Strict
            :description: QtNetwork/QNetworkCookie-SameSite-Strict-v.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.__init__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :description: QtNetwork/QNetworkCookie-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.__init__
        :args:
            name: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
            value: :sip:ref:`~PyQt6.QtCore.QByteArray` = QByteArray()
        :description: QtNetwork/QNetworkCookie-__init__-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.domain
        :returns:
            str
        :description: QtNetwork/QNetworkCookie-domain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.__eq__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :returns:
            bool
        :description: QtNetwork/QNetworkCookie-__eq__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.expirationDate
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtNetwork/QNetworkCookie-expirationDate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.hasSameIdentifier
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :returns:
            bool
        :description: QtNetwork/QNetworkCookie-hasSameIdentifier-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.isHttpOnly
        :returns:
            bool
        :description: QtNetwork/QNetworkCookie-isHttpOnly-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.isSecure
        :returns:
            bool
        :description: QtNetwork/QNetworkCookie-isSecure-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.isSessionCookie
        :returns:
            bool
        :description: QtNetwork/QNetworkCookie-isSessionCookie-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.name
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QNetworkCookie-name-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.__ne__
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :returns:
            bool
        :description: QtNetwork/QNetworkCookie-__ne__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.normalize
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtNetwork/QNetworkCookie-normalize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.parseCookies
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            List[:sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`]
        :static:
        :description: QtNetwork/QNetworkCookie-parseCookies-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.path
        :returns:
            str
        :description: QtNetwork/QNetworkCookie-path-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.sameSitePolicy
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.SameSite`
        :description: QtNetwork/QNetworkCookie-sameSitePolicy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setDomain
        :args:
            str
        :description: QtNetwork/QNetworkCookie-setDomain-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setExpirationDate
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
        :description: QtNetwork/QNetworkCookie-setExpirationDate-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setHttpOnly
        :args:
            bool
        :description: QtNetwork/QNetworkCookie-setHttpOnly-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setName
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QNetworkCookie-setName-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setPath
        :args:
            str
        :description: QtNetwork/QNetworkCookie-setPath-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setSameSitePolicy
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.SameSite`
        :description: QtNetwork/QNetworkCookie-setSameSitePolicy-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setSecure
        :args:
            bool
        :description: QtNetwork/QNetworkCookie-setSecure-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.setValue
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QNetworkCookie-setValue-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.swap
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie`
        :description: QtNetwork/QNetworkCookie-swap-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.toRawForm
        :args:
            form: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.RawForm` = :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.RawForm.Full`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QNetworkCookie-toRawForm-f.rst

    .. sip:method:: PyQt6.QtNetwork.QNetworkCookie.value
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtNetwork/QNetworkCookie-value-f.rst
