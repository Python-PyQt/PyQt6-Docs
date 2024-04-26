.. sip:enum-member-description::
    :status: todo
    :value: 0x0080
    :digest: e6eb2fcf6daac518e7acf6605ed9d146

Requests that the process disconnect from its controlling terminal, if it has one. If it has none, nothing happens. Processes still connected to a controlling terminal may get a Hang Up (``SIGHUP``) signal if the terminal closes, or one of the other terminal-control signals (``SIGTSTP``, ``SIGTTIN``, ``SIGTTOU``). Note that on some operating systems, a process may only disconnect from the controlling terminal if it is the session leader, meaning the ``CreateNewSession`` flag may be required. Like it, this is one of the steps to daemonize a process.
