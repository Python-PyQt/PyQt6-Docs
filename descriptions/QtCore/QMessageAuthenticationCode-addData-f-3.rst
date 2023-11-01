.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (QByteArrayView)
    :digest: 3feb3c6530f497fbdf9801bec81ec4ea

Adds *data* to the message.

**Note:** In Qt versions prior to 6.6, this function took its arguments as :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView. If you experience compile errors, it's because your code is passing objects that are implicitly convertible to :sip:ref:`~PyQt6.QtCore.QByteArray`, but not QByteArrayView. Wrap the corresponding argument in ``QByteArray{~~~}`` to make the cast explicit. This is backwards-compatible with old Qt versions.

.. seealso:: resultView(), :sip:ref:`~PyQt6.QtCore.QMessageAuthenticationCode.result`.
