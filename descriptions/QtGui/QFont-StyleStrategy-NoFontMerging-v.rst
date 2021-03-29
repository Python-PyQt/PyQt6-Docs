.. sip:enum-member-description::
    :status: todo
    :value: 0x8000
    :digest: 58b4e386564924205de8fd670b4b77c5

If the font selected for a certain writing system does not contain a character requested to draw, then Qt automatically chooses a similar looking font that contains the character. The  flag disables this feature. Please note that enabling this flag will not prevent Qt from automatically picking a suitable font when the selected font does not support the writing system of the text.
