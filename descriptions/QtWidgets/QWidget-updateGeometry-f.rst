.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ee778b799baf270189247ca8bd7e0d30

Notifies the layout system that this widget has changed and may need to change geometry.

Call this function if the :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` or :sip:ref:`~PyQt6.QtWidgets.QWidget.sizePolicy` have changed.

For explicitly hidden widgets,  is a no-op. The layout system will be notified as soon as the widget is shown.
