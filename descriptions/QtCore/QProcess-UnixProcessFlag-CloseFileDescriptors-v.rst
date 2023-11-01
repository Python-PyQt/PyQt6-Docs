.. sip:enum-member-description::
    :status: todo
    :value: 0x0010
    :digest: 3f898ae160571fcdc10a84be3f93c816

Close all file descriptors above the threshold defined by ``lowestFileDescriptorToClose``, preventing any currently open descriptor in the parent process from accidentally leaking to the child. The ``stdin``, ``stdout``, and ``stderr`` file descriptors are never closed.
