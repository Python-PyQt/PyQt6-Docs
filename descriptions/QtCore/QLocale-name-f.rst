.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: c672cc70052ef1b6b085d222d5626bfa

Returns the language and country of this locale as a string of the form "language_country", where language is a lowercase, two-letter ISO 639 language code, and country is an uppercase, two- or three-letter ISO 3166 country code.

Note that even if :sip:ref:`~PyQt6.QtCore.QLocale` object was constructed with an explicit script,  will not contain it for compatibility reasons. Use :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name` instead if you need a full locale name.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.country`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.
