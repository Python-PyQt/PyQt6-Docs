.. sip:method-description::
    :status: todo
    :pysig: a16338befe618e5ebb6497a2cf126c0b
    :realsig: (const QObject*)
    :digest: 30161e154c199c8ad9a829ee01f2f1b3

Returns the :sip:ref:`~PyQt6.QtQml.QJSEngine` associated with *object*, if any.

This function is useful if you have exposed a :sip:ref:`~PyQt6.QtCore.QObject` to the JavaScript environment and later in your program would like to regain access. It does not require you to keep the wrapper around that was returned from :sip:ref:`~PyQt6.QtQml.QJSEngine.newQObject`.
