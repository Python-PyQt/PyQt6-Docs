.. sip:enum-member-description::
    :status: todo
    :value: 0x8000
    :digest: 4f95ddd61fe8388c86fd04dde712eb37

If the font selected for a certain writing system does not contain a character requested to draw, then Qt automatically chooses a similar looking font that contains the character. The NoFontMerging flag disables this feature. Please note that enabling this flag will not prevent Qt from automatically picking a suitable font when the selected font does not support the writing system of the text.
