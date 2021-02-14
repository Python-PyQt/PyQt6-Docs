.. sip:method-description::
    :status: todo
    :pysig: bed3adaca4b12a1f45c21d7871fa1f0f
    :realname: Qt3DRender::QComputeCommand::trigger
    :realsig: (int,int,int,int)
    :digest: ca949da54f756093db6795f120cecd2e

When the run type is set to Manual, calling trigger will make the compute command be executed for the next *frameCount* frames. Upon completion of the execution, the enabled property will be set to false. The size of the workgroup previously set will be overridden with *workGroupX*, *workGroupY*, *workGroupZ*.
