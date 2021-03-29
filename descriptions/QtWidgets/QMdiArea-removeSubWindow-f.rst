.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 69794cc50e6ef2a794418ff6a6c7667f

Removes *widget* from the MDI area. The *widget* must be either a :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` or a widget that is the internal widget of a subwindow. Note *widget* is never actually deleted by :sip:ref:`~PyQt6.QtWidgets.QMdiArea`. If a :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` is passed in, its parent is set to ``nullptr`` and it is removed; but if an internal widget is passed in, the child widget is set to ``nullptr`` and the :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` is *not* removed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.addSubWindow`.
