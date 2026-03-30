.. sip:method-description::
    :status: todo
    :pysig: 5237000fc3bc4f513a579caca380c129
    :realsig: (const QColor&)
    :digest: 562386547076b690515eaea93b8c5e5f

Fills the entire image with the given *color*.

If the depth of the image is 1, the image will be filled with 1 if *color* equals :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.color1`; it will otherwise be filled with 0.

If the depth of the image is 8, the image will be filled with the index corresponding the *color* in the color table if present; it will otherwise be filled with 0.
