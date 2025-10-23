.. sip:class-description::
    :status: todo
    :brief: Internationalization support for text output
    :digest: 72ac9ad85017d9a8e7745bb3e21906e1

The :sip:ref:`~PyQt6.QtCore.QTranslator` class provides internationalization support for text output.

An object of this class contains a set of translations from a source language to a target language. :sip:ref:`~PyQt6.QtCore.QTranslator` provides functions to look up translations in a translation file. Translation files are created using Qt Linguist.

The most common use of :sip:ref:`~PyQt6.QtCore.QTranslator` is to: load a translation file, and install it using :sip:ref:`~PyQt6.QtCore.QCoreApplication.installTranslator`.

Here's an example ``main()`` function using the :sip:ref:`~PyQt6.QtCore.QTranslator`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-hellotrmain.py
    :lines: 54-68

Note that the translator must be created *before* the application's widgets.

Most applications will never need to do anything else with this class. The other functions provided by this class are useful for applications that work on translator files.

.. _qtranslator-looking-up-translations:

Looking up Translations
-----------------------

It is possible to look up a translation using :sip:ref:`~PyQt6.QtCore.QTranslator.translate` (as tr() and :sip:ref:`~PyQt6.QtCore.QCoreApplication.translate` do). The :sip:ref:`~PyQt6.QtCore.QTranslator.translate` function takes up to three parameters:

* The *context* - usually the class name for the tr() caller.

* The *source text* - usually the argument to tr().

* The *disambiguation* - an optional string that helps disambiguate different uses of the same text in the same context.

For example, the "Cancel" in a dialog might have "Anuluj" when the program runs in Polish (in this case the source text would be "Cancel"). The context would (normally) be the dialog's class name; there would normally be no comment, and the translated text would be "Anuluj".

But it's not always so simple. The Spanish version of a printer dialog with settings for two-sided printing and binding would probably require both "Activado" and "Activada" as translations for "Enabled". In this case the source text would be "Enabled" in both cases, and the context would be the dialog's class name, but the two items would have disambiguations such as "two-sided printing" for one and "binding" for the other. The disambiguation enables the translator to choose the appropriate gender for the Spanish version, and enables Qt to distinguish between translations.

.. _qtranslator-using-multiple-translations:

Using Multiple Translations
---------------------------

Multiple translation files can be installed in an application. Translations are searched for in the reverse order in which they were installed, so the most recently installed translation file is searched for translations first and the earliest translation file is searched last. The search stops as soon as a translation containing a matching string is found.

This mechanism makes it possible for a specific translation to be "selected" or given priority over the others; simply uninstall the translator from the application by passing it to the :sip:ref:`~PyQt6.QtCore.QCoreApplication.removeTranslator` function and reinstall it with :sip:ref:`~PyQt6.QtCore.QCoreApplication.installTranslator`. It will then be the first translation to be searched for matching strings.

.. _qtranslator-security-considerations:

Security Considerations
-----------------------

Only install translation files from trusted sources.

Translation files are binary files that are generated from text-based translation source files. The format of these binary files is strictly defined by Qt and any manipulation of the data in the binary file may crash the application when the file is loaded. Furthermore, even well-formed translation files may contain misleading or malicious translations.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.installTranslator`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.removeTranslator`, :sip:ref:`~PyQt6.QtCore.QObject.tr`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.translate`.
