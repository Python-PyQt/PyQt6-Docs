.. sip:class-description::
    :status: todo
    :brief: Way of finding Unicode text boundaries in a string
    :digest: e600d7a5256ff163cf3381251c771717

The :sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder` class provides a way of finding Unicode text boundaries in a string.

:sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder` allows to find Unicode text boundaries in a string, accordingly to the Unicode text boundary specification (see `Unicode Standard Annex #14 <http://www.unicode.org/reports/tr14/>`_ and `Unicode Standard Annex #29 <http://www.unicode.org/reports/tr29/>`_).

:sip:ref:`~PyQt6.QtCore.QTextBoundaryFinder` can operate on a QString in four possible modes depending on the value of *BoundaryType*.

Units of Unicode characters that make up what the user thinks of as a character or basic unit of the language are here called Grapheme clusters. The two unicode characters 'A' + diaeresis do for example form one grapheme cluster as the user thinks of them as one character, yet it is in this case represented by two unicode code points (see `http://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries <http://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries>`_).

Word boundaries are there to locate the start and end of what a language considers to be a word (see `http://www.unicode.org/reports/tr29/#Word_Boundaries <http://www.unicode.org/reports/tr29/#Word_Boundaries>`_).

Line break boundaries give possible places where a line break might happen and sentence boundaries will show the beginning and end of whole sentences (see `http://www.unicode.org/reports/tr29/#Sentence_Boundaries <http://www.unicode.org/reports/tr29/#Sentence_Boundaries>`_ and `http://www.unicode.org/reports/tr14/ <http://www.unicode.org/reports/tr14/>`_).

The first position in a string is always a valid boundary and refers to the position before the first character. The last position at the length of the string is also valid and refers to the position after the last character.
