.. sip:enum-member-description::
    :status: todo
    :value: 0x08
    :digest: 23571a3bd76fc60d19a24f4ec60665d2

Allow text to be positioned at fractions of pixels vertically as well as horizontally, if this is supported by the font engine. This is currently supported by Freetype on all platforms when the hinting preference is :sip:ref:`~PyQt6.QtGui.QFont.HintingPreference.PreferNoHinting`, and also on macOS. For most use cases this will not improve visual quality, but may increase memory consumption and some reduction in text rendering performance. Therefore, enabling this is not recommended unless the use case requires it. One such use case could be aligning glyphs with other visual primitives. This value was added in Qt 6.1.
