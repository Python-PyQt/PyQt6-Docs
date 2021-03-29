.. sip:method-description::
    :status: todo
    :pysig: 747489948cb811f4d1da5067faaf819f
    :realsig: (Qt::InputMethodQueries)
    :digest: 70c9cc0417da5a826c51eec315eec076

Called by the input item to inform the platform input methods when there has been state changes in editor's input method query attributes. When calling the function *queries* parameter has to be used to tell what has changes, which input method can use to make queries for attributes it's interested with :sip:ref:`~PyQt6.QtGui.QInputMethodQueryEvent`.

In particular calling update whenever the cursor position changes is important as that often causes other query attributes like surrounding text and text selection to change as well. The attributes that often change together with cursor position have been grouped in :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQueries.ImQueryInput` value for convenience.
