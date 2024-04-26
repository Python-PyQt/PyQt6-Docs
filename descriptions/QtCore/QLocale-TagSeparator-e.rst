.. sip:enum-description::
    :status: todo
    :digest: 3c7c11997e0440832051e198b0720ea2

Indicate how to combine the parts that make up a locale identifier.

A locale identifier may be made up of several tags, indicating language, script and territory (plus, potentially, other details), joined together to form the identifier. Various standards and conventional forms use either a dash (the Unicode HYPHEN-MINUS, U+002D) or an underscore (LOW LINE, U+005F). Different clients of :sip:ref:`~PyQt6.QtCore.QLocale` may thus need one or the other.

**Note:** Although dash and underscore are the only separators used in public standards (as at 2023), it is possible to cast any `ASCII <https://en.cppreference.com/w/cpp/language/ascii>`_ character to this type if a non-standard ASCII separator is needed. Casting a non-ASCII character (with decimal value above 127) is not supported: such values are reserved for future use as enum members if some public standard ever uses a non-ASCII separator. It is, of course, possible to use QString::replace() to replace the separator used by a function taking a parameter of this type with an arbitrary Unicode character or string.
