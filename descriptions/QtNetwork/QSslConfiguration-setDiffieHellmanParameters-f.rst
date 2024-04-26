.. sip:method-description::
    :status: todo
    :pysig: 89bb3e10f53fc50f57e05fa940c87cc1
    :realsig: (const QSslDiffieHellmanParameters&)
    :digest: 0f2de168c3ba92bd31a24196d968565c

Sets a custom set of Diffie-Hellman parameters to be used by this socket when functioning as a server to *dhparams*.

If no Diffie-Hellman parameters have been set, the :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object defaults to using the 2048-bit MODP group from RFC 3526.

Since 6.7 you can provide an empty Diffie-Hellman parameter to use auto selection (see SSL_CTX_set_dh_auto of openssl) if the tls backend supports it.

**Note:** The default parameters may change in future Qt versions. Please check the documentation of the *exact Qt version* that you are using in order to know what defaults that version uses.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.diffieHellmanParameters`.
