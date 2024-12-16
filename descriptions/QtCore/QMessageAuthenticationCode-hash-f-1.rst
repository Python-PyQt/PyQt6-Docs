.. sip:method-description::
    :status: todo
    :pysig: 356d4329560cfc53186989760a62a4e1
    :realsig: (QByteArrayView, QByteArrayView, QCryptographicHash::Algorithm)
    :digest: fbc2f2365b9bc4b6162817009a93733c

Returns the authentication code for the message *message* using the key *key* and the method *method*.

**Note:** In Qt versions prior to 6.6, this function took its arguments as :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView. If you experience compile errors, it's because your code is passing objects that are implicitly convertible to :sip:ref:`~PyQt6.QtCore.QByteArray`, but not QByteArrayView. Wrap the corresponding argument in ``QByteArray{~~~}`` to make the cast explicit. This is backwards-compatible with old Qt versions.

.. seealso:: hashInto().
