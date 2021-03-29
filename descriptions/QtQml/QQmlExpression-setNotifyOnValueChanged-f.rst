.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 816e6f5d4caab21b206916bb3c4ff814

Sets whether the :sip:ref:`~PyQt6.QtQml.QQmlExpression.valueChanged` signal is emitted when the expression's evaluated value changes.

If *notifyOnChange* is true, the :sip:ref:`~PyQt6.QtQml.QQmlExpression` will monitor properties involved in the expression's evaluation, and emit :sip:ref:`~PyQt6.QtQml.QQmlExpression.valueChanged` if they have changed. This allows an application to ensure that any value associated with the result of the expression remains up to date.

If *notifyOnChange* is false (default), the :sip:ref:`~PyQt6.QtQml.QQmlExpression` will not montitor properties involved in the expression's evaluation, and :sip:ref:`~PyQt6.QtQml.QQmlExpression.valueChanged` will never be emitted. This is more efficient if an application wants a "one off" evaluation of the expression.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlExpression.notifyOnValueChanged`.
