.. sip:method-description::
    :status: todo
    :pysig: 39aaf14661efa90a77ee054098b0fc5c
    :realsig: (QMetaType) const
    :digest: 3a0e85895215949737c70fd723609fbb

Returns ``true`` if the variant's type can be cast to the requested type, *type*. Such casting is done automatically when calling the toInt(), toBool(), ... methods.

Note this function operates only on the variant's type, not the contents. It indicates whether there is a conversion path from this variant to *type*, not that the conversion will succeed when attempted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaType.canConvert`.
