.. sip:class-description::
    :status: todo
    :brief: Resembles a MIME multipart message to be sent over HTTP
    :digest: 801fedfb938dcd0af7c9ded012f90fbc

The :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` class resembles a MIME multipart message to be sent over HTTP.

The :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` resembles a MIME multipart message, as described in RFC 2046, which is to be sent over HTTP. A multipart message consists of an arbitrary number of body parts (see :sip:ref:`~PyQt6.QtNetwork.QHttpPart`), which are separated by a unique boundary. The boundary of the :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart` is constructed with the string "boundary_.oOo._" followed by random characters, and provides enough uniqueness to make sure it does not occur inside the parts itself. If desired, the boundary can still be set via :sip:ref:`~PyQt6.QtNetwork.QHttpMultiPart.setBoundary`.

As an example, consider the following code snippet, which constructs a multipart message containing a text part followed by an image part:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qhttpmultipart.py
    :lines: 43-66

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpPart`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.post`.
