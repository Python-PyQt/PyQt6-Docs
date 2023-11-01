.. sip:method-description::
    :status: todo
    :pysig: ef2adf66f578d6c2baebf8db54110fe2
    :realsig: (const char*,const char*,const char*,int)
    :digest: 7664f186fc7cd1f069d051c48d695817

Returns the translation text for *sourceText*, by querying the installed translation files. The translation files are searched from the most recently installed file back to the first installed file.

:sip:ref:`~PyQt6.QtCore.QObject.tr` provides this functionality more conveniently.

*context* is typically a class name (e.g., "MyDialog") and *sourceText* is either English text or a short identifying text.

*disambiguation* is an identifying string, for when the same *sourceText* is used in different roles within the same context. By default, it is ``nullptr``.

See the :sip:ref:`~PyQt6.QtCore.QTranslator` and :sip:ref:`~PyQt6.QtCore.QObject.tr` documentation for more information about contexts, disambiguations and comments.

*n* is used in conjunction with ``%n`` to support plural forms. See :sip:ref:`~PyQt6.QtCore.QObject.tr` for details.

If none of the translation files contain a translation for *sourceText* in *context*, this function returns a QString equivalent of *sourceText*.

This function is not virtual. You can use alternative translation techniques by subclassing :sip:ref:`~PyQt6.QtCore.QTranslator`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.tr`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.installTranslator`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.removeTranslator`, :ref:`qcoreapplication-internationalization-and-translations`.
