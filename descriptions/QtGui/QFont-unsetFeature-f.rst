.. sip:method-description::
    :status: todo
    :pysig: 4b3a6218bb3e3a7303e8a171a60fcf92
    :realsig: (const char*)
    :digest: a4c7589dac53cb251657d551f714b131

This is an overloaded function.

Unsets the *feature* from the map of explicitly enabled/disabled features.

**Note:** Even if the feature has not previously been added, this will mark the font features map as modified in this :sip:ref:`~PyQt6.QtGui.QFont`, so that it will take precedence when resolving against other fonts.

Unsetting an existing feature on the :sip:ref:`~PyQt6.QtGui.QFont` reverts behavior to the default.

See setFeature(quint32, quint32) for more details on font features.

**Note:** This is equivalent to calling :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`\ (\ :sip:ref:`~PyQt6.QtGui.QFont.stringToTag`\ (feature)).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.clearFeatures`, :sip:ref:`~PyQt6.QtGui.QFont.setFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`, :sip:ref:`~PyQt6.QtGui.QFont.featureValue`, :sip:ref:`~PyQt6.QtGui.QFont.stringToTag`.
