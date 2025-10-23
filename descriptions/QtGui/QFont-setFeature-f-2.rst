.. sip:method-description::
    :status: todo
    :pysig: a0197453317bb7ca87df12ecdeed49f3
    :realsig: (QFont::Tag, quint32)
    :digest: 1cf1a806016920a95a12b3534ac5ff8d

Applies an integer value to the typographical feature specified by *tag* when shaping the text. This provides advanced access to the font shaping process, and can be used to support font features that are otherwise not covered in the API.

The feature is specified by a :sip:ref:`~PyQt6.QtGui.QFont.Tag`, which is typically encoded from the four-character feature name in the font feature map.

This integer *value* passed along with the tag in most cases represents a boolean value: A zero value means the feature is disabled, and a non-zero value means it is enabled. For certain font features, however, it may have other interpretations. For example, when applied to the ``salt`` feature, the value is an index that specifies the stylistic alternative to use.

For example, the ``frac`` font feature will convert diagonal fractions separated with a slash (such as ``1/2``) with a different representation. Typically this will involve baking the full fraction into a single character width (such as ``½``).

If a font supports the ``frac`` feature, then it can be enabled in the shaper by setting ``features["frac"] = 1`` in the font feature map.

**Note:** By default, Qt will enable and disable certain font features based on other font properties. In particular, the ``kern`` feature will be enabled/disabled depending on the :sip:ref:`~PyQt6.QtGui.QFont.kerning` property of the :sip:ref:`~PyQt6.QtGui.QFont`. In addition, all ligature features (``liga``, ``clig``, ``dlig``, ``hlig``) will be disabled if a :sip:ref:`~PyQt6.QtGui.QFont.letterSpacing` is applied, but only for writing systems where the use of ligature is cosmetic. For writing systems where ligatures are required, the features will remain in their default state. The values set using setFeature() and related functions will override the default behavior. If, for instance, the feature "kern" is set to 1, then kerning will always be enabled, regardless of whether the kerning property is set to false. Similarly, if it is set to 0, then it will always be disabled. To reset a font feature to its default behavior, you can unset it using :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.Tag`, :sip:ref:`~PyQt6.QtGui.QFont.clearFeatures`, :sip:ref:`~PyQt6.QtGui.QFont.unsetFeature`, :sip:ref:`~PyQt6.QtGui.QFont.featureTags`.
