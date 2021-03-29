.. sip:method-description::
    :status: todo
    :pysig: d040f8c82bf0336ad39533fdcb9e99b9
    :realsig: (bool,bool)
    :digest: b0f97bb90b41bc9e457a83783a41e6f6

Frees up window system resources. Destroys the widget window if *destroyWindow* is true.

calls itself recursively for all the child widgets, passing *destroySubWindows* for the *destroyWindow* parameter. To have more control over destruction of subwidgets, destroy subwidgets selectively first.

This function is usually called from the `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ destructor.
