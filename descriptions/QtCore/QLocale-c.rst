.. sip:class-description::
    :status: todo
    :brief: Converts between numbers and their string representations in various languages
    :digest: 3df4da95b78c98b089eca8058450e7ea

The :sip:ref:`~PyQt6.QtCore.QLocale` class converts between numbers and their string representations in various languages.

:sip:ref:`~PyQt6.QtCore.QLocale` is constructed for a specified language, optional script and territory. It offers various facilities for formatting data as text, localized appropriately, and for reading data out of localized text.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 54-59

:sip:ref:`~PyQt6.QtCore.QLocale` supports the concept of a default locale, which is determined from the system's locale settings at application startup. The default locale can be changed by calling the static member :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`. Setting the default locale has the following effects:

* If a :sip:ref:`~PyQt6.QtCore.QLocale` object is constructed with the default constructor, it will use the default locale's settings.

* QString::arg() uses the default locale to format a number when its position specifier in the format string contains an 'L', e.g. "%L1".

The following example illustrates how to use :sip:ref:`~PyQt6.QtCore.QLocale` directly:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 64-82

An alternative method for constructing a :sip:ref:`~PyQt6.QtCore.QLocale` object is by specifying the locale name.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 87-88

This constructor reads the language, script and/or territory from the given name, accepting either uderscore or dash as separator (and ignoring any trailing ``.codeset`` or ``@variant`` suffix).

**Note:** For the current keyboard input locale take a look at :sip:ref:`~PyQt6.QtGui.QInputMethod.locale`.

.. _qlocale-appropriateness-of-the-formats:

Appropriateness of the formats
------------------------------

:sip:ref:`~PyQt6.QtCore.QLocale`'s data is based on Common Locale Data Repository v46.1.

This data is published by The Unicode Consortium, who aim to follow customary, common use by writers of each language, in each script, in each territory for which data is given. This may in some cases differ from what is recognized as official, depending on how widely that official standard is followed in practice.

For example, although the relevant international standard (from the BIPM) mandates a thin non-breaking space as the separator between groups of digits in numbers, when they are split up to aid readability, and many jurisdictions have adopted this as their official standard for the formatting of numbers, many locales in fact have a traditional way of formatting numbers with punctuators separating groups of digits. CLDR, and thus :sip:ref:`~PyQt6.QtCore.QLocale`, follows this common usage rather than the official standard.

.. _qlocale-matching-combinations-of-language-script-and-territory:

Matching combinations of language, script and territory
-------------------------------------------------------

:sip:ref:`~PyQt6.QtCore.QLocale` has data, derived from CLDR, for many combinations of language, script and territory, but not all. If it is constructed with all three of these key values specified (treating ``AnyLanguage``, ``AnyScript`` or ``AnyTerritory`` as unspecified) and :sip:ref:`~PyQt6.QtCore.QLocale` has data for the given combination, this data is used. Otherwise, :sip:ref:`~PyQt6.QtCore.QLocale` does its best to find a sensible combination of language, script and territory, for which it does have data, that matches those that were specified.

The CLDR provides tables of likely combinations, which are used to fill in any unspecified key or keys; if :sip:ref:`~PyQt6.QtCore.QLocale` has data for the result of such a likely combination, that is used. If no language is specified, and none can be determined from script and territory, or if :sip:ref:`~PyQt6.QtCore.QLocale` has no data for the language, the "C" locale (when reading the keys from a string) or default locale (otherwise) is used.

When :sip:ref:`~PyQt6.QtCore.QLocale` has no data for the keys specified, with likely keys filled in where unspecified, but does have data for the resulting language, a fall-back is sought, based on ignoring either territory, script or both (in that order). This results in a :sip:ref:`~PyQt6.QtCore.QLocale` which may not match what was asked for, but provides localization that's as suitable as the available data permits, for the keys specified.

Use :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.script` and :sip:ref:`~PyQt6.QtCore.QLocale.territory` to determine the actual keys used.

.. seealso:: QString::arg(), :sip:ref:`~PyQt6.QtGui.QInputMethod.locale`.
