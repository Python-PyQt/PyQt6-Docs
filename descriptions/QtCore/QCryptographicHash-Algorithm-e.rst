.. sip:enum-description::
    :status: todo
    :digest: 55b4af94cb3a38b51c3754fec2a4a158

**Note:** In Qt versions before 5.9, when asked to generate a SHA3 hash sum, :sip:ref:`~PyQt6.QtCore.QCryptographicHash` actually calculated Keccak. If you need compatibility with SHA-3 hashes produced by those versions of Qt, use the ``Keccak_`` enumerators. Alternatively, if source compatibility is required, define the macro ``QT_SHA3_KECCAK_COMPAT``.
