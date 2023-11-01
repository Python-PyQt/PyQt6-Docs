:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest
    :description: QtWebEngineCore/QWebEngineHttpRequest-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method
        :description: QtWebEngineCore/QWebEngineHttpRequest-Method-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method.Get
            :description: QtWebEngineCore/QWebEngineHttpRequest-Method-Get-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method.Post
            :description: QtWebEngineCore/QWebEngineHttpRequest-Method-Post-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.__init__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest`
        :description: QtWebEngineCore/QWebEngineHttpRequest-__init__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.__init__
        :args:
            url: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
            method: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method` = :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method.Get`
        :description: QtWebEngineCore/QWebEngineHttpRequest-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.__eq__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest`
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineHttpRequest-__eq__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.hasHeader
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineHttpRequest-hasHeader-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.header
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWebEngineCore/QWebEngineHttpRequest-header-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.headers
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtWebEngineCore/QWebEngineHttpRequest-headers-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.method
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method`
        :description: QtWebEngineCore/QWebEngineHttpRequest-method-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.__ne__
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest`
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineHttpRequest-__ne__-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.postData
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWebEngineCore/QWebEngineHttpRequest-postData-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.postRequest
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            Dict[Optional[str], Optional[str]]
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest`
        :static:
        :description: QtWebEngineCore/QWebEngineHttpRequest-postRequest-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.setHeader
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWebEngineCore/QWebEngineHttpRequest-setHeader-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.setMethod
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.Method`
        :description: QtWebEngineCore/QWebEngineHttpRequest-setMethod-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.setPostData
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWebEngineCore/QWebEngineHttpRequest-setPostData-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.setUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineHttpRequest-setUrl-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.swap
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest`
        :description: QtWebEngineCore/QWebEngineHttpRequest-swap-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.unsetHeader
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWebEngineCore/QWebEngineHttpRequest-unsetHeader-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHttpRequest.url
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineHttpRequest-url-f.rst
