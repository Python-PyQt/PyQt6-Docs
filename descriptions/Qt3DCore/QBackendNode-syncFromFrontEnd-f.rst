.. sip:method-description::
    :status: todo
    :pysig: fdb9d6f59af056f8ea85c69aef32de86
    :realname: Qt3DCore::QBackendNode::syncFromFrontEnd
    :realsig: (const Qt3DCore::QNode*,bool)
    :digest: b4293024bb6c075511978f1b5571e19b

QBackendNode::syncFromFrontEnd *frontEnd* *firstTime*

This is called by the aspect when a *frontEnd* node needs to synchronize it's changes with the backend (normally due to property changes).

*firstTime* will be true if the backend node was just created
