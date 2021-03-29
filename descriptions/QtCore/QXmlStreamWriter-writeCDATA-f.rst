.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: f1543cf5b0ef4c630fb5666c45893d1f

Writes *text* as CDATA section. If *text* contains the forbidden character sequence "]]>", it is split into different CDATA sections.

This function mainly exists for completeness. Normally you should not need use it, because :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeCharacters` automatically escapes all non-content characters.
