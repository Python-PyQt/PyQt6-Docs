.. sip:method-description::
    :status: todo
    :pysig: 1512a78beed0c522a2fd3dcdf28d9ecd
    :realsig: (const char*, quint32)
    :digest: bbf13b227ae16817ee515b00f6509ad2

This is an overloaded function.

Sets the *value* of a specific *feature*. This is an advanced feature which can be used to enable or disable specific OpenType features if they are available in the font.

See setFeature(quint32, quint32) for more details on font features.

**Note:** This is equivalent to calling setFeature(\ :sip:ref:`~PyQt6.QtGui.QFont.stringToTag`\ (feature), value).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.clearFeatures`, :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`, :sip:ref:`~PyQt6.QtGui.QFont.featureValue`, :sip:ref:`~PyQt6.QtGui.QFont.stringToTag`.
