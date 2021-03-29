.. sip:method-description::
    :status: todo
    :pysig: e7d4b6e3f87ba9fe2928216c4f159b5b
    :realsig: (QEvent*)
    :digest: 284df1e1bb598de505c17b3732d52ad1

This event handler can be reimplemented to handle state changes.

The state being changed in this event can be retrieved through *event*.

Change events include: :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActivationChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.EnabledChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.FontChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.StyleChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.PaletteChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ParentChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.LayoutDirectionChange`, and :sip:ref:`~PyQt6.QtCore.QEvent.Type.ContentsRectChange`.
