.. sip:enum-member-description::
    :status: todo
    :value: 26
    :digest: 185a7e93defff34962c07957ca26fb35

When making a context current using `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_, do not check that the QObject thread affinity of the `QOpenGLContext <https://doc.qt.io/qt-6/gui-changes-qt6.html#qopenglcontext>`_ object is the same thread calling :sip:ref:`~PyQt6.QtGui.QOpenGLContext.makeCurrent`. This value was added in Qt 5.8.
