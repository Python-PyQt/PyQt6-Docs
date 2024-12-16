:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineCore/QWebEngineUrlRequestJob-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error.NoError
            :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error.RequestAborted
            :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-RequestAborted-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error.RequestDenied
            :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-RequestDenied-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error.RequestFailed
            :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-RequestFailed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error.UrlInvalid
            :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-UrlInvalid-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error.UrlNotFound
            :description: QtWebEngineCore/QWebEngineUrlRequestJob-Error-UrlNotFound-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.fail
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.Error`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-fail-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.initiator
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-initiator-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.redirect
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-redirect-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.reply
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-reply-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.requestBody
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-requestBody-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.requestHeaders
        :returns:
            dict[:sip:ref:`~PyQt6.QtCore.QByteArray`, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-requestHeaders-f-1.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.requestMethod
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-requestMethod-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.requestUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-requestUrl-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.setAdditionalResponseHeaders
        :args:
            dict[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Sequence[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]]]
        :description: QtWebEngineCore/QWebEngineUrlRequestJob-setAdditionalResponseHeaders-f-1.rst
