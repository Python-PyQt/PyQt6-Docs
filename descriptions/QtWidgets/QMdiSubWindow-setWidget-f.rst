.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: b0866eeab4f128166f87d71b099d59ff

Sets *widget* as the internal widget of this subwindow. The internal widget is displayed in the center of the subwindow beneath the title bar.

:sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` takes temporary ownership of *widget*; you do not have to delete it. Any existing internal widget will be removed and reparented to the root window.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.widget`.
