.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6b07c2a6d89a829d5f68fbc091491ec4

Returns ``true`` if the source effectively is a pixmap, e.g., a :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`.

This function is useful for optimization purposes. For instance, there's no point in drawing the source in device coordinates to avoid pixmap scaling if this function returns ``true`` - the source pixmap will be scaled anyways.
