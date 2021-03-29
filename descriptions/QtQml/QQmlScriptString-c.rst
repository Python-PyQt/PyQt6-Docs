.. sip:class-description::
    :status: todo
    :brief: Encapsulates a script and its context
    :digest: 873f38310757423324f1f51ddfc773ed

The :sip:ref:`~PyQt6.QtQml.QQmlScriptString` class encapsulates a script and its context.

:sip:ref:`~PyQt6.QtQml.QQmlScriptString` is used to create :sip:ref:`~PyQt6.QtCore.QObject` properties that accept a script "assignment" from QML.

Normally, the following QML would result in a binding being established for the ``script`` property; i.e. ``script`` would be assigned the value obtained from running ``myObj.value = Math.max(myValue, 100)``

If instead the property had a type of :sip:ref:`~PyQt6.QtQml.QQmlScriptString`, the script itself -- *myObj.value = Math.max(myValue, 100)* -- would be passed to the ``script`` property and the class could choose how to handle it. Typically, the class will evaluate the script at some later time using a :sip:ref:`~PyQt6.QtQml.QQmlExpression`.

::

    QQmlExpression expr(scriptString);
    expr.evaluate();

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlExpression`.
