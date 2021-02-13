.. sip:method-description::
    :status: todo
    :pysig: 0bee5ee99a425921db962be70be70688
    :realsig: (QMenu*)
    :digest: bc2fbcd9e1d08135e3529e479d6145e0

Sets *systemMenu* as the current system menu for this subwindow.

By default, each :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` has a standard system menu.

QActions for the system menu created by :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` will automatically be updated depending on the current window state; e.g., the minimize action will be disabled after the window is minimized.

QActions added by the user are not updated by :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow`.

:sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` takes ownership of *systemMenu*; you do not have to delete it. Any existing menus will be deleted.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.systemMenu`, :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.showSystemMenu`.
