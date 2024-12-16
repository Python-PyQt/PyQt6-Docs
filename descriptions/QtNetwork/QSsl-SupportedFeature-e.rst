.. sip:enum-description::
    :status: todo
    :digest: 36029042dbe42c74444abfe4d8e38179

Enumerates possible features that a TLS backend supports

In :sip:ref:`~PyQt6.QtNetwork` TLS-related classes have public API, that may be left unimplemented by some backend, for example, our SecureTransport backend does not support server-side ALPN. Enumerators from SupportedFeature enum indicate that a particular feature is supported.
