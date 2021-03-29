.. sip:method-description::
    :status: todo
    :pysig: 773223d7a97bc727764204f49d6f1d58
    :realsig: (const QRect&)
    :digest: c9674c822bf8392610b49fd0600b702d

For :sip:ref:`~PyQt6.QtWidgets.QCompleter.CompletionMode.PopupCompletion` and QCompletion::UnfilteredPopupCompletion modes, calling this function displays the popup displaying the current completions. By default, if *rect* is not specified, the popup is displayed on the bottom of the :sip:ref:`~PyQt6.QtWidgets.QCompleter.widget`. If *rect* is specified the popup is displayed on the left edge of the rectangle.

For :sip:ref:`~PyQt6.QtWidgets.QCompleter.CompletionMode.InlineCompletion` mode, the :sip:ref:`~PyQt6.QtWidgets.QCompleter.highlighted` signal is fired with the current completion.
