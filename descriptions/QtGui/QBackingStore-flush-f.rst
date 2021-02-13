.. sip:method-description::
    :status: todo
    :pysig: 23b06e7fb83cd7d0c5bfb8ab81b7c5a1
    :realsig: (const QRegion&,QWindow*,const QPoint&)
    :digest: 812f4ff12140c7695446a92e2ed830a9

Flushes the given *region* from the specified *window* onto the screen.

The *window* must either be the top level window represented by this backingstore, or a non-transient child of that window. Passing ``nullptr`` falls back to using the backingstore's top level window.

If the *window* is a child window, the *region* should be in child window coordinates, and the *offset* should be the child window's offset in relation to the backingstore's top level window.

You should call this function after ending painting with :sip:ref:`~PyQt6.QtGui.QBackingStore.endPaint`.
