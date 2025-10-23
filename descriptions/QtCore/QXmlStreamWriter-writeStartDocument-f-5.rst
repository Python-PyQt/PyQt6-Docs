.. sip:method-description::
    :status: todo
    :pysig: 547000f13f2e7a3400a249c3cc6ac740
    :realsig: (QAnyStringView)
    :digest: 3528a1600cc161be718c211bcb45b5b5

Writes a document start with the XML version number *version*.

**Note:** This function does not validate the version string and allows setting it manually. However, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` only supports XML 1.0. Setting a version string other than "1.0" does not change the writer's behavior or escaping rules. It is the caller's responsibility to ensure consistency between the declared version and the actual content.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEndDocument`.
