.. sip:method-description::
    :status: todo
    :pysig: ab3de262d9634be9a356c59c6e61cdd4
    :realsig: (QCryptographicHash::Algorithm, QByteArrayView)
    :digest: ab34ee1e5ede8b8589aee3233d91ad4b

Constructs an object that can be used to create a cryptographic hash from data using method *method* and key *key*.

**Note:** In Qt versions prior to 6.6, this function took its arguments as :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView. If you experience compile errors, it's because your code is passing objects that are implicitly convertible to :sip:ref:`~PyQt6.QtCore.QByteArray`, but not QByteArrayView. Wrap the corresponding argument in ``QByteArray{~~~}`` to make the cast explicit. This is backwards-compatible with old Qt versions.
