.. sip:class-description::
    :status: todo
    :brief: Converts between numbers and their string representations in various languages
    :digest: bc57bafc292d13f99474dcac00ffe598

The :sip:ref:`~PyQt6.QtCore.QLocale` class converts between numbers and their string representations in various languages.

:sip:ref:`~PyQt6.QtCore.QLocale` is initialized with a language/country pair in its constructor and offers number-to-string and string-to-number conversion functions similar to those in QString.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 54-59

:sip:ref:`~PyQt6.QtCore.QLocale` supports the concept of a default locale, which is determined from the system's locale settings at application startup. The default locale can be changed by calling the static member :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`. Setting the default locale has the following effects:

* If a :sip:ref:`~PyQt6.QtCore.QLocale` object is constructed with the default constructor, it will use the default locale's settings.

* QString::toInt(), QString::toDouble(), etc., interpret the string according to the default locale. If this fails, it falls back on the "C" locale.

* QString::arg() uses the default locale to format a number when its position specifier in the format string contains an 'L', e.g. "%L1".

The following example illustrates how to use :sip:ref:`~PyQt6.QtCore.QLocale` directly:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 64-82

When a language/country pair is specified in the constructor, one of three things can happen:

* If the language/country pair is found in the database, it is used.

* If the language is found but the country is not, or if the country is ``AnyCountry``, the language is used with the most appropriate available country (for example, Germany for German),

* If neither the language nor the country are found, :sip:ref:`~PyQt6.QtCore.QLocale` defaults to the default locale (see :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`).

Use :sip:ref:`~PyQt6.QtCore.QLocale.language` and :sip:ref:`~PyQt6.QtCore.QLocale.country` to determine the actual language and country values used.

An alternative method for constructing a :sip:ref:`~PyQt6.QtCore.QLocale` object is by specifying the locale name.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 87-88

This constructor converts the locale name to a language/country pair; it does not use the system locale database.

**Note:** For the current keyboard input locale take a look at :sip:ref:`~PyQt6.QtGui.QInputMethod.locale`.

:sip:ref:`~PyQt6.QtCore.QLocale`'s data is based on Common Locale Data Repository v38.

.. seealso:: QString::arg(), QString::toInt(), QString::toDouble(), :sip:ref:`~PyQt6.QtGui.QInputMethod.locale`.
