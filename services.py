from enum import Enum

from structures import RpcService

class ServiceRole:
    DOMAIN_CONTROLLER = RpcService(
        'role:adds',
        ['Roles', 'ADDS'],
        'Active Directory Domain Services (AD DS)',
        ''
    )

    CERTIFICATE_SERVICES = RpcService(
        'role:adcs',
        ['Roles', 'ADCS'],
        'Active Directory Certificate Services (AD CS)',
        ''
    )

    ADFS = RpcService(
        'role:adfs',
        ['Roles', 'ADFS'],
        'Active Directory Federation Services (AD FS)',
        ''
    )

    LDS = RpcService(
        'role:adlds',
        ['Roles', 'ADLDS'],
        'Active Directory Lightwight Directory Services (AD LDS)',
        ''
    )

    DHCP = RpcService(
        'role:dhcp',
        ['Roles', 'DHCP'],
        'DHCP Server',
        ''
    )

    DNS = RpcService(
        'role:dns',
        ['Roles', 'DNS'],
        'DNS Server',
        ''
    )

    FAX = RpcService(
        'role:fax',
        ['Roles', 'Fax'],
        'Fax Server',
        ''
    )

    FILE_SERVER = RpcService(
        'role:fileserver',
        ['Roles', 'FileServer'],
        'File Server',
        ''
    )

    DFS_NAMESPACES = RpcService(
        'role:dfsnamespaces',
        ['Roles', 'DFSNamespaces'],
        'DFS (Distributed Filesystem) Namespaces',
        ''
    )

    DFS_REPLICATION = RpcService(
        'role:dfsreplication',
        ['Roles', 'DFSReplication'],
        'DFS (Distributed Filesystem) Replication',
        ''
    )

    FSRM = RpcService(
        'role:fsrm',
        ['Roles', 'FSRM'],
        'File Server Resource Manager',
        ''
    )

    FILE_SERVER_VSS_AGENT = RpcService(
        'role:vssagent',
        ['Roles', 'FileServerVSSAgent'],
        'File Server VSS Agent',
        ''
    )

    ISCSI_TARGET_SERVER = RpcService(
        'role:iscsitarget',
        ['Roles', 'iSCSITarget'],
        'iSCSI Target Server',
        ''
    )

    ISCSI_TARGET_STORAGE_PROVIDER = RpcService(
        'role:iscsitargetstorageprovider',
        ['Roles', 'iSCSITargetStorageProvider'],
        'iSCSI Target Storage Provider (VDS and VSS)',
        ''
    )

    NFS_SERVER = RpcService(
        'role:nfsserver',
        ['Roles', 'NFSServer'],
        'Server for NFS',
        ''
    )

    PRINTING = RpcService(
        'role:printing',
        ['Roles', 'Printing'],
        'Print & Document Services',
        ''
    )

    NPS = RpcService(
        'role:nps',
        ['Roles', 'NPS'],
        'Network Policy Server',
        ''
    )

    WEB_SERVER = RpcService(
        'role:webserver',
        ['Roles', 'WebServer'],
        'Web Server (IIS)',
        ''
    )

    KMS = RpcService(
        'role:volumeactivation',
        ['Roles', 'VolumeActivation'],
        'Volume Activation Services',
        ''
    )

    WDS = RpcService(
        'role:deploymentservices',
        ['Roles', 'Deployment Services'],
        'Windows Deployment Services',
        ''
    )

    WSUS = RpcService(
        'role:wsus',
        ['Roles', 'WSUS'],
        'Windows Server Update Services',
        ''
    )


class ServiceFeature:
    FAILOVER_CLUSTERING = RpcService(
        'feature:failovercluster',
        ['Features', 'FailoverClustering'],
        'Failover Clustering',
        ''
    )

    # TODO: split
    MSMQ = RpcService(
        'feature:msmq',
        ['Features', 'MSMQ'],
        'Message Queuing',
        ''
    )

    TERMINAL_SERVICES = RpcService(
        'feature:terminalservices',
        ['Features', 'Terminal Services'],
        'Terminal Services',
        ''
    )


class ServiceBuiltIn:
    DISK_MANAGEMENT = RpcService(
        'builtin:diskmanagement',
        ['BuiltIn', 'DiskManagement'],
        'Disk Management',
        ''
    )

    EVENT_LOG = RpcService(
        'builtin:eventlog',
        ['BuiltIn', 'EventLog'],
        'Event Log',
        ''
    )

    FIREWALL = RpcService(
        'builtin:firewall',
        ['BuiltIn', 'Firewall'],
        'Windows Firewall',
        ''
    )

    PERFORMANCE_COUNTERS = RpcService(
        'builtin:performancecounters',
        ['BuiltIn', 'PerformanceCounters'],
        'Performance Counters',
        ''
    )

    REMOTE_ASSISTANCE = RpcService(
        'builtin:remoteassistance',
        ['BuiltIn', 'RemoteAssistance'],
        'Remote Assistance',
        ''
    )

    WINS = RpcService(
        'builtin:wins',
        ['BuiltIn', 'WINS'],
        'WINS',
        ''
    )

    REMOTE_REGISTRY = RpcService(
        'builtin:remoteregistry',
        ['BuiltIn', 'RemoteRegistry'],
        'Remote Registry',
        ''
    )

    REMOTE_SHUTDOWN = RpcService(
        'builtin:remoteshutdown',
        ['BuiltIn', 'RemoteShutdown'],
        'Remote Shutdown',
        ''
    )

    SERVICES = RpcService(
        'builtin:services',
        ['BuiltIn', 'services'],
        'Services',
        ''
    )

    TASK_SCHEDULER = RpcService(
        'builtin:taskscheduler',
        ['BuiltIn', 'TaskScheduler'],
        'Task Scheduler',
        ''
    )

    VIRTUAL_SMARTCARD = RpcService(
        'builtin:remoteshutdown',
        ['BuiltIn', 'RemoteShutdown'],
        'Remote Shutdown',
        ''
    )

    TELNET = RpcService(
        'builtin:telnet',
        ['BuiltIn', 'Telnet'],
        'Telnet',
        ''
    )

    TIME = RpcService(
        'builtin:time',
        ['BuiltIn', 'time'],
        'Windows Time Service',
        ''
    )

    WMI = RpcService(
        'builtin:wmi',
        ['BuiltIn', 'WMI'],
        'Windows Management Instrumentation',
        ''
    )

class ServiceOther:
    MICROSOFT_EXCHANGE = RpcService(
        'other:exchange',
        ['Other', 'MicrosoftExchange'],
        'Microsoft Exchange Server',
        ''
    )

ALL_SERVICES = {
    ServiceRole.__dict__[k].id: ServiceRole.__dict__[k]
    for k in filter(lambda k: '__' not in k, vars(ServiceRole).keys())
} | {
    ServiceFeature.__dict__[k].id: ServiceFeature.__dict__[k]
    for k in filter(lambda k: '__' not in k, vars(ServiceFeature).keys())
} | {
    ServiceBuiltIn.__dict__[k].id: ServiceBuiltIn.__dict__[k]
    for k in filter(lambda k: '__' not in k, vars(ServiceBuiltIn).keys())
} | {
    ServiceOther.__dict__[k].id: ServiceOther.__dict__[k]
    for k in filter(lambda k: '__' not in k, vars(ServiceOther).keys())
}