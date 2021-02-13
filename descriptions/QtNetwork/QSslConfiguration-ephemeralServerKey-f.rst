.. sip:method-description::
    :status: todo
    :pysig: 97ecfb6806202f6b76660508cd19022f
    :realsig: () const
    :digest: 6155962b99a0f0a7a782accf7a27410a

Returns the ephemeral server key used for cipher algorithms with forward secrecy, e.g. DHE-RSA-AES128-SHA.

The ephemeral key is only available when running in client mode, i.e. :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.SslClientMode`. When running in server mode or using a cipher algorithm without forward secrecy a null key is returned. The ephemeral server key will be set before emitting the encrypted() signal.
