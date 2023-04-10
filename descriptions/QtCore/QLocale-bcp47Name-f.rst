.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 4d2506ead54ef65cdf8dc68961b9479d

Returns the BCP47 field names joined with dashes.

This combines as many of language, script and territory (and possibly other BCP47 fields) for this locale as are needed to uniquely specify it. Note that fields may be omitted if the Unicode consortium's :ref:`qlocale-matching-combinations-of-language-script-and-territory` imply the omitted fields when given those retained. See :sip:ref:`~PyQt6.QtCore.QLocale.name` for how to construct a string from individual fields, if some other format is needed.

Unlike :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`, the value returned by bcp47Name() represents the locale name of the :sip:ref:`~PyQt6.QtCore.QLocale` data; this need not be the language the user-interface should be in.

This function tries to conform the locale name to BCP47.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.name`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.territory`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`.
