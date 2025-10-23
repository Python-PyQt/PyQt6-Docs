.. sip:method-description::
    :status: todo
    :pysig: c849316e09957cb8822b92c9b7c01bc5
    :realsig: (const QJSValue&) const
    :digest: 9b039b781f2e7c355ca0a4aaafb71156

Returns true if this :sip:ref:`~PyQt6.QtQml.QJSValue` is equal to *other* using strict comparison (no conversion), otherwise returns false. The comparison follows the behavior described in `ECMA-262 <https://doc.qt.io/qt-6/https://www.ecma-international.org/publications-and-standards/standards/ecma-262/>`_ section 11.9.6, "The Strict Equality Comparison Algorithm".

If the type of this :sip:ref:`~PyQt6.QtQml.QJSValue` is different from the type of the *other* value, this function returns false. If the types are equal, the result depends on the type, as shown in the following table:

+-----------+----------------------------------------------------------------------------------------+
| Type      | Result                                                                                 |
+===========+========================================================================================+
| Undefined | true                                                                                   |
+-----------+----------------------------------------------------------------------------------------+
| Null      | true                                                                                   |
+-----------+----------------------------------------------------------------------------------------+
| Boolean   | true if values are both true or both false, false otherwise                            |
+-----------+----------------------------------------------------------------------------------------+
| Number    | false if either value is NaN (Not-a-Number); true if values are equal, false otherwise |
+-----------+----------------------------------------------------------------------------------------+
| String    | true if both values are exactly the same sequence of characters, false otherwise       |
+-----------+----------------------------------------------------------------------------------------+
| Object    | true if both values refer to the same object, false otherwise                          |
+-----------+----------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.equals`.
