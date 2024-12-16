.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 4a607c36870e25d488b52687dbe893d3

Returns true if this :sip:ref:`~PyQt6.QtQml.QJSValue` is a variant value; otherwise returns false.

**Warning:** This function is likely to give unexpected results. A variant value is only constructed by the :sip:ref:`~PyQt6.QtQml.QJSEngine` in a very limited number of cases. This used to be different before Qt 5.14, where :sip:ref:`~PyQt6.QtQml.QJSEngine.toScriptValue` would have created them for more types instead of corresponding ECMAScript types. You can get a valid :sip:ref:`~PyQt6.QtCore.QVariant` via :sip:ref:`~PyQt6.QtQml.QJSValue.toVariant` for many values for which ``isVariant`` returns false.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSValue.toVariant`.
