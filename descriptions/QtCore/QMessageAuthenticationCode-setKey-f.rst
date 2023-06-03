.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: cc38bbf16889f75b28b9cf06fa834a4e

Sets secret *key*. Calling this method automatically resets the object state.

For optimal performance, call this method only to *change* the active key, not to set an *initial* key, as in

::

    QMessageAuthenticationCode mac(method);
    mac.setKey(key); // does extra work
    use(mac);

Prefer to pass initial keys as the constructor argument:

::

    QMessageAuthenticationCode mac(method, key); // OK, optimal
    use(mac);

You can use std::optional to delay construction of a :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode` until you know the key:

::

    std::optional<QMessageAuthenticationCode> mac;
    ~~~
    key = ~~~;
    mac.emplace(method, key);
    use(*mac);
