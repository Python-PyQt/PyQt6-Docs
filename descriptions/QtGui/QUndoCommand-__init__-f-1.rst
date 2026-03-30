.. sip:method-description::
    :status: todo
    :pysig: 8bbfd2d7f194a798f87dd38615fc9dbb
    :realsig: (const QString&, QUndoCommand*)
    :digest: 899aa9dec43997e7e14dee21efb1ca6c

Constructs a :sip:ref:`~PyQt6.QtGui.QUndoCommand` object with the given *parent* and *text*.

If *parent* is not ``nullptr``, this command is appended to parent's child list. The parent command then owns this command and will delete it in its destructor.

.. seealso:: ~QUndoCommand().
