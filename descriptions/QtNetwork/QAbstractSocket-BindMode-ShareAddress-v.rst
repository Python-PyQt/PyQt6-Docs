.. sip:enum-member-description::
    :status: todo
    :value: 0x1
    :realname: QAbstractSocket::BindFlag::ShareAddress
    :digest: adbbc9fa8987d80e33a0287c7b6dcfb1

Allow other services to bind to the same address and port. This is useful when multiple processes share the load of a single service by listening to the same address and port (e.g., a web server with several pre-forked listeners can greatly improve response time). However, because any service is allowed to rebind, this option is subject to certain security considerations. Note that by combining this option with , you will also allow your service to rebind an existing shared address. On Unix, this is equivalent to the SO_REUSEADDR socket option. On Windows, this is the default behavior, so this option is ignored.
