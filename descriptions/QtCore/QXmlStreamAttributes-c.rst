.. sip:class-description::
    :status: todo
    :brief: Represents a vector of QXmlStreamAttribute
    :digest: 8b8b825a2b5675c71ac8a6339c97291e

The :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes` class represents a vector of :sip:ref:`~PyQt6.QtCore.QXmlStreamAttribute`.

Attributes are returned by a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader` in :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.attributes` when the reader reports a :sip:ref:`~PyQt6.QtCore.QXmlStreamReader.TokenType.StartElement`. The class can also be used with a :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` as an argument to :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttributes`.

The convenience function :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes.value` loops over the vector and returns an attribute value for a given namespaceUri and an attribute's name.

New attributes can be added with :sip:ref:`~PyQt6.QtCore.QXmlStreamAttributes.append`.
