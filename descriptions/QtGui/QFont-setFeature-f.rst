.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (quint32, quint32)
    :digest: a44853f221ce9b48f3f573798a158ebf

This is an overloaded function.

Applies an integer value to a specific typographical feature when shaping the text. This provides advanced access to the font shaping process, and can be used to support font features that are otherwise not covered in the API.

A feature is defined by a 32-bit *tag* (encoded from the four-character name of the table by using the :sip:ref:`~PyQt6.QtGui.QFont.stringToTag` function), as well as an integer value.

This integer *value* passed along with the tag in most cases represents a boolean value: A zero value means the feature is disabled, and a non-zero value means it is enabled. For certain font features, however, it may have other intepretations. For example, when applied to the ``salt`` feature, the value is an index that specifies the stylistic alternative to use.

For example, the ``frac`` font feature will convert diagonal fractions separated with a slash (such as ``1/2``) with a different representation. Typically this will involve baking the full fraction into a single character width (such as ``½``).

If a font supports the ``frac`` feature, then it can be enabled in the shaper by setting ``features[stringToTag("frac")] = 1`` in the font feature map.

**Note:** By default, Qt will enable and disable certain font features based on other font properties. In particular, the ``kern`` feature will be enabled/disabled depending on the :sip:ref:`~PyQt6.QtGui.QFont.kerning` property of the :sip:ref:`~PyQt6.QtGui.QFont`. In addition, all ligature features (``liga``, ``clig``, ``dlig``, ``hlig``) will be disabled if a :sip:ref:`~PyQt6.QtGui.QFont.letterSpacing` is applied, but only for writing systems where the use of ligature is cosmetic. For writing systems where ligatures are required, the features will remain in their default state. The values set using :sip:ref:`~PyQt6.QtGui.QFont.setFeature` and related functions will override the default behavior. If, for instance, the feature "kern" is set to 1, then kerning will always be enabled, regardless of whether the kerning property is set to false. Similarly, if it is set to 0, then it will always be disabled. To reset a font feature to its default behavior, you can unset it using :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.clearFeatures`, :sip:ref:`~PyQt6.QtGui.QFont.setFeature`, :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`, :sip:ref:`~PyQt6.QtGui.QFont.stringToTag`.
