.. sip:method-description::
    :status: todo
    :pysig: 89bb3e10f53fc50f57e05fa940c87cc1
    :realsig: (const QSslDiffieHellmanParameters&)
    :digest: f17feb6a4df5983e6561b8e50e572418

Sets a custom set of Diffie-Hellman parameters to be used by this socket when functioning as a server to *dhparams*.

If no Diffie-Hellman parameters have been set, the :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object defaults to using the 2048-bit MODP group from RFC 3526.

**Note:** The default parameters may change in future Qt versions. Please check the documentation of the *exact Qt version* that you are using in order to know what defaults that version uses.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.diffieHellmanParameters`.
