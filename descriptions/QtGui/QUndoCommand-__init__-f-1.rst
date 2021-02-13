.. sip:method-description::
    :status: todo
    :pysig: e55abc7846a61fde3337677f0d68ebfc
    :realsig: (const QString&,QUndoCommand*)
    :digest: 899aa9dec43997e7e14dee21efb1ca6c

Constructs a :sip:ref:`~PyQt6.QtGui.QUndoCommand` object with the given *parent* and *text*.

If *parent* is not ``nullptr``, this command is appended to parent's child list. The parent command then owns this command and will delete it in its destructor.

.. seealso:: ~QUndoCommand().
