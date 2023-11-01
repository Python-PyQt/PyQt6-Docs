.. sip:signal-description::
    :status: todo
    :pysig: 93fc26ac0905bbad7695dae69e30b412
    :realsig: (const QString&, const QString&, const QUrl&)
    :digest: f58e50df511d49b9e535a572fb1c34b3

Signal emitted when the server responds to the authorization request with an error as defined in `RFC 6749 error response <https://www.rfc-editor.org/rfc/rfc6749#section-5.2>`_.

*error* is the name of the error; *errorDescription* describes the error and *uri* is an optional URI containing more information about the error.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.requestFailed`.
