.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 613e7c1963e5da24b4d8036890a032af

Writes *text*. The characters "<", "&", and """ are escaped as entity references "&lt;", "&amp;, and "&quot;". To avoid the forbidden sequence "]]>", ">" is also escaped as "&gt;".

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEntityReference`.
