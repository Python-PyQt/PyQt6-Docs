.. sip:class-description::
    :status: todo
    :brief: Way to read and write JSON documents
    :digest: 79d84d2dd7628bf3d1244830d7c4ade9

The :sip:ref:`~PyQt6.QtCore.QJsonDocument` class provides a way to read and write JSON documents.

:sip:ref:`~PyQt6.QtCore.QJsonDocument` is a class that wraps a complete JSON document and can read this document from, and write it to, a UTF-8 encoded text-based representation.

A JSON document can be converted from its text-based representation to a :sip:ref:`~PyQt6.QtCore.QJsonDocument` using :sip:ref:`~PyQt6.QtCore.QJsonDocument.fromJson`. :sip:ref:`~PyQt6.QtCore.QJsonDocument.toJson` converts it back to text. The parser is very fast and efficient and converts the JSON to the binary representation used by Qt.

Validity of the parsed document can be queried with !\ :sip:ref:`~PyQt6.QtCore.QJsonDocument.isNull`

A document can be queried as to whether it contains an array or an object using :sip:ref:`~PyQt6.QtCore.QJsonDocument.isArray` and :sip:ref:`~PyQt6.QtCore.QJsonDocument.isObject`. The array or object contained in the document can be retrieved using :sip:ref:`~PyQt6.QtCore.QJsonDocument.array` or :sip:ref:`~PyQt6.QtCore.QJsonDocument.object` and then read or manipulated.

.. seealso:: `JSON Support in Qt <https://doc.qt.io/qt-6/json.html>`_, `JSON Save Game Example <https://doc.qt.io/qt-6/qtcore-serialization-savegame-example.html>`_.
