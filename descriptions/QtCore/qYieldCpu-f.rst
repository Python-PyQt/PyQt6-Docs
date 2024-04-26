.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 74191b4a1439acb9629bb2ef4a102b5d

Pauses the execution of the current thread for an unspecified time, using hardware instructions, without de-scheduling this thread. This function is meant to be used in high-throughput loops where the code expects another thread to modify an atomic variable. This is completely different from :sip:ref:`~PyQt6.QtCore.QThread.yieldCurrentThread`, which is an OS-level operation that may take the whole thread off the CPU and allow other threads (possibly belonging to other processes) to run.

So, instead of

::

    while (!condition)
        ;

one should write

::

    while (!condition)
        qYieldCpu();

This is useful both with and without hardware multithreading on the same core. In the case of hardware threads, it serves to prevent further speculative execution filling up the pipeline, which could starve the sibling thread of resources. Across cores and higher levels of separation, it allows the cache coherency protocol to allocate the cache line being modified and inspected to the logical processor whose result this code is expecting.

It is also recommended to loop around code that does not modify the global variable, to avoid contention in exclusively obtaining the memory location. Therefore, an atomic modification loop such as a spinlock acquisition should be:

::

    while (true) {
        while (!readOnlyCondition(atomic))
            qYieldCpu();
        if (modify(atomic))
            break;
    }

On x86 processors and on RISC-V processors with the ``Zihintpause`` extension, this will emit the ``PAUSE`` instruction, which is ignored on processors that don't support it; on ARMv7 or later ARM processors, it will emit the ``YIELD`` instruction.
