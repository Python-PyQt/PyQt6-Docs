.. sip:class-description::
    :status: todo
    :brief: Convenience wrapper for QNetworkAccessManager
    :digest: feace0b2f9b573ffaae3101f844716bf

The :sip:ref:`~PyQt6.QtNetwork.QRestAccessManager` is a convenience wrapper for :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.

:sip:ref:`~PyQt6.QtNetwork.QRestAccessManager` is a convenience wrapper on top of :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`. It amends datatypes and HTTP methods that are useful for typical RESTful client applications.

The usual Qt networking features are accessible by configuring the wrapped :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` directly. :sip:ref:`~PyQt6.QtNetwork.QRestAccessManager` does not take ownership of the wrapped :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.

:sip:ref:`~PyQt6.QtNetwork.QRestAccessManager` and related :sip:ref:`~PyQt6.QtNetwork.QRestReply` classes can only be used in the thread they live in. See QObject thread affinity for more information.

.. _qrestaccessmanager-issuing-network-requests-and-handling-replies:

Issuing Network Requests and Handling Replies
---------------------------------------------

Network requests are initiated with a function call corresponding to the desired HTTP method, such as ``get()`` and ``post()``.

.. _qrestaccessmanager-using-signals-and-slots:

Using Signals and Slots
.......................

The function returns a :sip:ref:`~PyQt6.QtNetwork.QNetworkReply`\* object, whose signals can be used to follow up on the completion of the request in a traditional Qt-signals-and-slots way.

Here's an example of how you could send a GET request and handle the response:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qrestaccessmanager.py
    :lines: 7-13

.. _qrestaccessmanager-using-callbacks-and-context-objects:

Using Callbacks and Context Objects
...................................

The functions also take a context object of :sip:ref:`~PyQt6.QtCore.QObject` (subclass) type and a callback function as parameters. The callback takes one :sip:ref:`~PyQt6.QtNetwork.QRestReply`& as a parameter. The callback can be any callable, including a pointer-to-member-function.

These callbacks are invoked when the reply has finished processing (also in the case the processing finished due to an error).

The context object can be ``nullptr``, although, generally speaking, this is discouraged. Using a valid context object ensures that if the context object is destroyed during request processing, the callback will not be called. Stray callbacks which access a destroyed context is a source of application misbehavior.

Here's an example of how you could send a GET request and check the response:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qrestaccessmanager.py
    :lines: 18-25

Many of the functions take in data for sending to a server. The data is supplied as the second parameter after the request.

Here's an example of how you could send a POST request and check the response:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qrestaccessmanager.py
    :lines: 30-39

The provided :sip:ref:`~PyQt6.QtNetwork.QRestReply`& is valid only while the callback executes. If you need it for longer, you can either move it to another :sip:ref:`~PyQt6.QtNetwork.QRestReply`, or construct a new one and initialize it with the :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` (see :sip:ref:`~PyQt6.QtNetwork.QRestReply.networkReply`).

.. _qrestaccessmanager-supported-data-types:

Supported data types
....................

The following table summarizes the methods and the supported data types. ``X`` means support.

+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+
| Data type                                  | ``get()`` | ``post()`` | ``put()`` | ``head()`` | ``patch()`` | ``deleteResource()`` | ``sendCustomRequest()`` |
+============================================+===========+============+===========+============+=============+======================+=========================+
| No data                                    | X         | -          | -         | X          | -           | X                    | -                       |
+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+
| :sip:ref:`~PyQt6.QtCore.QByteArray`        | X         | X          | X         | -          | X           | -                    | X                       |
+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+
| :sip:ref:`~PyQt6.QtCore.QJsonDocument` \*) | X         | X          | X         | -          | X           | -                    | -                       |
+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+
| QVariantMap \*\*)                          | -         | X          | X         | -          | X           | -                    | -                       |
+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+
| :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` | -         | X          | X         | -          | -           | -                    | X                       |
+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+
| :sip:ref:`~PyQt6.QtCore.QIODevice`         | X         | X          | X         | -          | X           | -                    | X                       |
+--------------------------------------------+-----------+------------+-----------+------------+-------------+----------------------+-------------------------+

\*) :sip:ref:`~PyQt6.QtCore.QJsonDocument` is sent in :sip:ref:`~PyQt6.QtCore.QJsonDocument.JsonFormat.Compact` format, and the ``Content-Type`` header is set to ``application/json`` if the ``Content-Type`` header was not set

\*\*) QVariantMap is converted to and treated as a QJsonObject

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QRestReply`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequestFactory`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.
