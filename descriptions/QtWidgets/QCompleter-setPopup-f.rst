.. sip:method-description::
    :status: todo
    :pysig: dd9861cc8684c775152f94a62ebafc36
    :realsig: (QAbstractItemView*)
    :digest: 62de4c8617e51554e629ea812bb5c8c5

Sets the popup used to display completions to *popup*. :sip:ref:`~PyQt6.QtWidgets.QCompleter` takes ownership of the view.

A :sip:ref:`~PyQt6.QtWidgets.QListView` is automatically created when the :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionMode` is set to :sip:ref:`~PyQt6.QtWidgets.QCompleter.CompletionMode.PopupCompletion` or :sip:ref:`~PyQt6.QtWidgets.QCompleter.CompletionMode.UnfilteredPopupCompletion`. The default popup displays the :sip:ref:`~PyQt6.QtWidgets.QCompleter.completionColumn`.

Ensure that this function is called before the view settings are modified. This is required since view's properties may require that a model has been set on the view (for example, hiding columns in the view requires a model to be set on the view).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QCompleter.popup`.
