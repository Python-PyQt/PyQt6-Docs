.. sip:method-description::
    :status: todo
    :pysig: d040f8c82bf0336ad39533fdcb9e99b9
    :realsig: (bool,bool)
    :digest: 6ab6c78093ceffa87a0c442379a1d428

Frees up window system resources. Destroys the widget window if *destroyWindow* is true.

destroy() calls itself recursively for all the child widgets, passing *destroySubWindows* for the *destroyWindow* parameter. To have more control over destruction of subwidgets, destroy subwidgets selectively first.

This function is usually called from the :sip:ref:`~PyQt6.QtWidgets.QWidget` destructor.
