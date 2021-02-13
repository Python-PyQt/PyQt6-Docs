.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 86b90d9819c5b80b409b917288bb320f

Call this function to close the widget.

Returns ``true`` if the widget was closed; otherwise returns ``false``. This slot will first send a :sip:ref:`~PyQt6.QtGui.QCloseEvent` to the widget, which may or may not accept the event. If the event was ignored, nothing happens. If the event was accepted, it will hide() the widget.

If the widget has the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_DeleteOnClose` attribute set it will be deleted.
