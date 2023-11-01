.. sip:method-description::
    :status: todo
    :pysig: dc45284078afec4c3444cbd2960ee438
    :realsig: (const char*)
    :digest: 757c698355a3b6c7c1765e5cd30058d5

Returns the encoded tag for *name* as defined in the OpenType font specification. The name must be a null-terminated string of four characters exactly, and in order to be a valid tag, each character must be in the basic Latin range of 0x20 to 0x7E.

The function returns 0 for strings of the wrong length, but does not otherwise check the input for validity.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.setFeature`, :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`, :sip:ref:`~PyQt6.QtGui.QFont.featureValue`, :sip:ref:`~PyQt6.QtGui.QFont.tagToString`.
