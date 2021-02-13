.. sip:method-description::
    :status: todo
    :pysig: 0657463e9793567e3b29a2e27a019172
    :realsig: ()
    :digest: ed8eee74c47c0f5cd4ca6f631b0fac80

Returns the position of the cursor (hot spot) of the primary screen in global screen coordinates.

You can call QWidget::mapFromGlobal() to translate it to widget coordinates.

**Note:** The position is queried from the windowing system. If mouse events are generated via other means (e.g., via QWindowSystemInterface in a unit test), those fake mouse moves will not be reflected in the returned value.

**Note:** On platforms where there is no windowing system or cursors are not available, the returned position is based on the mouse move events generated via QWindowSystemInterface.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QCursor.setPos`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.primaryScreen`.
