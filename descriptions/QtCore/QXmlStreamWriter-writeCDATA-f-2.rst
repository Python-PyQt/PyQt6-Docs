.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: e0d87f89b6433f9048ada230e082a543

Writes *text* as CDATA section. If *text* contains the forbidden character sequence "]]>", it is split into different CDATA sections.

This function mainly exists for completeness. Normally you should not need use it, because :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeCharacters` automatically escapes all non-content characters.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
