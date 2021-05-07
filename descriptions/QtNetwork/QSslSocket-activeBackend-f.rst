.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 6ecef30aa273c36ff0a4017a81338775

Returns the name of the backend that :sip:ref:`~PyQt6.QtNetwork.QSslSocket` and related classes use. If the active backend was not set explicitly, this function returns the name of a default backend that :sip:ref:`~PyQt6.QtNetwork.QSslSocket` selects implicitly from the list of available backends.

**Note:** When selecting a default backend implicitly, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` prefers native backends, such as SecureTransport on Darwin, or Schannel on Windows.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setActiveBackend`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.availableBackends`.
