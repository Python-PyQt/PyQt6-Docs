.. sip:method-description::
    :status: todo
    :pysig: 9bc29bafb178397ce4c22d82b34e6148
    :realsig: (const char*,const char*,const char*,int) const
    :digest: 76d2ace2c62c63b8bc9e27a441751b59

Returns the translation for the key (\ *context*, *sourceText*, *disambiguation*). If none is found, also tries (\ *context*, *sourceText*, ""). If that still fails, returns a null string.

**Note:** Incomplete translations may result in unexpected behavior: If no translation for (\ *context*, *sourceText*, "") is provided, the method might in this case actually return a translation for a different *disambiguation*.

If *n* is not -1, it is used to choose an appropriate form for the translation (e.g. "%n file found" vs. "%n files found").

If you need to programatically insert translations into a :sip:ref:`~PyQt6.QtCore.QTranslator`, this function can be reimplemented.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTranslator.load`.
