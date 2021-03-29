.. sip:signal-description::
    :status: todo
    :pysig: 4f8f93e499a4090f930ac51556f2b328
    :realsig: (QMdiSubWindow*)
    :digest: b47edbcf110b85fb482eac49868bceaf

:sip:ref:`~PyQt6.QtWidgets.QMdiArea` emits this signal after *window* has been activated. When *window* is ``nullptr``, :sip:ref:`~PyQt6.QtWidgets.QMdiArea` has just deactivated its last active window, and there are no active windows on the workspace.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activeSubWindow`.
