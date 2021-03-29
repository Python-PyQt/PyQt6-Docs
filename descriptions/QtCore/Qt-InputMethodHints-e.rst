.. sip:enum-description::
    :status: todo
    :realname: Qt::InputMethodHint
    :digest: 2947323d99c14a093e50c6f2478a68c2

Flags that alter the behavior:

Flags that restrict input (exclusive flags):

Masks:

**Note:** If several exclusive flags are OR-ed together, the resulting character set will consist of the union of the specified sets. For instance specifying ``ImhNumbersOnly`` and ``ImhUppercaseOnly`` would yield a set consisting of numbers and uppercase letters.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodHints`.
