.. sip:method-description::
    :status: todo
    :pysig: e7d4b6e3f87ba9fe2928216c4f159b5b
    :realsig: (QEvent*)
    :digest: 9585c939f47ff5c015994e42b3b7b101

This event handler can be reimplemented to handle state changes.

The state being changed in this event can be retrieved through the *event* supplied.

Change events include: :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolBarChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActivationChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.EnabledChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.FontChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.StyleChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.PaletteChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.WindowTitleChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.IconTextChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ModifiedChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.MouseTrackingChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ParentChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.WindowStateChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.LanguageChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.LocaleChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.LayoutDirectionChange`, :sip:ref:`~PyQt6.QtCore.QEvent.Type.ReadOnlyChange`.
