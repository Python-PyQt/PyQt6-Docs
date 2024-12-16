.. sip:signal-description::
    :status: todo
    :pysig: 1e0fbc8b2227534d978205e98d5cb27d
    :realsig: (QWebEnginePermission)
    :digest: cfae9a58bd3e1988a45b47abca9cf6dd

This signal is emitted when a web site requests to make use of a feature (e.g. geolocation access, permission to send notifications). The *permission* object can queried for the requesting URL and the ``QWebEnginePermission::Feature`` it's asking for, as well as to grant or deny permission.
