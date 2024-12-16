.. sip:method-description::
    :status: todo
    :pysig: 208a94b61d8ae7187580ae35039b6343
    :realsig: (QMdiArea::WindowOrder) const
    :digest: 08c137c2ae2b19659ade0baccfab35a1

Returns a list of all subwindows in the MDI area. If *order* is :sip:ref:`~PyQt6.QtWidgets.QMdiArea.WindowOrder.CreationOrder` (the default), the windows are sorted in the order in which they were inserted into the workspace. If *order* is :sip:ref:`~PyQt6.QtWidgets.QMdiArea.WindowOrder.StackingOrder`, the windows are listed in their stacking order, with the topmost window as the last item in the list. If *order* is :sip:ref:`~PyQt6.QtWidgets.QMdiArea.WindowOrder.ActivationHistoryOrder`, the windows are listed according to their recent activation history.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.WindowOrder.WindowOrder`.
