.. sip:enum-member-description::
    :status: todo
    :value: 0x10
    :realname: QSsl::SslOption::SslOptionDisableLegacyRenegotiation
    :digest: 53956a3337f8a8c2ed74dacf3d119301

Disables the older insecure mechanism for renegotiating the connection parameters. When enabled, this option can allow connections for legacy servers, but it introduces the possibility that an attacker could inject plaintext into the SSL session.
