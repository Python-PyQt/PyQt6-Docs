.. sip:method-description::
    :status: todo
    :pysig: a809066194c68e595c18fee038a13409
    :realsig: (QFont::Tag)
    :digest: 56efbcb8b0485b2bd8fa1750590ca1b9

This is an overloaded function.

Unsets the *tag* from the map of explicitly enabled/disabled features.

**Note:** Even if the feature has not previously been added, this will mark the font features map as modified in this :sip:ref:`~PyQt6.QtGui.QFont`, so that it will take precedence when resolving against other fonts.

Unsetting an existing feature on the :sip:ref:`~PyQt6.QtGui.QFont` reverts behavior to the default.

See :sip:ref:`~PyQt6.QtGui.QFont.setFeature` for more details on font features.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.Tag`, :sip:ref:`~PyQt6.QtGui.QFont.clearFeatures`, :sip:ref:`~PyQt6.QtGui.QFont.setFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`, :sip:ref:`~PyQt6.QtGui.QFont.featureValue`.
