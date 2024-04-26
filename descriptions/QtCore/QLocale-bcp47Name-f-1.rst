.. sip:method-description::
    :status: todo
    :pysig: ef17c355a2e519cc8c6912d1f193ce5a
    :realsig: (QLocale::TagSeparator) const
    :digest: c907646a1efedad32d82c18ef9b04a81

Returns the BCP47 field names joined with dashes.

This combines as many of language, script and territory (and possibly other BCP47 fields) for this locale as are needed to uniquely specify it. Note that fields may be omitted if the Unicode consortium's :ref:`qlocale-matching-combinations-of-language-script-and-territory` imply the omitted fields when given those retained. See :sip:ref:`~PyQt6.QtCore.QLocale.name` for how to construct a string from individual fields, if some other format is needed.

Unlike :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`, the value returned by bcp47Name() represents the locale name of the :sip:ref:`~PyQt6.QtCore.QLocale` data; this need not be the language the user-interface should be in.

This function tries to conform the locale name to the IETF Best Common Practice 47, defined by RFC 5646. Since Qt 6.7, it supports an optional *separator* parameter which can be used to override the BCP47-specified use of a hyphen to separate the tags. For use in IETF-defined protocols, however, the default, :sip:ref:`~PyQt6.QtCore.QLocale.TagSeparator.Dash`, should be retained.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.name`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.territory`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`.
