.. sip:method-description::
    :status: todo
    :pysig: 0c6845b55096a8baa01dbf69e44664ed
    :realsig: (QChar::Script, const QString&)
    :digest: e9231d1fad8b6b699d750bb72f111509

Adds *familyName* as an application-defined fallback font for *script*.

When Qt encounters characters that are not supported by the selected font, it will search through a list of fallback fonts to find a match for them. This ensures that combining multiple scripts in a single string is possible, even if the main font does not support them.

The list of fallback fonts is selected based on the script of the string as well as other conditions, such as system language.

While the system fallback list is usually sufficient, there are cases where it is useful to override the default behavior. One such case is for using application fonts as fallback to ensure cross-platform consistency.

In another case the application may be written in a script with regional differences and want to run it untranslated in multiple regions. In this case, it might be useful to override the local region's fallback with one that matches the language of the application.

By passing *familyName* to addApplicationFallbackFontFamily(), this will become the preferred family when matching missing characters from *script*. The *script* must be a valid script (``QChar::Script_Latin`` or higher). When adding multiple fonts for the same script, they will be prioritized in reverse order, so that the last family added will be checked first and so on.

**Note:** Qt's font matching algorithm considers ``QChar::Script_Common`` (undetermined script) and ``QChar::Script_Latin`` the same. Adding a fallback for either of these will also apply to the other.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.setApplicationFallbackFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFallbackFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFallbackFontFamilies`.
