.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (QByteArrayView)
    :digest: e8a49c82f9710fb37af685722e93633c

Sets secret *key*. Calling this function automatically resets the object state.

For optimal performance, call this function only to *change* the active key, not to set an *initial* key, as in

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

**Note:** In Qt versions prior to 6.6, this function took its arguments as :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView. If you experience compile errors, it's because your code is passing objects that are implicitly convertible to :sip:ref:`~PyQt6.QtCore.QByteArray`, but not QByteArrayView. Wrap the corresponding argument in ``QByteArray{~~~}`` to make the cast explicit. This is backwards-compatible with old Qt versions.
