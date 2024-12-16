.. sip:enum-member-description::
    :status: todo
    :value: 0x2000
    :digest: 07137cadbcdcb670056c4780d98e5c26

If the selected font does not contain a certain character, then Qt automatically chooses a similar-looking fallback font that contains the character. By default this is done on a character-by-character basis. This means that in certain uncommon cases, multiple fonts may be used to represent one string of text even if it's in the same script. Setting ``ContextFontMerging`` will try finding the fallback font that matches the largest subset of the input string instead. This will be more expensive for strings where missing glyphs occur, but may give more consistent results. If ``NoFontMerging`` is set, then ``ContextFontMerging`` will have no effect.
