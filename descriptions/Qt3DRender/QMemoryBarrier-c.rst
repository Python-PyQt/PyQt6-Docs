.. sip:class-description::
    :status: todo
    :brief: Class to emplace a memory barrier
    :realname: Qt3DRender::QMemoryBarrier
    :digest: 1449a4209da931cab2af00ace7cdf1b9

Class to emplace a memory barrier.

A :sip:ref:`~PyQt6.Qt3DRender.QMemoryBarrier` FrameGraph node is used to emplace a specific memory barrier at a specific time of the rendering. This is required to properly synchronize drawing and compute commands on the GPU.

The barrier defines the ordering of memory operations issued by a prior command. This means that if command1 is manipulating a buffer that is to be used as a vertex attribute buffer in a following command2, then the memory barrier should be placed after command1 and setting the appropriate barrier type for vertex attribute buffer.

When a :sip:ref:`~PyQt6.Qt3DRender.QMemoryBarrier` node is found in a FrameGraph branch, the barrier will be enforced prior to any draw or compute command even if these are defined deeper in the branch.

For OpenGL rendering, this page gives more info about the `Memory Model <https://www.opengl.org/wiki/Memory_Model>`_
