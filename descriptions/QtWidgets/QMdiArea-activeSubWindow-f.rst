.. sip:method-description::
    :status: todo
    :pysig: 4f8f93e499a4090f930ac51556f2b328
    :realsig: () const
    :digest: 979911018173de85d1e9043a4370734d

Returns a pointer to the current active subwindow. If no window is currently active, ``nullptr`` is returned.

Subwindows are treated as top-level windows with respect to window state, i.e., if a widget outside the MDI area is the active window, no subwindow will be active. Note that if a widget in the window in which the MDI area lives gains focus, the window will be activated.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.setActiveSubWindow`, :sip:ref:`~PyQt6.QtCore.Qt.WindowStates`.
