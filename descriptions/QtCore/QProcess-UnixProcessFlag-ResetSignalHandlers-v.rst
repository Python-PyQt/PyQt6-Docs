.. sip:enum-member-description::
    :status: todo
    :value: 0x0001
    :digest: e42606b4e945218d4e735c6cab82f4c4

Resets all Unix signal handlers back to their default state (that is, pass ``SIG_DFL`` to ``signal(2)``). This flag is useful to ensure any ignored (``SIG_IGN``) signal does not affect the child's behavior.
