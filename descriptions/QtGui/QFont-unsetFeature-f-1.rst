.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint32)
    :digest: 690ee8ebf56c8b95eaec2451df0f794d

This is an overloaded function.

Unsets the *tag* from the map of explicitly enabled/disabled features.

**Note:** Even if the feature has not previously been added, this will mark the font features map as modified in this :sip:ref:`~PyQt6.QtGui.QFont`, so that it will take precedence when resolving against other fonts.

Unsetting an existing feature on the :sip:ref:`~PyQt6.QtGui.QFont` reverts behavior to the default.

See setFeature(quint32, quint32) for more details on font features.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.clearFeatures`, :sip:ref:`~PyQt6.QtGui.QFont.setFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`, :sip:ref:`~PyQt6.QtGui.QFont.featureValue`, :sip:ref:`~PyQt6.QtGui.QFont.stringToTag`.
