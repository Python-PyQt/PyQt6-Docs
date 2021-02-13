.. sip:method-description::
    :status: todo
    :pysig: cd950c891859c6272700ee58ab9a65a9
    :realsig: (QUndoCommand*)
    :digest: 81ec72d3f61945392875004a55f5bef9

Constructs a :sip:ref:`~PyQt6.QtGui.QUndoCommand` object with parent *parent*.

If *parent* is not ``nullptr``, this command is appended to parent's child list. The parent command then owns this command and will delete it in its destructor.

.. seealso:: ~QUndoCommand().
