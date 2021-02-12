.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 64612697a941cd086b56badb3ebc244b

Returns the scheme of the URL. If an empty string is returned, this means the scheme is undefined and the URL is then relative.

The scheme can only contain US-ASCII letters or digits, which means it cannot contain any character that would otherwise require encoding. Additionally, schemes are always returned in lowercase form.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setScheme`, :sip:ref:`~PyQt6.QtCore.QUrl.isRelative`.
