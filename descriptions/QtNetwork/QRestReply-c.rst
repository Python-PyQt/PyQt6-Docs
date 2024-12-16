.. sip:class-description::
    :status: todo
    :brief: Convenience wrapper for QNetworkReply
    :digest: cf6965ab3b632e78fae06afc9368e766

:sip:ref:`~PyQt6.QtNetwork.QRestReply` is a convenience wrapper for :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`.

:sip:ref:`~PyQt6.QtNetwork.QRestReply` wraps a :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` and provides convenience methods for data and status handling. The methods provide convenience for typical RESTful client applications.

:sip:ref:`~PyQt6.QtNetwork.QRestReply` doesn't take ownership of the wrapped :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`, and the lifetime and ownership of the reply is as defined by :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` documentation.

:sip:ref:`~PyQt6.QtNetwork.QRestReply` object is not copyable, but is movable.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setAutoDeleteReplies`.
