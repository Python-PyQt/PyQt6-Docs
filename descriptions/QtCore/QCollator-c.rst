.. sip:class-description::
    :status: todo
    :brief: Compares strings according to a localized collation algorithm
    :digest: d7870ea0f25cf430067f69ebb36e4b73

The :sip:ref:`~PyQt6.QtCore.QCollator` class compares strings according to a localized collation algorithm.

:sip:ref:`~PyQt6.QtCore.QCollator` is initialized with a :sip:ref:`~PyQt6.QtCore.QLocale`. It can then be used to compare and sort strings in using the ordering appropriate to the locale.

A :sip:ref:`~PyQt6.QtCore.QCollator` object can be used together with template-based sorting algorithms, such as std::sort(), to sort a list with QString entries.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qcollator.py
    :lines: 54-59

In addition to the locale, several optional flags can be set that influence the result of the collation.

**Note:** On Linux, Qt is normally compiled to use ICU. When it isn't, all options are ignored and the only supported locales are the system default (that ``setlocale(LC_COLLATE, nullptr)`` would report) and the "C" locale.
