.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 9ed98ca04368a2f9fc05b4071f59405a

This virtual handler is called when the scroll bars are moved by *dx*, *dy*, and consequently the viewport's contents should be scrolled accordingly.

The default implementation simply calls update() on the entire :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewport`, subclasses can reimplement this handler for optimization purposes, or - like :sip:ref:`~PyQt6.QtWidgets.QScrollArea` - to move a contents widget. The parameters *dx* and *dy* are there for convenience, so that the class knows how much should be scrolled (useful e.g. when doing pixel-shifts). You may just as well ignore these values and scroll directly to the position the scroll bars indicate.

Calling this function in order to scroll programmatically is an error, use the scroll bars instead (e.g. by calling QScrollBar::setValue() directly).
