.. sip:class-description::
    :status: todo
    :brief: Updates on the QML parser state
    :digest: eeeec8966d6c90fda782aecdf9a7f556

The :sip:ref:`~PyQt6.QtQml.QQmlParserStatus` class provides updates on the QML parser state.

:sip:ref:`~PyQt6.QtQml.QQmlParserStatus` provides a mechanism for classes instantiated by a :sip:ref:`~PyQt6.QtQml.QQmlEngine` to receive notification at key points in their creation.

This class is often used for optimization purposes, as it allows you to defer an expensive operation until after all the properties have been set on an object. For example, QML's `Text <https://doc.qt.io/qt-6/qml-qtquick-text.html>`_ element uses the parser status to defer text layout until all of its properties have been set (we don't want to layout when the ``text`` is assigned, and then relayout when the ``font`` is assigned, and relayout again when the ``width`` is assigned, and so on).

Be aware that :sip:ref:`~PyQt6.QtQml.QQmlParserStatus` methods are only called when a class is instantiated by a :sip:ref:`~PyQt6.QtQml.QQmlEngine`. If you create the same class directly from C++, these methods will not be called automatically. To avoid this problem, it is recommended that you start deferring operations from :sip:ref:`~PyQt6.QtQml.QQmlParserStatus.classBegin` instead of from the initial creation of your class. This will still prevent multiple revaluations during initial binding assignment in QML, but will not defer operations invoked from C++.

To use :sip:ref:`~PyQt6.QtQml.QQmlParserStatus`, you must inherit both a :sip:ref:`~PyQt6.QtCore.QObject`-derived class and :sip:ref:`~PyQt6.QtQml.QQmlParserStatus`, and use the Q_INTERFACES() macro.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlparserstatus.py
    :lines: 54-64
