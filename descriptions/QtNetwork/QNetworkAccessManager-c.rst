.. sip:class-description::
    :status: todo
    :brief: Allows the application to send network requests and receive replies
    :digest: 125d8fb313f1b862c1f0280303af4467

The :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` class allows the application to send network requests and receive replies.

The Network Access API is constructed around one :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` object, which holds the common configuration and settings for the requests it sends. It contains the proxy and cache configuration, as well as the signals related to such issues, and reply signals that can be used to monitor the progress of a network operation. One :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instance should be enough for the whole Qt application. Since :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` is based on :sip:ref:`~PyQt6.QtCore.QObject`, it can only be used from the thread it belongs to.

Once a :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` object has been created, the application can use it to send requests over the network. A group of standard functions is supplied that take a request and optional data, and each returns a :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object. The returned object is used to obtain any data returned in response to the corresponding request.

A simple download off the network could be accomplished with:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkaccessmanager.py
    :lines: 54-58

:sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` has an asynchronous API. When the ``replyFinished`` slot above is called, the parameter it takes is the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object containing the downloaded data as well as meta-data (headers, etc.).

**Note:** After the request has finished, it is the responsibility of the user to delete the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` object at an appropriate time. Do not directly delete it inside the slot connected to :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.finished`. You can use the deleteLater() function.

**Note:** :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` queues the requests it receives. The number of requests executed in parallel is dependent on the protocol. Currently, for the HTTP protocol on desktop platforms, 6 requests are executed in parallel for one host/port combination.

**Note:** :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` doesn't handle RFC 2616 Section 8.2.2 properly, in that it doesn't react to incoming data until it's done writing. For example, the upload of a large file won't stop even if the server returns a status code that instructs the client to not continue.

A more involved example, assuming the manager is already existent, can be:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkaccessmanager.py
    :lines: 63-72

Since Qt 6.11 the defaults of the TCP Keepalive parameters used by :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` have been changed. With the current settings the connection will be terminated after 2 minutes of inactivity.

These settings can be changed the individual requests, to make them more lenient, or even more aggressive via the :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest` API.

.. literalinclude:: ../../../snippets/qtbase-examples-network-http-httpwindow.py
    :lines: 103-106

In the above snippet we are picking a more aggressive strategy, to terminate the connection after thirty seconds of inactivity. This can be useful, for example, in early detection of network hangs caused by network changes on Linux.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest`, :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`.
