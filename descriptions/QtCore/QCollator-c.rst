.. sip:class-description::
    :status: todo
    :brief: Compares strings according to a localized collation algorithm
    :digest: a901c152d8aa08b2846dd2d185a5a9a4

The :sip:ref:`~PyQt6.QtCore.QCollator` class compares strings according to a localized collation algorithm.

:sip:ref:`~PyQt6.QtCore.QCollator` is initialized with a :sip:ref:`~PyQt6.QtCore.QLocale` and an optional collation strategy. It tries to initialize the collator with the specified values. The collator can then be used to compare and sort strings in a locale dependent fashion.

A :sip:ref:`~PyQt6.QtCore.QCollator` object can be used together with template based sorting algorithms such as std::sort to sort a list of QStrings.

In addition to the locale and collation strategy, several optional flags can be set that influence the result of the collation.
