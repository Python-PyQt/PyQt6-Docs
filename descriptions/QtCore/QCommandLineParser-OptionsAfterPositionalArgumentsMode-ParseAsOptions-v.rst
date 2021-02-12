.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: 169c98cf7d7a411881d5a93be88b6712

``application argument --opt -t`` is interpreted as setting the options ``opt`` and ``t``, just like ``application --opt -t argument`` would do. This is the default parsing mode. In order to specify that ``--opt`` and ``-t`` are positional arguments instead, the user can use ``--``, as in ``application argument -- --opt -t``.
