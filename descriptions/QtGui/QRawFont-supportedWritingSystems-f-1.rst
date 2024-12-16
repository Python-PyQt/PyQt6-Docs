.. sip:method-description::
    :status: todo
    :pysig: ffe6771a0f9c9a22e8a7eb9f47951874
    :realsig: () const
    :digest: 9381e08ce0fad61285720dbfed3af98d

Returns a list of writing systems supported by the font according to designer supplied information in the font file. Please note that this does not guarantee support for a specific unicode point in the font. You can use the :sip:ref:`~PyQt6.QtGui.QRawFont.supportsCharacter` to check support for a single, specific character.

**Note:** The list is determined based on the unicode ranges and codepage ranges set in the font's OS/2 table and requires such a table to be present in the underlying font file.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QRawFont.supportsCharacter`.
