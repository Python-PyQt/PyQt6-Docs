.. sip:class-description::
    :status: todo
    :brief: 16-bit Unicode character
    :digest: 121220c27ce1438e4ab4d101337ff90e

The :sip:ref:`~PyQt6.QtCore.QChar` class provides a 16-bit Unicode character.

In Qt, Unicode characters are 16-bit entities without any markup or structure. This class represents such an entity. It is lightweight, so it can be used everywhere. Most compilers treat it like an ``unsigned short``.

:sip:ref:`~PyQt6.QtCore.QChar` provides a full complement of testing/classification functions, converting to and from other formats, converting from composed to decomposed Unicode, and trying to compare and case-convert if you ask it to.

The classification functions include functions like those in the standard C++ header <cctype> (formerly <ctype.h>), but operating on the full range of Unicode characters, not just for the ASCII range. They all return true if the character is a certain type of character; otherwise they return false. These classification functions are isNull() (returns ``true`` if the character is '\\0'), isPrint() (true if the character is any sort of printable character, including whitespace), isPunct() (any sort of punctation), isMark() (Unicode Mark), isLetter() (a letter), isNumber() (any sort of numeric character, not just 0-9), isLetterOrNumber(), and isDigit() (decimal digits). All of these are wrappers around category() which return the Unicode-defined category of each character. Some of these also calculate the derived properties (for example isSpace() returns ``true`` if the character is of category Separator_\* or an exceptional code point from Other_Control category).

:sip:ref:`~PyQt6.QtCore.QChar` also provides direction(), which indicates the "natural" writing direction of this character. The joiningType() function indicates how the character joins with it's neighbors (needed mostly for Arabic or Syriac) and finally hasMirrored(), which indicates whether the character needs to be mirrored when it is printed in it's "unnatural" writing direction.

Composed Unicode characters (like *ring*) can be converted to decomposed Unicode ("a" followed by "ring above") by using decomposition().

In Unicode, comparison is not necessarily possible and case conversion is very difficult at best. Unicode, covering the "entire" world, also includes most of the world's case and sorting problems. operator==() and friends will do comparison based purely on the numeric Unicode value (code point) of the characters, and toUpper() and toLower() will do case changes when the character has a well-defined uppercase/lowercase equivalent. For locale-dependent comparisons, use QString::localeAwareCompare().

The conversion functions include unicode() (to a scalar), toLatin1() (to scalar, but converts all non-Latin-1 characters to 0), row() (gives the Unicode row), cell() (gives the Unicode cell), digitValue() (gives the integer value of any of the numerous digit characters), and a host of constructors.

:sip:ref:`~PyQt6.QtCore.QChar` provides constructors and cast operators that make it easy to convert to and from traditional 8-bit ``char``\ s. If you defined ``QT_NO_CAST_FROM_ASCII`` and ``QT_NO_CAST_TO_ASCII``, as explained in the QString documentation, you will need to explicitly call fromLatin1(), or use QLatin1Char, to construct a :sip:ref:`~PyQt6.QtCore.QChar` from an 8-bit ``char``, and you will need to call toLatin1() to get the 8-bit value back.

Starting with Qt 6.0, most :sip:ref:`~PyQt6.QtCore.QChar` constructors are ``explicit``. This is done to avoid dangerous mistakes when accidentally mixing integral types and strings.

For more information see `"About the Unicode Character Database" <https://www.unicode.org/ucd/>`_.

.. seealso:: QString, QLatin1Char, Unicode.
