.. sip:enum-description::
    :status: todo
    :realname: Qt::InputMethodHint
    :digest: 0c273c89667da1779863f82e9e270a71

Flags that alter the behavior:

Flags that restrict input (exclusive flags):

Masks:

**Note:** If several exclusive flags are OR-ed together, the resulting character set will consist of the union of the specified sets. For instance specifying ``ImhNumbersOnly`` and ``ImhUppercaseOnly`` would yield a set consisting of numbers and uppercase letters.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodHints`.
