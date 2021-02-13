.. sip:method-description::
    :status: todo
    :pysig: a224e19238458489966f90a03a7a4379
    :realsig: (QMarginsF)
    :digest: c5025dcca907aa4823756b3cb944009e

Sets the widget's contents margins to *margins*.

Contents margins are used by the assigned layout to define the placement of subwidgets and layouts. Margins are particularly useful for widgets that constrain subwidgets to only a section of its own geometry. For example, a group box with a layout will place subwidgets inside its frame, but below the title.

Changing a widget's contents margins will always trigger an update(), and any assigned layout will be activated automatically. The widget will then receive a :sip:ref:`~PyQt6.QtCore.QEvent.Type.ContentsRectChange` event.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.getContentsMargins`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setGeometry`.
