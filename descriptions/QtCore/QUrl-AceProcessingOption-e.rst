.. sip:enum-description::
    :status: todo
    :digest: b0887695984aa78e7c6c4e360ea6e7ec

The ACE processing options control the way URLs are transformed to and from ASCII-Compatible Encoding.

The default is to use nontransitional processing and to allow non-ASCII characters only inside URLs whose top-level domains are listed in the IDN whitelist.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.toAce`, :sip:ref:`~PyQt6.QtCore.QUrl.fromAce`, :sip:ref:`~PyQt6.QtCore.QUrl.idnWhitelist`.
