.. sip:enum-description::
    :status: todo
    :digest: 9bcac70ca9fbb67765c6f9e3c8112b25

Describes the options that can be used to control the details of SSL behaviour. These options are generally used to turn features off to work around buggy servers.

By default, SslOptionDisableEmptyFragments is turned on since this causes problems with a large number of servers. SslOptionDisableLegacyRenegotiation is also turned on, since it introduces a security risk. SslOptionDisableCompression is turned on to prevent the attack publicised by CRIME. SslOptionDisableSessionPersistence is turned on to optimize memory usage. The other options are turned off.

**Note:** Availability of above options depends on the version of the SSL backend in use.
