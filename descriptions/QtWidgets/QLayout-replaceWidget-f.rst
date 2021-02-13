.. sip:method-description::
    :status: todo
    :pysig: b40a7218e0a4f6f8752f696917ad67b0
    :realsig: (QWidget*,QWidget*,Qt::FindChildOptions)
    :digest: cb9a2f234a4ce34fe0008ed4a5b55678

Searches for widget *from* and replaces it with widget *to* if found. Returns the layout item that contains the widget *from* on success. Otherwise ``nullptr`` is returned. If *options* contains ``Qt::FindChildrenRecursively`` (the default), sub-layouts are searched for doing the replacement. Any other flag in *options* is ignored.

Notice that the returned item therefore might not belong to this layout, but to a sub-layout.

The returned layout item is no longer owned by the layout and should be either deleted or inserted to another layout. The widget *from* is no longer managed by the layout and may need to be deleted or hidden. The parent of widget *from* is left unchanged.

This function works for the built-in Qt layouts, but might not work for custom layouts.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout.indexOf`.
