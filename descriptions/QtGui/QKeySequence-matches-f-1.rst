.. sip:method-description::
    :status: todo
    :pysig: 0ec371bfc74761fed09ca4b8bc829555
    :realsig: (const QKeySequence&) const
    :digest: b81c3a7109cbb12d8196a796423c0f85

Matches the sequence with *seq*. Returns :sip:ref:`~PyQt6.QtGui.QKeySequence.SequenceMatch.ExactMatch` if successful, :sip:ref:`~PyQt6.QtGui.QKeySequence.SequenceMatch.PartialMatch` if *seq* matches incompletely, and :sip:ref:`~PyQt6.QtGui.QKeySequence.SequenceMatch.NoMatch` if the sequences have nothing in common. Returns :sip:ref:`~PyQt6.QtGui.QKeySequence.SequenceMatch.NoMatch` if *seq* is shorter.
