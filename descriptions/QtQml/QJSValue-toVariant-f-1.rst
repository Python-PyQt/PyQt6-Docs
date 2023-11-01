.. sip:method-description::
    :status: todo
    :pysig: 332a4d59d70101583e8b009fdba59639
    :realsig: (QJSValue::ObjectConversionBehavior) const
    :digest: ea0a2bacf470443ac069da07610b27c1

Returns the :sip:ref:`~PyQt6.QtCore.QVariant` value of this :sip:ref:`~PyQt6.QtQml.QJSValue`, if it can be converted to a :sip:ref:`~PyQt6.QtCore.QVariant`; otherwise returns an invalid :sip:ref:`~PyQt6.QtCore.QVariant`. Some JavaScript types and objects have native expressions in Qt. Those are converted to their native expressions. For example:

+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Input Type                                                       | Result                                                                                                             |
+==================================================================+====================================================================================================================+
| Undefined                                                        | An invalid :sip:ref:`~PyQt6.QtCore.QVariant`.                                                                      |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Null                                                             | A :sip:ref:`~PyQt6.QtCore.QVariant` containing a null pointer (\ :sip:ref:`~PyQt6.QtCore.QMetaType.Type.Nullptr`). |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Boolean                                                          | A :sip:ref:`~PyQt6.QtCore.QVariant` containing the value of the boolean.                                           |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Number                                                           | A :sip:ref:`~PyQt6.QtCore.QVariant` containing the value of the number.                                            |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| String                                                           | A :sip:ref:`~PyQt6.QtCore.QVariant` containing the value of the string.                                            |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QVariant` Object                         | The result is the :sip:ref:`~PyQt6.QtCore.QVariant` value of the object (no conversion).                           |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QObject` Object                          | A :sip:ref:`~PyQt6.QtCore.QVariant` containing a pointer to the :sip:ref:`~PyQt6.QtCore.QObject`.                  |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Date Object                                                      | A :sip:ref:`~PyQt6.QtCore.QVariant` containing the date value (\ :sip:ref:`~PyQt6.QtQml.QJSValue.toDateTime`).     |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QCborKnownTags.RegularExpression` Object | A :sip:ref:`~PyQt6.QtCore.QVariant` containing the regular expression value.                                       |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

For other types the *behavior* parameter is relevant. If ``ConvertJSObjects`` is given, a best effort but possibly lossy conversion is attempted. Generic JavaScript objects are converted to QVariantMap. JavaScript arrays are converted to QVariantList. Each property or element is converted to a :sip:ref:`~PyQt6.QtCore.QVariant`, recursively; cyclic references are not followed. JavaScript function objects are dropped. If ``RetainJSObjects`` is given, the :sip:ref:`~PyQt6.QtQml.QJSValue` is wrapped into a :sip:ref:`~PyQt6.QtCore.QVariant` via QVariant::fromValue(). The resulting conversion is lossless but the internal structure of the objects is not immediately accessible.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.isVariant`.
