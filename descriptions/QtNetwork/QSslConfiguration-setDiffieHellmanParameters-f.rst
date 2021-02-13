.. sip:method-description::
    :status: todo
    :pysig: 89bb3e10f53fc50f57e05fa940c87cc1
    :realsig: (const QSslDiffieHellmanParameters&)
    :digest: b76e10b3f3ef7b641d1b21f6f4f79ebf

Sets a custom set of Diffie-Hellman parameters to be used by this socket when functioning as a server to *dhparams*.

If no Diffie-Hellman parameters have been set, the :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object defaults to using the 1024-bit MODP group from RFC 2409.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.diffieHellmanParameters`.
