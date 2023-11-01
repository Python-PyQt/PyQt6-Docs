.. sip:method-description::
    :status: todo
    :pysig: 89bb3e10f53fc50f57e05fa940c87cc1
    :realsig: () const
    :digest: bae797b2d23126238a819c2f6e7eded5

Retrieves the current set of Diffie-Hellman parameters.

If no Diffie-Hellman parameters have been set, the :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object defaults to using the 2048-bit MODP group from RFC 3526.

**Note:** The default parameters may change in future Qt versions. Please check the documentation of the *exact Qt version* that you are using in order to know what defaults that version uses.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setDiffieHellmanParameters`.
