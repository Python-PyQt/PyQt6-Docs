.. sip:class-description::
    :status: todo
    :brief: Compares strings according to a localized collation algorithm
    :digest: d40491166a30519a7ec3c64e688208a6

The :sip:ref:`~PyQt6.QtCore.QCollator` class compares strings according to a localized collation algorithm.

:sip:ref:`~PyQt6.QtCore.QCollator` is initialized with a :sip:ref:`~PyQt6.QtCore.QLocale`. It can then be used to compare and sort strings by using the ordering appropriate for that locale.

A :sip:ref:`~PyQt6.QtCore.QCollator` object can be used together with template-based sorting algorithms, such as std::sort(), to sort a list with QString entries.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qcollator.py
    :lines: 54-59

In addition to the locale, several optional flags can be set that influence the result of the collation.

.. _qcollator-posix-fallback-implementation:

POSIX fallback implementation
-----------------------------

On Unix systems, Qt is normally compiled to use ICU (except for macOS, where Qt defaults to using an equivalent Apple API). However, if ICU was not available at compile time or explicitly disabled, Qt will use a fallback backend that uses the POSIX API only. This backend has several limitations:

* Only the :sip:ref:`~PyQt6.QtCore.QLocale.c` and :sip:ref:`~PyQt6.QtCore.QLocale.system` locales are supported. Consult the POSIX and C Standard Library manuals for the ``<locale.h>`` header for more information on the system locale.

* :sip:ref:`~PyQt6.QtCore.QCollator.caseSensitivity` is not supported: only case-sensitive collation can be performed.

* :sip:ref:`~PyQt6.QtCore.QCollator.numericMode` and :sip:ref:`~PyQt6.QtCore.QCollator.ignorePunctuation` are not supported.

The use of any of the unsupported options will cause a warning to be printed to the application's output.
