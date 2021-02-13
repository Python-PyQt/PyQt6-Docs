.. sip:method-description::
    :status: todo
    :pysig: 89bb3e10f53fc50f57e05fa940c87cc1
    :realsig: () const
    :digest: b27d2d3eefb270450fca0a1b44d21c2a

Retrieves the current set of Diffie-Hellman parameters.

If no Diffie-Hellman parameters have been set, the :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object defaults to using the 1024-bit MODP group from RFC 2409.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setDiffieHellmanParameters`.
