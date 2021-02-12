.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 063800ea3a8d500c24c4c6ddcb175c61

``application argument --opt`` is interpreted as having two positional arguments, ``argument`` and ``--opt``. This mode is useful for executables that aim to launch other executables (e.g. wrappers, debugging tools, etc.) or that support internal commands followed by options for the command. ``argument`` is the name of the command, and all options occurring after it can be collected and parsed by another command line parser, possibly in another executable.
