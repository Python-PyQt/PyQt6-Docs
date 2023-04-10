.. sip:method-description::
    :status: todo
    :pysig: 81445f071599e8ca359c5cd31fa289a9
    :realsig: (QAnyStringView)
    :digest: f9daa54cc69071c96b03e7b9a99a7811

Writes *text*. The characters "<", "&", and """ are escaped as entity references "&lt;", "&amp;, and "&quot;". To avoid the forbidden sequence "]]>", ">" is also escaped as "&gt;".

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEntityReference`.
