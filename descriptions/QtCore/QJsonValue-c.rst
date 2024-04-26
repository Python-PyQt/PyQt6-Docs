.. sip:class-description::
    :status: todo
    :brief: Encapsulates a value in JSON
    :digest: 9c180d88fbd8900304cdc4d8b85d6be7

The :sip:ref:`~PyQt6.QtCore.QJsonValue` class encapsulates a value in JSON.

A value in JSON can be one of 6 basic types:

JSON is a format to store structured data. It has 6 basic data types:

* bool :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.Bool`

* double :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.Double`

* string :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.String`

* array :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.Array`

* object :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.Object`

* null :sip:ref:`~PyQt6.QtCore.QJsonValue.Type.Null`

A value can represent any of the above data types. In addition, :sip:ref:`~PyQt6.QtCore.QJsonValue` has one special flag to represent undefined values. This can be queried with :sip:ref:`~PyQt6.QtCore.QJsonValue.isUndefined`.

The type of the value can be queried with :sip:ref:`~PyQt6.QtCore.QJsonValue.type` or accessors like :sip:ref:`~PyQt6.QtCore.QJsonValue.isBool`, :sip:ref:`~PyQt6.QtCore.QJsonValue.isString`, and so on. Likewise, the value can be converted to the type stored in it using the :sip:ref:`~PyQt6.QtCore.QJsonValue.toBool`, :sip:ref:`~PyQt6.QtCore.QJsonValue.toString` and so on.

Values are strictly typed internally and contrary to :sip:ref:`~PyQt6.QtCore.QVariant` will not attempt to do any implicit type conversions. This implies that converting to a type that is not stored in the value will return a default constructed return value.

.. _qjsonvalue-qjsonvalueref:

QJsonValueRef
-------------

:ref:`qjsonvalue-qjsonvalueref` is a helper class for QJsonArray and QJsonObject. When you get an object of type :ref:`qjsonvalue-qjsonvalueref`, you can use it as if it were a reference to a :sip:ref:`~PyQt6.QtCore.QJsonValue`. If you assign to it, the assignment will apply to the element in the QJsonArray or QJsonObject from which you got the reference.

The following methods return :ref:`qjsonvalue-qjsonvalueref`:

* QJsonArray::operator[](qsizetype i)

* QJsonObject::operator[](const QString & key) const

.. seealso:: `JSON Support in Qt <https://doc.qt.io/qt-6/json.html>`_, `Saving and Loading a Game <https://doc.qt.io/qt-6/qtcore-serialization-savegame-example.html>`_.
