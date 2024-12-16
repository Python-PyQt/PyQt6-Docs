.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: a25d7a8289d8a98c7d3655d51dd0745d

Returns the name of the backend that :sip:ref:`~PyQt6.QtNetwork.QSslSocket` and related classes use. If the active backend was not set explicitly, this function returns the name of a default backend that :sip:ref:`~PyQt6.QtNetwork.QSslSocket` selects implicitly from the list of available backends.

**Note:** When selecting a default backend implicitly, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` prefers the OpenSSL backend if available. If it's not available, the Schannel backend is implicitly selected on Windows, and Secure Transport on Darwin platforms. Failing these, if a custom TLS backend is found, it is used. If no other backend is found, the "certificate only" backend is selected. For more information about TLS plugins, please see `Enabling and Disabling SSL Support when Building Qt from Source <https://doc.qt.io/qt-6/ssl.html#enabling-and-disabling-ssl-support-when-building-qt-from-source>`_.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setActiveBackend`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.availableBackends`.
