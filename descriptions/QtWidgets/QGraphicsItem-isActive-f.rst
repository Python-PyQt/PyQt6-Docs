.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 3b04d64968678863f233c73a61962e6e

Returns ``true`` if this item is active; otherwise returns ``false``.

An item can only be active if the scene is active. An item is active if it is, or is a descendent of, an active panel. Items in non-active panels are not active.

Items that are not part of a panel follow scene activation when the scene has no active panel.

Only active items can gain input focus.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.isActive`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.activePanel`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.panel`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isPanel`.
