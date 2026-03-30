.. sip:method-description::
    :status: todo
    :pysig: cffec0305d55b4c7e8b122d0e65c761f
    :realsig: (QByteArrayView, QUrl::ParsingMode)
    :digest: d6f75820aef1c2bd006c7f9c695090f6

Parses *input* and returns the corresponding :sip:ref:`~PyQt6.QtCore.QUrl`. *input* is assumed to be in encoded form, containing only ASCII characters.

Parses the URL using *mode*. See :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` for more information on this parameter. :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is not permitted in this context.

**Note:** In Qt versions prior to 6.7, this function took a :sip:ref:`~PyQt6.QtCore.QByteArray`, not QByteArrayView. If you experience compile errors, it's because your code is passing objects that are implicitly convertible to :sip:ref:`~PyQt6.QtCore.QByteArray`, but not QByteArrayView. Wrap the corresponding argument in ``QByteArray{~~~}`` to make the cast explicit. This is backwards-compatible with old Qt versions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`.
