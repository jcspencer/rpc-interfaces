from structures import *
from services import *


INTERFACES = {
    "EPM": RpcInterfaceDefinition(
        id="MS-EPM",
        metadata=RpcInterfaceMetadata(
            name="Endpoint Mapper Protocol",
            description=""
        ),
        profiles=[
            # TODO
        ],
        uuids=[
            RpcUuid(uuid="e1af8308-5d1f-11c9-91a4-08002b14a0fa")
        ],
        named_pipes=[]
    ),

    "MC-CCFG": RpcInterfaceDefinition(
        id="MC-CCFG",
        metadata=RpcInterfaceMetadata(
            name="Server Cluster: Configuration (ClusCfg) Protocol",
            description=(
                "The Server Cluster: Configuration (ClusCfg) Protocol enables users to restore "
                "a node that is no longer a configured member of a failover cluster back to its "
                "pre-cluster installation state."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-ccfg/9996b3e3-2834-46ce-9883-dcf52f017981",
        ),
        profiles=[
            RpcInterfaceProfile(ServiceFeature.FAILOVER_CLUSTERING, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        uuids=[
            RpcUuid(uuid="52C80B95-C1AD-4240-8D89-72E9FA84025E", name="IClusCfgAsyncEvictCleanup")
        ],
        named_pipes=[]
    ),

    "MC-IISA": RpcInterfaceDefinition(
        id="MC-IISA",
        metadata=RpcInterfaceMetadata(
            name="Internet Information Services (IIS) Application Host COM Protocol",
            description=(
                "The Internet Information Services (IIS) Application Host COM Protocol "
                "provides read/write access to administrative configuration data that "
                "is located on a remote server."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-iisa/488de90f-9710-45fb-b71a-6938733fafb6"
        ),
        profiles=[
            RpcInterfaceProfile(ServiceRole.WEB_SERVER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        uuids=[
            RpcUuid(uuid="FA7660F6-7B3F-4237-A8BF-ED0AD0DCBBD9", name="IAppHostWritableAdminManager"),
            RpcUuid(uuid="450386DB-7409-4667-935E-384DBBEE2A9E", name="IAppHostPropertySchema"),
            RpcUuid(uuid="832A32F7-B3EA-4B8C-B260-9A2923001184", name="IAppHostConfigLocationCollection"),
            RpcUuid(uuid="2D9915FB-9D42-4328-B782-1B46819FAB9E", name="IAppHostMethodSchema"),
            RpcUuid(uuid="0DD8A158-EBE6-4008-A1D9-B7ECC8F1104B", name="IAppHostSectionGroup"),
            RpcUuid(uuid="0716CAF8-7D05-4A46-8099-77594BE91394", name="IAppHostConstantValue"),
            RpcUuid(uuid="B80F3C42-60E0-4AE0-9007-F52852D3DBED", name="IAppHostMethodInstance"),
            RpcUuid(uuid="0344CDDA-151E-4CBF-82DA-66AE61E97754", name="IAppHostElementSchemaCollection"),
            RpcUuid(uuid="8BED2C68-A5FB-4B28-8581-A0DC5267419F", name="IAppHostPropertySchemaCollection"),
            RpcUuid(uuid="7883CA1C-1112-4447-84C3-52FBEB38069D", name="IAppHostMethod"),
            RpcUuid(uuid="09829352-87C2-418D-8D79-4133969A489D", name="IAppHostChangeHandler"),
            RpcUuid(uuid="5B5A68E6-8B9F-45E1-8199-A95FFCCDFFFF", name="IAppHostConstantValueCollection"),
            RpcUuid(uuid="9BE77978-73ED-4A9A-87FD-13F09FEC1B13", name="IAppHostAdminManager"),
            RpcUuid(uuid="ED35F7A1-5024-4E7B-A44D-07DDAF4B524D", name="IAppHostProperty"),
            RpcUuid(uuid="4DFA1DF3-8900-4BC7-BBB5-D1A458C52410", name="IAppHostConfigException"),
            RpcUuid(uuid="370AF178-7758-4DAD-8146-7391F6E18585", name="IAppHostConfigLocation"),
            RpcUuid(uuid="C8550BFF-5281-4B1E-AC34-99B6FA38464D", name="IAppHostElementCollection"),
            RpcUuid(uuid="08A90F5F-0702-48D6-B45F-02A9885A9768", name="IAppHostChildElementCollection"),
            RpcUuid(uuid="8F6D760F-F0CB-4D69-B5F6-848B33E9BDC6", name="IAppHostConfigManager"),
            RpcUuid(uuid="E7927575-5CC3-403B-822E-328A6B904BEE", name="IAppHostPathMapper"),
            RpcUuid(uuid="DE095DB1-5368-4D11-81F6-EFEF619B7BCF", name="IAppHostCollectionSchema"),
            RpcUuid(uuid="64FF8CCC-B287-4DAE-B08A-A72CBF45F453", name="IAppHostElement"),
            RpcUuid(uuid="EAFE4895-A929-41EA-B14D-613E23F62B71", name="IAppHostPropertyException"),
            RpcUuid(uuid="EF13D885-642C-4709-99EC-B89561C6BC69", name="IAppHostElementSchema"),
            RpcUuid(uuid="0191775E-BCFF-445A-B4F4-3BDDA54E2816", name="IAppHostPropertyCollection"),
            RpcUuid(uuid="31A83EA0-C0E4-4A2C-8A01-353CC2A4C60A", name="IAppHostMappingExtension"),
            RpcUuid(uuid="D6C7CD8F-BB8D-4F96-B591-D3A5F1320269", name="IAppHostMethodCollection"),
            RpcUuid(uuid="ADA4E6FB-E025-401E-A5D0-C3134A281F07", name="IAppHostConfigFile"),
            RpcUuid(uuid="B7D381EE-8860-47A1-8AF4-1F33B2B1F325", name="IAppHostSectionDefinitionCollection"),
            RpcUuid(uuid="C5C04795-321C-4014-8FD6-D44658799393", name="IAppHostSectionDefinition"),
        ],
        named_pipes=[]
    ),

    "MC-MQAC": RpcInterfaceDefinition(
        id="MC-MQAC",
        metadata=RpcInterfaceMetadata(
            name="Message Queuing (MSMQ): ActiveX Client Protocol",
            description=(
                "The Message Queuing (MSMQ): ActiveX Client Protocol is a collection "
                "of Distributed Component Object Model (DCOM) interfaces that "
                "expose message queuing functionality for use by client applications."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-mqac/5ed096a9-b641-4a5a-b749-7e6937d20f4d"
        ),
        profiles=[
            RpcInterfaceProfile(ServiceFeature.MSMQ, RpcProfileType.CORE)
        ],
        uuids=[
            # TODO: come on - seriously?
            RpcUuid("EBA96B22-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("12A30900-7300-11D2-B0E6-00E02C074F6B"),
            RpcUuid("EBA96B24-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("2CE0C5B0-6E67-11D2-B0E6-00E02C074F6B"),
            RpcUuid("EBA96B0E-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("B196B285-BAB4-101A-B69C-00AA00341D07"),
            RpcUuid("39CE96FE-F4C5-4484-A143-4C2D5D324229"),
            RpcUuid("D7D6E07F-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("EBA96B1A-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B18-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B23-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B14-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("FD174A80-89CF-11D2-B0F2-00E02C074F6B"),
            RpcUuid("F72B9031-2F0C-43E8-924E-E6052CDC493F"),
            RpcUuid("D7D6E072-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("D7D6E075-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("0188401C-247A-4FED-99C6-BF14119D7055"),
            RpcUuid("EBA96B15-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E07C-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("BE5F0241-E489-4957-8CC4-A452FCF3E23E"),
            RpcUuid("EBA96B1C-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E077-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("D7D6E078-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("B196B284-BAB4-101A-B69C-00AA00341D07"),
            RpcUuid("D7D6E073-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("D7D6E07D-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("EBA96B1B-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E079-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("D7D6E084-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("EBA96B1F-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("33B6D07E-F27D-42FA-B2D7-BF82E11E9374"),
            RpcUuid("D7D6E07A-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("0188AC2F-ECB3-4173-9779-635CA2039C72"),
            RpcUuid("D7D6E085-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("EF0574E0-06D8-11D3-B100-00E02C074F6B"),
            RpcUuid("D7D6E086-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("B196B286-BAB4-101A-B69C-00AA00341D07"),
            RpcUuid("D9933BE0-A567-11D2-B0F3-00E02C074F6B"),
            RpcUuid("D7AB3341-C9D3-11D1-BB47-0080C7C5A2C0"),
            RpcUuid("D7D6E082-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("0FB15084-AF41-11CE-BD2B-204C4F4F5020"),
            RpcUuid("D7D6E083-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("EBA96B13-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B1D-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B17-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B20-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E074-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("7FBE7759-5760-444D-B8A5-5E7AB9A84CCE"),
            RpcUuid("B196B287-BAB4-101A-B69C-00AA00341D07"),
            RpcUuid("EBA96B12-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B1E-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E07E-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("D7D6E081-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("D7D6E07B-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("64C478FB-F9B0-4695-8A7F-439AC94326D3"),
            RpcUuid("EBA96B16-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B19-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B10-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B21-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E076-DCCD-11D0-AA4B-0060970DEBAE"),
            RpcUuid("EBA96B0F-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("EBA96B11-2168-11D3-898C-00E02C074F6B"),
            RpcUuid("D7D6E080-DCCD-11D0-AA4B-0060970DEBAE"),
        ],
        named_pipes=[]
    ),

    ## TODO: MC-

    "MS-ADTG": RpcInterfaceDefinition(
        "MS-ADTG",
        RpcInterfaceMetadata(
            "Remote Data Services (RDS) Transport Protocol",
            "",
            # note: The functionality supplied by the RDS Transport Protocol has been superseded by SOAP and DCOM
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adtg/e2d9f59e-28c4-499e-ab81-5b582c1f3bd6"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("0EAC4842-8763-11CF-A743-00AA00A3F00D", "IDataFactory"),
            RpcUuid("070669EB-B52F-11D1-9270-00C04FBBBFB3", "IDataFactory2"),
            RpcUuid("4639DB2A-BFC5-11D2-9318-00C04FBBBFB3", "IDataFactory3")
        ],
        named_pipes=[]
    ),

    "MS-BKRP": RpcInterfaceDefinition(
        id="MS-BKRP",
        metadata=RpcInterfaceMetadata(
            name="BackupKey Remote Protocol",
            description=(
                "This protocol encrypts secret values (such as cryptographic keys) "
                "so they can be backed up to storage that is not specially protected, "
                "and enables decryption of such values if recovery is necessary."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-bkrp/90b08be4-5175-4177-b4ce-d920d797e3a8"
        ),
        profiles=[
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        uuids=[
            RpcUuid("3DDE7C30-165D-11D1-AB8F-00805F14DB40", "BackupKey")
        ],
        named_pipes=[
            RpcNamedPipe("\\\\pipe\\protected_storage"),
            RpcNamedPipe("\\\\pipe\\ntsvcs")
        ]
    ),

    "MS-BPAU": RpcInterfaceDefinition(
        id="MS-BPAU",
        metadata=RpcInterfaceMetadata(
            name="Background Intelligent Transfer Service (BITS) Peer-Caching: Peer Authentication Protocol",
            description=(
                "The BITS Peer-Caching: Peer Authentication Protocol allows hosts in an "
                "Active Directory domain to exchange self-signed X.509 certificates with "
                "enough information to associate those certificates securely with a domain account."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-bpau/ce053264-a500-40df-b963-98d5f911db5d"
        ),
        profiles=[],
        uuids=[
            RpcUuid("E3D0D746-D2AF-40FD-8A7A-0D7078BB7092", "BitsPeerAuth"),
        ],
        named_pipes=[]
    ),

    "MS-BRWSA": RpcInterfaceDefinition(
        id="MS-BRWSA",
        metadata=RpcInterfaceMetadata(
            name="Common Internet File System (CIFS) Browser Auxiliary Protocol",
            description=(
                "The Common Internet File System (CIFS) Browser Auxiliary Protocol, "
                "which is used by the master browser server to query configuration information "
                "for the domains from the domain master browser server."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-brwsa/5995d2f2-fff1-40af-9100-ca67794d50a5"
        ),
        profiles=[
            # TODO: confirm
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        uuids=[
            RpcUuid("6BFFD098-A112-3610-9833-012892020162", "MS-BRWSA")
        ],
        named_pipes=[]
    ),

    "MS-CAPR": RpcInterfaceDefinition(
        id="MS-CAPR",
        metadata=RpcInterfaceMetadata(
            name="Central Access Policy Identifier (ID) Retrieval Protocol",
            description=(
                "The Central Access Policy ID Retrieval (CAPR) Protocol is designed "
                "to allow an administrative tool running on one computer to remotely "
                "query the set of central access control policies configured on another computer."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-capr/66f308bc-ebc7-4870-8b41-d8da9495b222"
        ),
        profiles=[
            # TODO: confirm
            # RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        uuids=[
            RpcUuid("AFC07E2E-311C-4435-808C-C483FFEEC7C9", "lsacap")
        ],
        named_pipes=[]
    ),

    "MS-CMRP": RpcInterfaceDefinition(
        id="MS-CMRP",
        metadata=RpcInterfaceMetadata(
            name="Failover Cluster: Management API (ClusAPI) Protocol",
            description=(
                "The Failover Cluster: Management API (ClusAPI) Protocol is an "
                "RPC-based protocol that is used for remotely managing a cluster."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cmrp/ba4117c0-530e-4e70-a085-4b4cf5bbf193"
        ),
        profiles=[
            RpcInterfaceProfile(ServiceFeature.FAILOVER_CLUSTERING, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        uuids=[
            RpcUuid("B97DB8B2-4C63-11CF-BFF6-08002BE23F2F", "MS-CMRP")
        ],
        named_pipes=[]
    ),

    "MS-COM": RpcInterfaceDefinition(
        "MS-COM",
        RpcInterfaceMetadata(
            "Component Object Model Plus (COM+) Protocol",
            (
                "Specifies the Component Object Model Plus (COM+) Protocol, which consists of a "
                "DCOM interface (and DCOM protocol extensions) that is used for adding transactions, "
                "implementing synchronization, managing multiple object class configurations, "
                "enforcing security, and providing additional functionality and attributes to "
                "DCOM-based distributed object applications."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-com/a846e48d-bbc9-4b28-9650-601810cf3af0"
        ),
        [
            # TODO: COM
        ],
        [
            RpcUuid("97199110-DB2E-11D1-A251-0000F805CA53", "ITransactionStream (IID_ITransactionStream)")
        ]
    ),

    "MS-COMA": RpcInterfaceDefinition(
        "MS-COMA",
        RpcInterfaceMetadata(
            "Component Object Model Plus (COM+) Remote Administration Protocol",
            (
                "The Component Object Model Plus (COM+) Remote Administration Protocol enables "
                "remote clients to register, import, remove, configure, control, and monitor "
                "components and conglomerations for an Object Request Broker (ORB)."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-coma/c5b1ef02-e8f6-4195-9efe-9667928d1bdd"
        ),
        [
            # TODO: COM
        ],
        [
            RpcUuid("0E3D6630-B46B-11D1-9D2D-006008B0E5CA", "ICatalogTableRead"),
            RpcUuid("3F3B1B86-DBBE-11D1-9DA6-00805F85CFE3", "IContainerControl"),
            RpcUuid("7F43B400-1A0E-4D57-BBC9-6B0C65F7A889", "IAlternateLaunch"),
            RpcUuid("456129E2-1078-11D2-B0F9-00805FC73204", "ICatalogUtils"),
            RpcUuid("8DB2180E-BD29-11D1-8B7E-00C04FD7A924", "IRegister"),
            RpcUuid("182C40FA-32E4-11D0-818B-00A0C9231C29", "ICatalogSession"),
            RpcUuid("971668DC-C3FE-4EA1-9643-0C7230F494A1", "IRegister2"),
            RpcUuid("98315903-7BE5-11D2-ADC1-00A02463D6E7", "IReplicationUtil"),
            RpcUuid("6C935649-30A6-4211-8687-C4C83E5FE1C7", "IContainerControl2"),
            RpcUuid("F131EA3E-B7BE-480E-A60D-51CB2785779E", "IExport2"),
            RpcUuid("1F7B1697-ECB2-4CBB-8A0E-75C427F4A6F0", "IImport2"),
            RpcUuid("A8927A41-D3CE-11D1-8472-006008B0E5CA", "ICatalogTableInfo"),
            RpcUuid("CFADAC84-E12C-11D1-B34C-00C04F990D54", "IExport"),
            RpcUuid("1D118904-94B3-4A64-9FA6-ED432666A7B9", "ICatalog64BitSupport"),
            RpcUuid("47CDE9A1-0BF6-11D2-8016-00C04FB9988E", "ICapabilitySupport"),
            RpcUuid("0E3D6631-B46B-11D1-9D2D-006008B0E5CA", "ICatalogTableWrite"),
            RpcUuid("C2BE6970-DF9E-11D1-8B87-00C04FD7A924", "IImport"),
            RpcUuid("C726744E-5735-4F08-8286-C510EE638FB6", "ICatalogUtils2"),
        ]
    ),

    "MS-COMEV": RpcInterfaceDefinition(
        "MS-COMEV",
        RpcInterfaceMetadata(
            "Component Object Model Plus (COM+) Event System Protocol",
            (
                "The Component Object Model Plus (COM+) Event System Protocol is a protocol that "
                "exposes DCOM interfaces for storing and managing configuration data for publishers "
                "of events and their respective subscribers on remote computers. This protocol also "
                "specifies how to get specific information about a publisher and its subscribers."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-comev/fe6baa92-4e19-49b7-9880-87db94d12299"
        ),
        [
            # TODO: COM
        ],
        [
            RpcUuid("FB2B72A0-7A68-11D1-88F9-0080C7D771BF", "IEventClass"),
            RpcUuid("FB2B72A1-7A68-11D1-88F9-0080C7D771BF", "IEventClass2"),
            RpcUuid("7FB7EA43-2D76-4EA8-8CD9-3DECC270295E", "IEventClass3"),
            RpcUuid("4E14FB9F-2E22-11D1-9964-00C04FBBB345", "IEventSystem"),
            RpcUuid("99CC098F-A48A-4E9C-8E58-965C0AFC19D5", "IEventSystem2"),
            RpcUuid("4A6B0E15-2E38-11D1-9965-00C04FBBB345", "IEventSubscription"),
            RpcUuid("4A6B0E16-2E38-11D1-9965-00C04FBBB345", "IEventSubscription2"),
            RpcUuid("FBC1D17D-C498-43A0-81AF-423DDD530AF6", "IEventSubscription3"),
            RpcUuid("F89AC270-D4EB-11D1-B682-00805FC79216", "IEventObjectCollection"),
            RpcUuid("A0E8F27A-888C-11D1-B763-00C04FB926AF", "IEventSystemInitialize"),
            RpcUuid("F4A07D63-2E25-11D1-9964-00C04FBBB345", "IEnumEventObject"),
        ]
    ),

    "MS-COMT": RpcInterfaceDefinition(
        "MS-COMT",
        RpcInterfaceMetadata(
            "Component Object Model Plus (COM+) Event System Protocol",
            (
                "The Component Object Model Plus (COM+) Tracker Service Protocol enables "
                "clients to monitor running instances of components."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-comt/e0d5ebcd-66c5-4ce5-ad7e-4f3646c92547"
        ),
        [
            # TODO: COM
        ],
        [
            RpcUuid("B60040E0-BCF3-11D1-861D-0080C729264D", "IGetTrackingData"),
            RpcUuid("23C9DD26-2355-4FE2-84DE-F779A238ADBD", "IProcessDump"),
            RpcUuid("4E6CDCC9-FB25-4FD5-9CC5-C9F4B6559CEC", "IComTrackingInfoEvents"),
        ]
    ),

    "MS-CSRA": RpcInterfaceDefinition(
        "MS-CSRA",
        RpcInterfaceMetadata(
            "Certificate Services Remote Administration Protocol",
            (
                "The Certificate Services Remote Administration Protocol consists of "
                "a set of Distributed Component Object Model (DCOM) interfaces that "
                "enable administrative tools to configure the state and policy of "
                "a certification authority (CA) on a server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-csra/40e74714-14bf-4f97-a264-35efbd63a813"
        ),
        [
            RpcInterfaceProfile(ServiceRole.CERTIFICATE_SERVICES, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("D99E6E71-FC88-11D0-B498-00A0C90312F3", "ICertAdminD"),
            RpcUuid("7FE0D935-DDA6-443F-85D0-1CFB58FE41DD", "ICertAdminD2"),
        ],
    ),

    "MS-CSVP": RpcInterfaceDefinition(
        "MS-CSVP",
        RpcInterfaceMetadata(
            "Failover Cluster: Setup and Validation Protocol (ClusPrep)",
            (
                "The Failover Cluster: Setup and Validation Protocol (ClusPrep) remotely "
                "configures cluster nodes, cleans up cluster nodes, and validates that hardware "
                "and software settings are compatible with Failover Clustering."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-csvp/600931f0-739b-4c09-8ddf-05555438c279"
        ),
        [
            RpcInterfaceProfile(ServiceFeature.FAILOVER_CLUSTERING, RpcProfileType.CORE)
        ],
        [
            RpcUuid("491260B5-05C9-40D9-B7F2-1F7BDAE0927F", "IClusterSetup"),
            RpcUuid("E3C9B851-C442-432B-8FC6-A7FAAFC09D3B", "IClusterUpdate"),
            RpcUuid("D6105110-8917-41A5-AA32-8E0AA2933DC9", "IClusterCleanup"),
            RpcUuid("85923CA7-1B6B-4E83-A2E4-F5BA3BFBB8A3", "IClusterLog"),
            RpcUuid("F1D6C29C-8FBE-4691-8724-F6D8DEAEAFC8", "IClusterFirewall"),
            RpcUuid("12108A88-6858-4467-B92F-E6CF4568DFB6", "IClusterStorage2"),
            RpcUuid("11942D87-A1DE-4E7F-83FB-A840D9C5928D", "IClusterStorage3"),
            RpcUuid("2931C32C-F731-4C56-9FEB-3D5F1C5E72BF", "IClusterNetwork2"),

            RpcUuid("C72B09DB-4D53-4f41-8DCC-2D752AB56F7C", "ClusterStorage2"),
            RpcUuid("E1568352-586D-43e4-933F-8E6DC4DE317A", "ClusterNetwork2"),
            RpcUuid("A6D3E32B-9814-4409-8DE3-CFA673E6D3DE", "ClusterCleanup"),
            RpcUuid("04D55210-B6AC-4248-9E69-2A569D1D2AB6", "ClusterSetup"),
            RpcUuid("88E7AC6D-C561-4F03-9A60-39DD768F867D", "ClusterLog"),
            RpcUuid("3CFEE98C-FB4B-44C6-BD98-A1DB14ABCA3F", "ClusterFirewall"),
            RpcUuid("4142DD5D-3472-4370-8641-DE7856431FB0", "ClusterUpdate"),
        ],
    ),

    "MS-DCOM": RpcInterfaceDefinition(
        "MS-DCOM",
        RpcInterfaceMetadata(
            "Distributed Component Object Model (DCOM) Remote Protocol",
            (
                "The Distributed Component Object Model (DCOM) Remote Protocol exposes "
                "application objects via remote procedure calls (RPCs) and consists of a "
                "set of extensions layered on the Microsoft Remote Procedure Call Extensions."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dcom/86b9cf84-df2e-4f0b-ac22-1b957627e1ca"
        ),
        [

        ],
        [
            RpcUuid("00000131-0000-0000-C000-000000000046", "IRemUnknown"),
            RpcUuid("4D9F4AB8-7D1C-11CF-861E-0020AF6E7C57", "IActivation"),
            RpcUuid("00000143-0000-0000-C000-000000000046", "IRemUnknown2"),
            RpcUuid("000001A0-0000-0000-C000-000000000046", "IRemoteSCMActivator"),
            RpcUuid("99FCFEC4-5260-101B-BBCB-00AA0021347A", "IObjectExporter"),
            RpcUuid("00000000-0000-0000-C000-000000000046", "IUnknown"),
            # RpcUuid("00000134-0000-0000-C000-000000000046", "IRundown"), ?
        ]
    ),

    "MS-DFSNM": RpcInterfaceDefinition(
        "MS-DFSNM",
        RpcInterfaceMetadata(
            "Distributed File System (DFS): Namespace Management Protocol",
            (
                "Specifies the Distributed File System (DFS): Namespace Management Protocol, "
                "which provides an RPC interface for administering DFS configurations. "
                "The client is an application that issues method calls on the RPC "
                "interface to administer DFS. The server is a DFS service that implements "
                "support for this RPC interface for administering DFS."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dfsnm/95a506a8-cae6-4c42-b19d-9c1ed1223979",
            security_notes=[
                ""
            ]
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE),
            RpcInterfaceProfile(ServiceRole.DFS_NAMESPACES, RpcProfileType.REMOTE_MANAGEMENT),
        ],
        [
            RpcUuid("4FC742E0-4A10-11CF-8273-00AA004AE673", "MS-DFSNM"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\netdfs")
        ]
    ),

    "MS-DFSRH": RpcInterfaceDefinition(
        "MS-DFSRH",
        RpcInterfaceMetadata(
            "DFS Replication Helper Protocol",
            (
                "The DFS Replication Helper Protocol is made up of a set of "
                "distributed component object model (DCOM) interfaces for configuring "
                "and monitoring DFS Replication Helper Protocols on a server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dfsrh/c3170e6b-e195-4aef-a286-8e6f4923a8ae"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DFS_REPLICATION, RpcProfileType.CORE)
        ],
        [
            # TODO: structs?
            # RpcUuid("9009D654-250B-4E0D-9AB0-ACB63134F69F"),
            # RpcUuid("D3766938-9FB7-4392-AF2F-2CE8749DBBD0"),
            # RpcUuid("CEB5D7B4-3964-4F71-AC17-4BF57A379D87"),
            # RpcUuid("7A2323C7-9EBE-494A-A33C-3CC329A18E1D"),
            RpcUuid("E65E8028-83E8-491B-9AF7-AAF6BD51A0CE", "IServerHealthReport"),
            RpcUuid("20D15747-6C48-4254-A358-65039FD8C63C", "IServerHealthReport2"),
            RpcUuid("4BB8AB1D-9EF9-4100-8EB6-DD4B4E418B72", "IADProxy"),
            RpcUuid("C4B0C7D9-ABE0-4733-A1E1-9FDEDF260C7A", "IADProxy2"),
        ]
    ),

    "MS-DHCPM": RpcInterfaceDefinition(
        "MS-DHCPM",
        RpcInterfaceMetadata(
            "Dynamic Host Configuration Protocol (DHCP) Server Management Protocol",
            (
                "The Microsoft Dynamic Host Configuration Protocol (DHCP) Server Management Protocol, "
                "defines the RPC interfaces that provide methods for remotely accessing and administering "
                "the DHCP server. This protocol is a client and server protocol based on RPC that is used "
                "in the configuration, management, and monitoring of a DHCP server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dhcpm/d117857c-1491-46a2-a68e-c844be3627d4"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DHCP, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("6BFFD098-A112-3610-9833-46C3F874532D", "dhcpsrv"),
            RpcUuid("5B821720-F63B-11D0-AAD2-00C04FC324DB", "dhcpsrv2"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\dhcpserver")
        ]
    ),

    "MS-DLTM": RpcInterfaceDefinition(
        "MS-DLTM",
        RpcInterfaceMetadata(
            "Distributed Link Tracking: Central Manager Protocol",
            (
                "The Distributed Link Tracking: Central Manager Protocol works with the "
                "Distributed Link Tracking (DLT) Workstation Protocol to discover the new "
                "location of a file that has moved. DLT can determine whether the file has "
                "moved on a mass-storage device, within a computer, or between computers in "
                "a network. The DLT Central Manager Protocol keeps track of file and volume "
                "moves and other relevant information from participating computers in order to "
                "provide this information in response to workstation queries."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dltm/a4a88aac-3bc5-4d5a-8136-52a3bfb979ef"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("4DA1C422-943D-11D1-ACAE-00C04FC2AA3F", "MS-DLTM"),
        ],
        [
            # TODO: confirm
        ]
    ),

    "MS-DLTW": RpcInterfaceDefinition(
        "MS-DLTW",
        RpcInterfaceMetadata(
            "Distributed Link Tracking: Workstation Protocol",
            (
                "The Distributed Link Tracking: Workstation Protocol works with the Distributed Link "
                "Tracking (DLT) Central Manager Protocol to discover the new location of a file that "
                "has moved. DLT can determine whether the file has moved on a mass-storage device, "
                "within a computer, or between computers in a network."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dltw/fc649f0e-871a-431a-88b5-d5b2f80e9cc9"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("300F3532-38CC-11D0-A3F0-0020AF6B0ADD", "MS-DLTW"),
        ],
        [
             RpcNamedPipe("\\\\pipe\\ntsvcs"),
             RpcNamedPipe("\\\\pipe\\trkwks")
        ]
    ),

    "MS-DMRP": RpcInterfaceDefinition(
        "MS-DMRP",
        RpcInterfaceMetadata(
            "Disk Management Remote Protocol",
            (
                "The Disk Management Remote Protocol is a set of Distributed Component Object Model (DCOM) "
                "interfaces that manages storage objects on a machine."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dmrp/19a16e20-072f-4d74-a245-ce4df2f1ecdd"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.DISK_MANAGEMENT, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("D2D79DF5-3400-11D0-B40B-00AA005FF586", "IVolumeClient (dmintf)"),
            RpcUuid("3A410F21-553F-11D1-8E5E-00A0C92C9D5D", "IDMRemoteServer (dmintf)"),
            RpcUuid("D2D79DF7-3400-11D0-B40B-00AA005FF586", "IDMNotify (dmintf)"),
            RpcUuid("4BDAFC52-FE6A-11D2-93F8-00105A11164A", "IVolumeClient2 (dmintf)"),
            RpcUuid("DEB01010-3A37-4D26-99DF-E2BB6AE3AC61", "IVolumeClient4 (dmintf3)"),
            RpcUuid("135698D2-3A37-4D26-99DF-E2BB6AE3AC61", "IVolumeClient3 (dmintf3)"),
        ]
    ),

    "MS-DNSP": RpcInterfaceDefinition(
        "MS-DNSP",
        RpcInterfaceMetadata(
            "Domain Name Service (DNS) Server Management",
            (
                "The Domain Name Service (DNS) Server Management Protocol defines the RPC "
                "interfaces that provide methods for remotely accessing and administering a DNS server. "
                "It is a client and server protocol based on RPC that is used in the configuration, "
                "management, and monitoring of a DNS server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dnsp/f97756c9-3783-428b-9451-b376f877319a"
        ),
        [
            # Maybe DC?
            RpcInterfaceProfile(ServiceRole.DNS, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("50ABC2A4-574D-40B3-9D66-EE4FD5FBA076", "dnsserver")
        ],
        [
            RpcNamedPipe("\\\\pipe\\dnsserver")
        ]
    ),

    "MS-DRSR": RpcInterfaceDefinition(
        "MS-DRSR",
        RpcInterfaceMetadata(
            "Directory Replication Service (DRS) Remote Protocol",
            (
                "The Directory Replication Service (DRS) Remote Protocol is an RPC protocol "
                "for replication and management of data in Active Directory."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-drsr/f977faaa-673e-4f66-b9bf-48c640241d47"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("7C44D7D4-31D5-424C-BD5E-2B3E1F323D22", "dsaop"),
            RpcUuid("E3514235-4B06-11D1-AB04-00C04FC2DCD2", "drsuapi"),
        ]
    ),

    "MS-DSSP": RpcInterfaceDefinition(
        "MS-DSSP",
        RpcInterfaceMetadata(
            "Directory Services Setup Remote Protocol",
            (
                "The Directory Services Setup Remote Protocol exposes an RPC interface "
                "that a client can call to obtain domain-related computer state and configuration information."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dssp/6f843846-2494-4d49-b715-2f181317dd34"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("3919286A-B10C-11D0-9BA8-00C04FD92EF5", "lsarpc")
            # maybe 51b836e8-484d-4d03-b0fc-22e265cb3f7b too
        ],
        [
            RpcNamedPipe("\\\\pipe\\lsarpc")
        ]
    ),

    "MS-EERR": RpcInterfaceDefinition(
        "MS-EERR",
        RpcInterfaceMetadata(
            "ExtendedError Remote Data Structure",
            (
                "The ExtendedError Remote Data Structure encodes extended error information. "
                "This data structure assumes that the reader has familiarity with the concepts "
                "and the requirements that are detailed in [MS-RPCE] and [C706]."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-eerr/572bb78f-9116-4966-8f9d-4593456da307"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("14A8831C-BC82-11D2-8A64-0008C7457E5D")
        ]
    ),

    "MS-EFSR": RpcInterfaceDefinition(
        "MS-EFSR",
        RpcInterfaceMetadata(
            "Encrypting File System Remote (EFSRPC) Protocol",
            (
                "The Encrypting File System Remote (EFSRPC) Protocol performs maintenance "
                "and management operations on encrypted data that is stored remotely and accessed over a network."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("df1941c5-fe89-4e79-bf10-463657acf44d", "efsrpc"),
            RpcUuid("C681D488-D850-11D0-8C52-00C04FD90F7E", "lsarpc"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\efsrpc"),
            RpcNamedPipe("\\\\pipe\\lsarpc")
        ]
    ),

    "MS-EVEN": RpcInterfaceDefinition(
        "MS-EVEN",
        RpcInterfaceMetadata(
            "EventLog Remoting Protocol",
            (
                "The EventLog Remoting Protocol exposes the RPC methods for "
                "reading events in both live and backup event logs on remote computers."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even/55b13664-f739-4e4e-bd8d-04eeda59d09f"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.EVENT_LOG, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("82273FDC-E32A-18C3-3F78-827929DC23EA", "eventlog"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\eventlog")
        ]
    ),

        
    "MS-EVEN6": RpcInterfaceDefinition(
        "MS-EVEN6",
        RpcInterfaceMetadata(
            "EventLog Remoting Protocol Version 6.0",
            (
                "The EventLog Remoting Protocol Version 6.0 protocol exposes RPC methods "
                "for reading events in both live and backup event logs on remote computers. "
                "This protocol was originally made available for Windows Vista."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-even6/18000371-ae6d-45f7-95f3-249cbe2be39b"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.EVENT_LOG, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("F6BEAFF7-1E19-4FBB-9F8F-B89E2018337C", "MS-EVEN6"),
        ]
    ),

    "MS-FASP": RpcInterfaceDefinition(
        "MS-FASP",
        RpcInterfaceMetadata(
            "Firewall and Advanced Security Protocol",
            (
                "The Firewall and Advanced Security Protocol manages firewall "
                "and advanced security components on remote computers."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fasp/55e50895-2e1f-4479-b130-122f9dc0265f"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.FIREWALL, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("6B5BDD1E-528C-422C-AF8C-A4079BE4FE48", "MS-FASP"),
        ]
    ),
    
    "MS-FAX": RpcInterfaceDefinition(
        "MS-FAX",
        RpcInterfaceMetadata(
            "Fax Server and Client Remote Protocol",
            (
                "The Fax Server and Client Remote Protocol is an RPC-based, client-server "
                "protocol, and is used to send faxes and to manage the fax server and its queues."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fax/dabce486-05b1-4ea4-95fe-f2c3d5315ff4"
        ),
        [
            # TODO: maybe split into management / core?
            RpcInterfaceProfile(ServiceRole.FAX, RpcProfileType.HYBRID)
        ],
        [
            RpcUuid("6099FC12-3EFF-11D0-ABD0-00C04FD91A4E", "faxclient"),
            RpcUuid("EA0A3165-4834-11D2-A6F8-00C04FA346CC", "sharedfax"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\sharefax")
        ]
    ),

    "MS-FRS1": RpcInterfaceDefinition(
        "MS-FRS1",
        RpcInterfaceMetadata(
            "File Replication Service Protocol",
            (
                "The File Replication Service Protocol is a replication protocol that is "
                "used to replicate files and folders across one or more members in an "
                "Active Directory domain. It works to keep copies of a file system tree "
                "up to date on all members of a replication group, while allowing any "
                "member of the group to change the contents at any time."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-frs1/0fa4f914-9442-4b49-93cc-038674a333f1"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("D049B186-814F-11D1-9A3C-00C04FC9B232", "NtFrsApi"),
            RpcUuid("F5CC59B4-4264-101A-8C59-08002B2F8426", "frsrpc"),
            # a00c021c-2be2-11d2-b678-0000f87a8f8e = File Replication (PerfFrs)
        ]
    ),

    "MS-FRS2": RpcInterfaceDefinition(
        "MS-FRS2",
        RpcInterfaceMetadata(
            "Distributed File System Replication Protocol",
            (
                "The SD Microsoft Distributed File System Replication Protocol is an RPC "
                "interface that replicates files between servers and enables the creation "
                "of multimaster optimistic file replication systems."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-frs2/9914bdd4-9579-43a7-9f2d-9efe2e162944"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE), # TODO: confirm
            RpcInterfaceProfile(ServiceRole.DFS_REPLICATION, RpcProfileType.CORE)
        ],
        [
            RpcUuid("897E2E5F-93F3-4376-9C9C-FD2277495C27", "MS-FRS2")
        ]
    ),

    "MS-FSRM": RpcInterfaceDefinition(
        "MS-FSRM",
        RpcInterfaceMetadata(
            "File Server Resource Manager Protocol",
            (
                "The File Server Resource Manager Protocol implements a set of a "
                "Distributed Component Object Model (DCOM) interfaces for managing "
                "the configuration of directory quotas, file screens, and storage "
                "report jobs on a machine."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fsrm/907f898e-2eb6-44d7-aaca-48fa46ff6941"
        ),
        [
            RpcInterfaceProfile(ServiceRole.FSRM, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("0770687E-9F36-4D6F-8778-599D188461C9", "IFsrmFileManagementJob"),
            RpcUuid("12937789-E247-4917-9C20-F3EE9C7EE783", "IFsrmActionCommand"),
            RpcUuid("1568A795-3924-4118-B74B-68D8F0FA5DAF", "IFsrmQuotaBase"),
            RpcUuid("15A81350-497D-4ABA-80E9-D4DBCC5521FE", "IFsrmStorageModuleDefinition"),
            RpcUuid("1BB617B8-3886-49DC-AF82-A6C90FA35DDA", "IFsrmMutableCollection"),
            RpcUuid("205BEBF8-DD93-452A-95A6-32B566B35828", "IFsrmFileScreenTemplate"),
            RpcUuid("22BCEF93-4A3F-4183-89F9-2F8B8A628AEE", "IFsrmObject"),
            RpcUuid("27B899FE-6FFA-4481-A184-D3DAADE8A02B", "IFsrmReportManager"),
            RpcUuid("2DBE63C4-B340-48A0-A5B0-158E07FC567E", "IFsrmActionReport"),
            RpcUuid("326AF66F-2AC0-4F68-BF8C-4759F054FA29", "IFsrmPropertyCondition"),
            RpcUuid("377F739D-9647-4B8E-97D2-5FFCE6D759CD", "IFsrmQuota"),
            RpcUuid("38E87280-715C-4C7D-A280-EA1651A19FEF", "IFsrmReportJob"),
            RpcUuid("39322A2D-38EE-4D0D-8095-421A80849A82", "IFsrmDerivedObjectsResult"),
            RpcUuid("4173AC41-172D-4D52-963C-FDC7E415F717", "IFsrmQuotaTemplateManager"),
            RpcUuid("426677D5-018C-485C-8A51-20B86D00BDC4", "IFsrmFileGroupManager"),
            RpcUuid("42DC3511-61D5-48AE-B6DC-59FC00C0A8D6", "IFsrmQuotaObject"),
            RpcUuid("47782152-D16C-4229-B4E1-0DDFE308B9F6", "IFsrmPropertyDefinition2"),
            RpcUuid("4846CB01-D430-494F-ABB4-B1054999FB09", "IFsrmQuotaManagerEx"),
            RpcUuid("4A73FEE4-4102-4FCC-9FFB-38614F9EE768", "IFsrmProperty"),
            RpcUuid("4C8F96C3-5D94-4F37-A4F4-F56AB463546F", "IFsrmActionEventLog"),
            RpcUuid("515C1277-2C81-440E-8FCF-367921ED4F59", "IFsrmPipelineModuleDefinition"),
            RpcUuid("5F6325D3-CE88-4733-84C1-2D6AEFC5EA07", "IFsrmFileScreen"),
            RpcUuid("6879CAF9-6617-4484-8719-71C3D8645F94", "IFsrmReportScheduler"),
            RpcUuid("6CD6408A-AE60-463B-9EF1-E117534D69DC", "IFsrmAction"),
            RpcUuid("6F4DBFFF-6920-4821-A6C3-B7E94C1FD60C", "IFsrmPathMapper"),
            RpcUuid("8276702F-2532-4839-89BF-4872609A2EA4", "IFsrmActionEmail2"),
            RpcUuid("8BB68C7D-19D8-4FFB-809E-BE4FC1734014", "IFsrmQuotaManager"),
            RpcUuid("8DD04909-0E34-4D55-AFAA-89E1F1A1BBB9", "IFsrmFileGroup"),
            RpcUuid("96DEB3B5-8B91-4A2A-9D93-80A35D8AA847", "IFsrmCommittableCollection"),
            RpcUuid("9A2BF113-A329-44CC-809A-5C00FCE8DA40", "IFsrmQuotaTemplateImported"),
            RpcUuid("A2EFAB31-295E-46BB-B976-E86D58B52E8B", "IFsrmQuotaTemplate"),
            RpcUuid("AD55F10B-5F11-4BE7-94EF-D9EE2E470DED", "IFsrmFileGroupImported"),
            RpcUuid("AFC052C2-5315-45AB-841B-C6DB0E120148", "IFsrmClassificationRule"),
            RpcUuid("BB36EA26-6318-4B8C-8592-F72DD602E7A5", "IFsrmClassifierModuleDefinition"),
            RpcUuid("BEE7CE02-DF77-4515-9389-78F01C5AFC1A", "IFsrmFileScreenException"),
            RpcUuid("CB0DF960-16F5-4495-9079-3F9360D831DF", "IFsrmRule"),
            RpcUuid("CFE36CBA-1949-4E74-A14F-F1D580CEAF13", "IFsrmFileScreenTemplateManager"),
            RpcUuid("D2DC89DA-EE91-48A0-85D8-CC72A56F7D04", "IFsrmClassificationManager"),
            RpcUuid("D646567D-26AE-4CAA-9F84-4E0AAD207FCA", "IFsrmActionEmail"),
            RpcUuid("D8CC81D9-46B8-4FA4-BFA5-4AA9DEC9B638", "IFsrmReport"),
            RpcUuid("E1010359-3E5D-4ECD-9FE4-EF48622FDF30", "IFsrmFileScreenTemplateImported"),
            RpcUuid("E946D148-BD67-4178-8E22-1C44925ED710", "IFsrmPropertyDefinitionValue"),
            RpcUuid("EDE0150F-E9A3-419C-877C-01FE5D24C5D3", "IFsrmPropertyDefinition"),
            RpcUuid("EE321ECB-D95E-48E9-907C-C7685A013235", "IFsrmFileManagementJobManager"),
            RpcUuid("F3637E80-5B22-4A2B-A637-BBB642B41CFC", "IFsrmFileScreenBase"),
            RpcUuid("F411D4FD-14BE-4260-8C40-03B7C95E608A", "IFsrmSetting"),
            RpcUuid("F76FBF3B-8DDD-4B42-B05A-CB1C3FF1FEE8", "IFsrmCollection"),
            RpcUuid("F82E5729-6ABA-4740-BFC7-C7F58F75FB7B", "IFsrmAutoApplyQuota"),
            RpcUuid("FF4FA04E-5A94-4BDA-A3A0-D5B4D3C52EBA", "IFsrmFileScreenManager"),
        ]
    ),

    "MS-FSRVP": RpcInterfaceDefinition(
        "MS-FSRVP",
        RpcInterfaceMetadata(
            "File Server Remote VSS Protocol",
            (
                "The File Server Remote VSS Protocol is an RPC-based protocol used for "
                "creating shadow copies of file shares on a remote computer, and for "
                "facilitating backup applications in performing application-consistent "
                "backup and restore of data on SMB2 shares."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fsrvp/dae107ec-8198-4778-a950-faa7edad125b"
        ),
        [
            # Is this remote management?
            RpcInterfaceProfile(ServiceRole.FILE_SERVER_VSS_AGENT, RpcProfileType.CORE)
        ],
        [
            RpcUuid("A8E0653C-2744-4389-A61D-7373DF8B2292", "FileServerVssAgent"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\FssagentRpc")
        ]
    ),

    "MS-GKDI": RpcInterfaceDefinition(
        "MS-GKDI",
        RpcInterfaceMetadata(
            "Group Key Distribution Protocol",
            (
                "The Group Key Distribution Protocol enables clients to obtain "
                "cryptographic keys associated with Active Directory security principals."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fsrvp/dae107ec-8198-4778-a950-faa7edad125b"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("B9785960-524F-11DF-8B6D-83DCDED72085", "MS-GKDI"),
        ]
    ),

    "MS-ICPR": RpcInterfaceDefinition(
        "MS-ICPR",
        RpcInterfaceMetadata(
            "ICertPassage Remote Protocol",
            (
                "The ICertPassage Remote Protocol is subset of the Windows Client "
                "Certificate Enrollment Protocol, as specified in [MS-WCCE]. "
                "This protocol only enables the client to enroll certificates, "
                "whereas [MS-WCCE] provides enrollment and additional functionality."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-icpr/9b8ed605-6b00-41d1-9a2a-9897e40678fc"
        ),
        [
            RpcInterfaceProfile(ServiceRole.CERTIFICATE_SERVICES, RpcProfileType.CORE)
        ],
        [
            RpcUuid("91AE6020-9E3C-11CF-8D7C-00AA00C091BE", "ICertPassage"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\cert")
        ]
    ),

    "MS-IISS": RpcInterfaceDefinition(
        "MS-IISS",
        RpcInterfaceMetadata(
            "Internet Information Services (IIS) ServiceControl",
            (
                "The Internet Information Services (IIS) ServiceControl Protocol is "
                "a client-to-server protocol that enables remote control of Internet "
                "services as a single unit."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-iiss/5ac91b49-276c-4402-9ed4-82c4e7bb0c2b"
        ),
        [
            RpcInterfaceProfile(ServiceRole.WEB_SERVER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("E8FB8620-588F-11D2-9D61-00C04F79C5FE", "IIisServiceControl"),
        ]
    ),

    "MS-IMSA": RpcInterfaceDefinition(
        "MS-IMSA",
        RpcInterfaceMetadata(
            "Internet Information Services (IIS) IMSAdminBaseW",
            (
                "The Internet Information Services (IIS) IMSAdminBaseW Remote Protocol defines "
                "interfaces that provide Unicode-compliant methods for remotely accessing and "
                "administering the IIS metabase associated with an application that manages IIS "
                "configuration, such as the IIS snap-in for Microsoft Management Console (MMC)."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-imsa/9cd07fff-2cb6-44fb-be98-6f292ae2a457"
        ),
        [
            RpcInterfaceProfile(ServiceRole.WEB_SERVER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("F612954D-3B0B-4C56-9563-227B7BE624B4", "IMSAdminBase3W"),
            RpcUuid("8298D101-F992-43B7-8ECA-5052D885B995", "IMSAdminBase2W"),
            RpcUuid("29822AB8-F302-11D0-9953-00C04FD919C1", "IWamAdmin2"),
            RpcUuid("70B51430-B6CA-11D0-B9B9-00A0C922E750", "IMSAdminBaseW"),
            RpcUuid("29822AB7-F302-11D0-9953-00C04FD919C1", "IWamAdmin"),
            RpcUuid("BD0C73BC-805B-4043-9C30-9A28D64DD7D2", "IIISCertObj"),
            RpcUuid("7C4E1804-E342-483D-A43E-A850CFCC8D18", "IIISApplicationAdmin"),
        ]
    ),

    "MS-IOI": RpcInterfaceDefinition(
        "MS-IOI",
        RpcInterfaceMetadata(
            "IManagedObject Interface Protocol",
            (
                "The IManagedObject Interface Protocol provides a COM interface "
                "used by the common language runtime (CLR) to identify managed "
                "objects (objects created by the CLR) that are exported for "
                "interoperability with the Component Object Model (COM)."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ioi/0d0efe1d-a04d-433b-b9aa-efa6cf7dc148"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("6619A740-8154-43BE-A186-0319578E02DB", "IRemoteDispatch"),
            RpcUuid("8165B19E-8D3A-4D0B-80C8-97DE310DB583", "IServicedComponentInfo"),
            RpcUuid("C3FCC19E-A970-11D2-8B5A-00A0C9B7C9C4", "IManagedObject"),
        ]
    ),

    "MS-IRP": RpcInterfaceDefinition(
        "MS-IRP",
        RpcInterfaceMetadata(
            "Internet Information Services (IIS) Inetinfo Remote Protocol",
            (
                "The Internet Information Services (IIS) Inetinfo Remote Protocol is "
                "an RPC-based client/server protocol that is used for managing Internet "
                "protocol servers such as those hosted by IIS."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-irp/b9fa0d73-fff1-4bc4-bdc0-ce62ba855a5e"
        ),
        [
            RpcInterfaceProfile(ServiceRole.WEB_SERVER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("82AD4280-036B-11CF-972C-00AA006887B0", "inetinfo"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\inetinfo")
        ]
    ),

    "MS-ISTM": RpcInterfaceDefinition(
        "MS-ISTM",
        RpcInterfaceMetadata(
            "iSCSI Software Target Management Protocol",
            (
                "TODO"
            ),
            "https://download.microsoft.com/download/0/3/4/034A8114-5DA1-4C65-8581-C48EDD189437/[MS-ISTM].pdf"
        ),
        [
            RpcInterfaceProfile(ServiceRole.ISCSI_TARGET_SERVER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            # TODO
            RpcUuid("4E65A71E-4EDE-4886-BE67-3C90A08D1F29"),
            RpcUuid("866A78BC-A2FB-4AC4-94D5-DB3041B4ED75"),
            RpcUuid("B0D1AC4B-F87A-49B2-938F-D439248575B2"),
            RpcUuid("E141FD54-B79E-4938-A6BB-D523C3D49FF1"),
            RpcUuid("40CC8569-6D23-4005-9958-E37F08AE192B"),
            RpcUuid("1822A95E-1C2B-4D02-AB25-CC116DD9DBDE"),
            RpcUuid("B4FA8E86-2517-4A88-BD67-75447219EEE4"),
            RpcUuid("3C73848A-A679-40C5-B101-C963E67F9949"),
            RpcUuid("66C9B082-7794-4948-839A-D8A5A616378F"),
            RpcUuid("01454B97-C6A5-4685-BEA8-9779C88AB990"),
            RpcUuid("D6BD6D63-E8CB-4905-AB34-8A278C93197A"),
            RpcUuid("348A0821-69BB-4889-A101-6A9BDE6FA720"),
            RpcUuid("703E6B03-7AD1-4DED-BA0D-E90496EBC5DE"),
            RpcUuid("100DA538-3F4A-45AB-B852-709148152789"),
            RpcUuid("592381E5-8D3C-42E9-B7DE-4E77A1F75AE4"),
            RpcUuid("883343F1-CEED-4E3A-8C1B-F0DADFCE281E"),
            RpcUuid("6AEA6B26-0680-411D-8877-A148DF3087D5"),
            RpcUuid("D71B2CAE-33E8-4567-AE96-3CCF31620BE2"),
            RpcUuid("8C58F6B3-4736-432A-891D-389DE3505C7C"),
            RpcUuid("1995785D-2A1E-492F-8923-E621EACA39D9"),
            RpcUuid("C10A76D8-1FE4-4C2F-B70D-665265215259"),
            RpcUuid("8D7AE740-B9C5-49FC-A11E-89171907CB86"),
            RpcUuid("8AD608A4-6C16-4405-8879-B27910A68995"),
            RpcUuid("B0076FEC-A921-4034-A8BA-090BC6D03BDE"),
            RpcUuid("640038F1-D626-40D8-B52B-09660601D045"),
            RpcUuid("BB39E296-AD26-42C5-9890-5325333BB11E"),
            RpcUuid("B06A64E3-814E-4FF9-AFAC-597AD32517C7"),
            RpcUuid("A5ECFC73-0013-4A9E-951C-59BF9735FDDA"),
            RpcUuid("1396DE6F-A794-4B11-B93F-6B69A5B47BAE"),
            RpcUuid("DD6F0A28-248F-4DD3-AFE9-71AED8F685C4"),
            RpcUuid("52BA97E7-9364-4134-B9CB-F8415213BDD8"),
            RpcUuid("E2842C88-07C3-4EB0-B1A9-D3D95E76FEF2"),
            RpcUuid("312CC019-D5CD-4CA7-8C10-9E0A661F147E"),
            RpcUuid("345B026B-5802-4E38-AC75-795E08B0B83F"),
            RpcUuid("442931D5-E522-4E64-A181-74E98A4E1748"),
            RpcUuid("1B1C4D1C-ABC4-4D3A-8C22-547FBA3AA8A0"),
            RpcUuid("56E65EA5-CDFF-4391-BA76-006E42C2D746"),
            RpcUuid("E645744B-CAE5-4712-ACAF-13057F7195AF"),
            RpcUuid("FE7F99F9-1DFB-4AFB-9D00-6A8DD0AABF2C"),
            RpcUuid("81FE3594-2495-4C91-95BB-EB5785614EC7"),
            RpcUuid("F093FE3D-8131-4B73-A742-EF54C20B337B"),
            RpcUuid("28BC8D5E-CA4B-4F54-973C-ED9622D2B3AC"),
        ],
        [
            # TODO
        ]
    ),

    "MS-LREC": RpcInterfaceDefinition(
        "MS-LREC",
        RpcInterfaceMetadata(
            "Live Remote Event Capture (LREC) Protocol",
            (
                "The Live Remote Event Capture (LREC) Protocol enables a management "
                "station to monitor events on a target system across a network. "
                "The protocol supports various monitoring scenarios, such as a "
                "_first line of defense_ for troubleshooting, where the remote "
                "system does not support the ability to log events locally."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lrec/dbd9a142-13a0-4b76-8498-45920d00530b"
        ),
        [
            #RpcInterfaceProfile(ServiceBuiltIn.LREC, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("22E5386D-8B12-4BF0-B0EC-6A1EA419E366", "NetEventForwarder")
        ]
    ),

    "MS-LSAT": RpcInterfaceDefinition(
        "MS-LSAT",
        RpcInterfaceMetadata(
            "Local Security Authority (Translation Methods) Remote",
            (
                "The Local Security Authority (Translation Methods) Remote Protocol is implemented "
                "in Windows-based products to translate identifiers for security principal between "
                "human-readable and machine-readable forms."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lsat/1ba21e6f-d8a9-462c-9153-4375f2020894"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("12345778-1234-ABCD-EF00-0123456789AB", "lsarpc")
        ],
        [
            RpcNamedPipe("\\\\pipe\\lsarpc")
        ]
    ),

    "MS-MQDS": RpcInterfaceDefinition(
        "MS-MQDS",
        RpcInterfaceMetadata(
            "Message Queuing (MSMQ): Directory Service Protocol",
            (
                "The Message Queuing (MSMQ): Directory Service Protocol is an RPC-based "
                "protocol that is used by MSMQ clients and Message Queuing servers to "
                "remotely access and maintain MSMQ directory objects."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-mqds/1c8a4041-846e-487e-a4b7-6051b9774247"
        ),
        [
            RpcInterfaceProfile(ServiceFeature.MSMQ, RpcProfileType.CORE)
        ],
        [
            RpcUuid("708CCA10-9569-11D1-B2A5-0060977D8118", "dscomm2"),
            RpcUuid("77DF7A80-F298-11D0-8358-00A024C480A8", "dscomm"),
        ]
    ),

    "MS-MQMP": RpcInterfaceDefinition(
        "MS-MQMP",
        RpcInterfaceMetadata(
            "Message Queuing (MSMQ): Queue Manager Client Protocol",
            (
                "The Message Queuing (MSMQ): Queue Manager Client Protocol enables "
                "communication between message queuing client applications and an "
                "MSMQ Queue Manager."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-mqmp/8e379aa2-802d-4fcc-b6a6-6203e4606fa9"
        ),
        [
            RpcInterfaceProfile(ServiceFeature.MSMQ, RpcProfileType.CORE)
        ],
        [
            RpcUuid("76D12B80-3467-11D3-91FF-0090272F9EA3", "qmcomm2"),
            RpcUuid("FDB3A030-065F-11D1-BB9B-00A024EA5525", "qmcomm"),
        ]
    ),

    "MS-MQMR": RpcInterfaceDefinition(
        "MS-MQMR",
        RpcInterfaceMetadata(
            "Message Queuing (MSMQ): Queue Manager Management Protocol",
            (
                "The Message Queuing (MSMQ): Queue Manager Management Protocol that is "
                "used for management operations on the MSMQ server, including monitoring "
                "the MSMQ installation and the queues."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-mqmr/7271d4fa-afdb-47b1-abf1-610f1c06386c"
        ),
        [
            RpcInterfaceProfile(ServiceFeature.MSMQ, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("41208EE0-E970-11D1-9B9E-00E02C064C39", "qmmgmt"),
        ]
    ),

    "MS-MQQP": RpcInterfaceDefinition(
        "MS-MQQP",
        RpcInterfaceMetadata(
            "Message Queuing (MSMQ): Queue Manager to Queue Manager Protocol",
            (
                "The Message Queuing (MSMQ): Queue Manager to Queue Manager Protocol is"
                "an RPC-based protocol used by the queue manager and runtime library "
                "to read and purge messages from a remote queue."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-mqqp/c9a334a7-89b4-4e75-902a-bc029e29a072"
        ),
        [
            RpcInterfaceProfile(ServiceFeature.MSMQ, RpcProfileType.CORE)
        ],
        [
            RpcUuid("1088A980-EAE5-11D0-8D9B-00A02453C337", "qm2qm"),
        ]
    ),

    "MS-MQRR": RpcInterfaceDefinition(
        "MS-MQRR",
        RpcInterfaceMetadata(
            "Message Queuing (MSMQ): Queue Manager Remote Read Protocol",
            (
                "The Message Queuing (MSMQ): Queue Manager Remote Read Protocol is "
                "an RPC-based protocol that is used by MSMQ clients to read or "
                "reject a message from a queue, move a message between queues, "
                "and purge messages from a queue."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-mqrr/9edbc8fa-02ad-4c79-804f-6bb8f430aac1"
        ),
        [
            RpcInterfaceProfile(ServiceFeature.MSMQ, RpcProfileType.CORE)
        ],
        [
            RpcUuid("1A9134DD-7B39-45BA-AD88-44D01CA47F28", "RemoteRead"),
        ]
    ),

    "MS-MSRP": RpcInterfaceDefinition(
        "MS-MSRP",
        RpcInterfaceMetadata(
            "Messenger Service Remote Protocol",
            (
                "The Messenger Service Remote Protocol is a set of RPC interfaces "
                "that instructs a server to display short text messages to a console "
                "user, to deliver messages to a local or remote server for display to "
                "a console user, and to manage the names for which the server receives messages."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-mqrr/9edbc8fa-02ad-4c79-804f-6bb8f430aac1"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("17FDD703-1827-4E34-79D4-24A55C53BB37", "msgsvc"),
            RpcUuid("5A7B91F8-FF00-11D0-A9B2-00C04FB6E6FC", "msgsvcsend"),
        ]
    ),

    "MS-NRPC": RpcInterfaceDefinition(
        "MS-NRPC",
        RpcInterfaceMetadata(
            "Netlogon Remote Protocol",
            (
                "The Netlogon Remote Protocol is an RPC interface that is used for "
                "user and machine authentication on domain-based networks; to replicate "
                "the user account database for operating systems earlier than Windows "
                "2000 backup domain controllers; to discover, manage, and maintain "
                "domain relationships of domain members and domain controllers across domains."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/ff8f970f-3e37-40f7-bd4b-af7336e4792f"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("12345678-1234-ABCD-EF00-01234567CFFB", "logon"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\netlogon")
        ]
    ),

    "MS-OAUT": RpcInterfaceDefinition(
        "MS-OAUT",
        RpcInterfaceMetadata(
            "OLE Automation Protocol",
            (
                "The OLE Automation Protocol uses DCOM as its transport layer and provides "
                "support for an additional set of types as well as for a late-bound calling mechanism."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-oaut/bbb05720-f724-45c7-8d17-f83c3d1a3961"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("00020400-0000-0000-C000-000000000046", "IDispatch"),
            RpcUuid("00020401-0000-0000-C000-000000000046", "ITypeInfo"),
            RpcUuid("00020402-0000-0000-C000-000000000046", "ITypeLib"),
            RpcUuid("00020403-0000-0000-C000-000000000046", "ITypeComp"),
            RpcUuid("00020404-0000-0000-C000-000000000046", "IEnumVARIANT"),
            RpcUuid("00020411-0000-0000-C000-000000000046", "ITypeLib2"),
            RpcUuid("00020412-0000-0000-C000-000000000046", "ITypeInfo2"),
        ]
    ),

    "MS-OCSPA": RpcInterfaceDefinition(
        "MS-OCSPA",
        RpcInterfaceMetadata(
            "Microsoft OCSP Administration Protocol",
            (
                "The Microsoft OCSP Administration Protocol consists of a set "
                "of distributed component object model (DCOM) interfaces that "
                "allows administrative tools to configure the properties of "
                "the Online Responder"
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ocspa/bfe568cf-e1c4-4b03-b344-002e643a6ff5"
        ),
        [
            RpcInterfaceProfile(ServiceRole.CERTIFICATE_SERVICES, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("784B693D-95F3-420B-8126-365C098659F2", "IOCSPAdminD"),
        ]
    ),

    "MS-PAN": RpcInterfaceDefinition(
        "MS-PAN",
        RpcInterfaceMetadata(
            "Print System Asynchronous Notification Protocol",
            (
                "The Print System Asynchronous Notification Protocol is an asynchronous "
                "protocol that clients use to receive print status notifications from a "
                "print server and send server-requested responses to those notifications "
                "back to the server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pan/e44d984c-07d3-414c-8ffc-f8c8ad8512a8"
        ),
        [
            RpcInterfaceProfile(ServiceRole.PRINTING, RpcProfileType.CORE)
        ],
        [
            RpcUuid("AE33069B-A2A8-46EE-A235-DDFD339BE281", "IRPCRemoteObject"),
            RpcUuid("0B6EDBFA-4A24-4FC6-8A23-942B1ECA65D1", "IRPCAsyncNotify"),

            # 4a452661-8290-4b36-8fbe-7f4093a94978 - spooler??
        ]
    ),

    "MS-PAR": RpcInterfaceDefinition(
        "MS-PAR",
        RpcInterfaceMetadata(
            "Print System Asynchronous Remote Protocol",
            (
                "The Print System Asynchronous Remote Protocol defines the communication "
                "of print job processing and print system management information between "
                "a print client and a print server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-par/695e3f9a-f83f-479a-82d9-ba260497c2d0"
        ),
        [
            RpcInterfaceProfile(ServiceRole.PRINTING, RpcProfileType.CORE)
        ],
        [
            RpcUuid("76F03F96-CDFD-44FC-A22C-64950A001209", "IRemoteWinspool"),
        ]
    ),

    "MS-PCQ": RpcInterfaceDefinition(
        "MS-PCQ",
        RpcInterfaceMetadata(
            "Performance Counter Query Protocol",
            (
                "The Performance Counter Query Protocol is used for browsing "
                "performance counters and retrieving performance counter values from a server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pcq/08f8d061-2974-4657-9dc7-9880ce7cb5f9"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.PERFORMANCE_COUNTERS, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("DA5A86C5-12C2-4943-AB30-7F74A813D853", "PerflibV2"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\winreg")
        ]
    ),

    "MS-PLA": RpcInterfaceDefinition(
        "MS-PLA",
        RpcInterfaceMetadata(
            "Performance Logs and Alerts Protocol",
            (
                "The Performance Logs and Alerts Protocol, which provides a set of DCOM "
                "interfaces to control data collection on a remote system. "
                "The control includes starting, stopping, scheduling, and configuration "
                "of data collector objects, and the creation of alerts."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pla/d752a77f-442f-4e38-8a40-4b5258e83700"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("03837510-098B-11D8-9414-505054503030", "ITraceDataProviderCollection"),
            RpcUuid("03837543-098B-11D8-9414-505054503030", "IFolderAction"),
            RpcUuid("03837533-098B-11D8-9414-505054503030", "IValueMapItem"),
            RpcUuid("03837541-098B-11D8-9414-505054503030", "03837541"),
            RpcUuid("03837544-098B-11D8-9414-505054503030", "IFolderActionCollection"),
            RpcUuid("03837524-098B-11D8-9414-505054503030", "IDataCollectorSetCollection"),
            RpcUuid("0383753A-098B-11D8-9414-505054503030", "ISchedule"),
            RpcUuid("03837534-098B-11D8-9414-505054503030", "IValueMap"),
            RpcUuid("0383750B-098B-11D8-9414-505054503030", "ITraceDataCollector"),
            RpcUuid("0383751A-098B-11D8-9414-505054503030", "IApiTracingDataCollector"),
            RpcUuid("03837512-098B-11D8-9414-505054503030", "ITraceDataProvider"),
            RpcUuid("0383753D-098B-11D8-9414-505054503030", "IScheduleCollection"),
            RpcUuid("03837506-098B-11D8-9414-505054503030", "IPerformanceCounterDataCollector"),
            RpcUuid("03837520-098B-11D8-9414-505054503030", "IDataCollectorSet"),
            RpcUuid("038374FF-098B-11D8-9414-505054503030", "IDataCollector"),
            RpcUuid("03837514-098B-11D8-9414-505054503030", "IConfigurationDataCollector"),
            RpcUuid("03837502-098B-11D8-9414-505054503030", "IDataCollectorCollection"),
            RpcUuid("03837516-098B-11D8-9414-505054503030", "IAlertDataCollector"),
        ]
    ),

    "MS-RAA": RpcInterfaceDefinition(
        "MS-RAA",
        RpcInterfaceMetadata(
            "Remote Authorization API Protocol",
            (
                "The Remote Authorization API Protocol is used to perform 'what-if' "
                "authorization queries on remote computers. It allows applications to "
                "simulate an access control decision that would be made when a principal "
                "attempts to access a remote resource protected with an authorization policy."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raa/98ab2e01-da37-4e76-bea5-8d4d83e66e1a"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("0B1C2170-5732-4E0E-8CD3-D9B16F3B84D7", "authzr"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\lsass")
        ]
    ),

    "MS-RAI": RpcInterfaceDefinition(
        "MS-RAI",
        RpcInterfaceMetadata(
            "Remote Assistance Initiation Protocol",
            (
                "The Remote Assistance Initiation Protocol enables an authorized expert "
                "to start Remote Assistance (RA) on a remote novice computer to retrieve "
                "data that is required to make a Remote Assistance connection from the "
                "expert's computer to the novice's computer."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rai/8711afb1-c382-4ba7-8b38-f344fb2c4030"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.REMOTE_ASSISTANCE, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("F120A684-B926-447F-9DF4-C966CB785648", "IRASrv"),
            RpcUuid("833E4010-AFF7-4AC3-AAC2-9F24C1457BCE", "PCHService Class"),
            RpcUuid("833E4200-AFF7-4AC3-AAC2-9F24C1457BCE", "IPCHService"),
            RpcUuid("3C3A70A7-A468-49B9-8ADA-28E11FCCAD5D", "RASrv Class"),
            RpcUuid("833E4100-AFF7-4AC3-AAC2-9F24C1457BCE", "IPCHCollection"),
            RpcUuid("833E41AA-AFF7-4AC3-AAC2-9F24C1457BCE", "ISAFSession"),
        ]
    ),

    "MS-RAINPS": RpcInterfaceDefinition(
        "MS-RAINPS",
        RpcInterfaceMetadata(
            "Remote Administrative Interface: NPS",
            (
                "The Remote Administrative Interface: Network Policy Server (NPS) Protocol, "
                "also known as the Internet Authentication Service (IAS) Data Server Store COM Protocol, "
                "is a client-server protocol that enables local or remote administration of remote access "
                "policies, configuration, and operational parameters on a Network Policy Server (NPS)"
            ),
            "https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/WinArchive/%5BMS-RAINPS%5D.pdf"
        ),
        [
            RpcInterfaceProfile(ServiceRole.NPS, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("C323BE28-E546-4C23-A81B-D6AD8D8FAC7B", "IIASDataStoreComServer2"),
            RpcUuid("83E05BD5-AEC1-4E58-AE50-E819C7296F67", "IIASDataStoreComServer"),
        ]
    ),

    "MS-RAIW": RpcInterfaceDefinition(
        "MS-RAIW",
        RpcInterfaceMetadata(
            "Remote Administrative Interface: WINS",
            (
                "The Remote Administrative Interface: WINS protocol enables local or remote "
                "administration of the Windows Internet Name Service (WINS) within the Microsoft "
                "Management Console (MMC) WINS snap-in and the NetSh command line (WINS context)."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-raiw/830a759d-3157-4bfa-901a-d7dcd860c3b9"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.WINS, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("45F52C28-7F9F-101A-B52B-08002B2EFABE", "winsif"),
            RpcUuid("811109BF-A4E1-11D1-AB54-00A0C91E9B45", "winsi2"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\winspipe")
        ]
    ),

    "MS-RPRN": RpcInterfaceDefinition(
        "MS-RPRN",
        RpcInterfaceMetadata(
            "Print System Remote Protocol",
            (
                "The Print System Remote Protocol defines the communication of "
                "print job processing and print system management between a "
                "print client and a print server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/d42db7d5-f141-4466-8f47-0a4be14e2fc1"
        ),
        [
            RpcInterfaceProfile(ServiceRole.PRINTING, RpcProfileType.CORE)
        ],
        [
            RpcUuid("12345678-1234-ABCD-EF00-0123456789AB", "winspool"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\spoolss")
        ]
    ),

    "MS-RRASM": RpcInterfaceDefinition(
        "MS-RRASM",
        RpcInterfaceMetadata(
            "Routing and Remote Access Server (RRAS) Management Protocol",
            (
                "The Routing and Remote Access Server (RRAS) Management Protocol "
                "enables remote management (configuration and monitoring) of RRAS. "
                "The RRAS implementation refers to the components that can be configured "
                "to provide routing, remote access service, and site-to-site connectivity."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rrasm/a1e2840d-c9ff-4407-abf4-17aa6af34112"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("20610036-FA22-11CF-9823-00A0C911E5DF", "rasrpc"),
            RpcUuid("5FF9BDF6-BD91-4D8B-A614-D6317ACC8DD8", "IRemoteSstpCertCheck"),
            RpcUuid("6139D8A4-E508-4EBB-BAC7-D7F275145897", "IRemoteIPV6Config"),
            RpcUuid("66A2DB1B-D706-11D0-A37B-00C04FC9DA04", "IRemoteNetworkConfig"),
            RpcUuid("66A2DB20-D706-11D0-A37B-00C04FC9DA04", "IRemoteRouterRestart"),
            RpcUuid("66A2DB21-D706-11D0-A37B-00C04FC9DA04", "IRemoteSetDnsConfig"),
            RpcUuid("66A2DB22-D706-11D0-A37B-00C04FC9DA04", "IRemoteICFICSConfig"),
            RpcUuid("67E08FC2-2984-4B62-B92E-FC1AAE64BBBB", "IRemoteStringIdConfig"),
            RpcUuid("8F09F000-B7ED-11CE-BBD2-00001A181CAD", "dimsvc"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\router")
        ]
    ),

    "MS-RRP": RpcInterfaceDefinition(
        "MS-RRP",
        RpcInterfaceMetadata(
            "Windows Remote Registry Protocol",
            (
                "The Windows Remote Registry Protocol is a remote procedure call "
                "(RPC)-based client/server protocol that is used to remotely "
                "manage a hierarchical data store such as the Windows registry."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/0fa3191d-bb79-490a-81bd-54c2601b7a78"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.REMOTE_REGISTRY, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("338CD001-2244-31F1-AAAA-900038001003", "winreg"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\winreg")
        ]
    ),

    "MS-RSMP": RpcInterfaceDefinition(
        "MS-RSMP",
        RpcInterfaceMetadata(
            "Removable Storage Manager (RSM) Remote Protocol",
            (
                "The Removable Storage Manager (RSM) Remote Protocol is a set of distributed "
                "component object model (DCOM) interfaces for applications to manage robotic "
                "changers, media libraries, and tape drives. This protocol deals with detailed "
                "low-level operating system and storage concepts."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rsmp/5873331e-7fa2-4131-a493-769087a1c89f"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("3BBED8D9-2C9A-4B21-8936-ACB2F995BE6C", "INtmsObjectManagement3"),
            RpcUuid("8DA03F40-3419-11D1-8FB1-00A024CB6019", "INtmsSession1"),
            RpcUuid("D61A27C6-8F53-11D0-BFA0-00A024151983", "CNtmsSvr (Removable Storage Manager Class)"),
            RpcUuid("081E7188-C080-4FF3-9238-29F66D6CABFD", "IMessenger"),
            RpcUuid("895A2C86-270D-489D-A6C0-DC2A9B35280E", "INtmsObjectManagement2"),
            RpcUuid("D02E4BE0-3419-11D1-8FB1-00A024CB6019", "INtmsMediaServices1"),
            RpcUuid("DB90832F-6910-4D46-9F5E-9FD6BFA73903", "INtmsLibraryControl2"),
            RpcUuid("4E934F30-341A-11D1-8FB1-00A024CB6019", "INtmsLibraryControl1"),
            RpcUuid("879C8BBE-41B0-11D1-BE11-00C04FB6BF70", "IClientSink"),
            RpcUuid("69AB7050-3059-11D1-8FAF-00A024CB6019", "INtmsObjectInfo1"),
            RpcUuid("7D07F313-A53F-459A-BB12-012C15B1846E", "IRobustNtmsMediaServices1"),
            RpcUuid("BB39332C-BFEE-4380-AD8A-BADC8AFF5BB6", "INtmsNotifySink"),
            RpcUuid("B057DC50-3059-11D1-8FAF-00A024CB6019", "INtmsObjectManagement1"),
        ]
    ),

    "MS-RSP": RpcInterfaceDefinition(
        "MS-RSP",
        RpcInterfaceMetadata(
            "Remote Shutdown Protocol",
            (
                "The Remote Shutdown Protocol is designed for shutting down, "
                "or for terminating the shutdown, of a remote computer during "
                "the shutdown waiting period."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rsp/43a7d8d6-307d-445c-8678-d209a19926fe"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.REMOTE_SHUTDOWN, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            #RpcUuid("338CD001-2244-31F1-AAAA-900038001003", "winreg"),
            RpcUuid("894DE0C0-0D55-11D3-A322-00C04FA321A1", "InitShutdown"),
            RpcUuid("D95AFE70-A6D5-4259-822E-2C84DA1DDB0D", "WindowsShutdown"),
            #RpcUuid("76f226c3-ec14-4325-8a99-6a46348418af"), # TODO: CONFIRM
            #RpcUuid("76f226c3-ec14-4325-8a99-6a46348418ae") # TODO: CONFIRM
        ],
        [
            RpcNamedPipe("\\\\pipe\\InitShutdown"),
            RpcNamedPipe("\\\\pipe\\winreg")
        ]
    ),

    "MS-SAMR": RpcInterfaceDefinition(
        "MS-SAMR",
        RpcInterfaceMetadata(
            "Security Account Manager (SAM) Remote Protocol (Client-to-Server)",
            (
                "The Security Account Manager (SAM) Remote Protocol supports management functionality "
                "for an account store or directory containing users and groups. The goal of the "
                "protocol is to enable IT administrators and users to manage users, groups, and computers."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/4df07fab-1bbc-452f-8e92-7853a3c7e380"
        ),
        [
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("12345778-1234-ABCD-EF00-0123456789AC", "samr"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\samr"),
            RpcNamedPipe("\\\\pipe\\lsass")
        ]
    ),

    "MS-SCMP": RpcInterfaceDefinition(
        "MS-SCMP",
        RpcInterfaceMetadata(
            "Shadow Copy Management Protocol",
            (
                "The Shadow Copy Management Protocol programmatically enumerates "
                "shadow copies and configures shadow copy storage on remote machines."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-scmp/a1ab0e30-2dc1-49bb-8c46-4616ea09cc54"
        ),
        [
            RpcInterfaceProfile(ServiceRole.FILE_SERVER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("01954E6B-9254-4E6E-808C-C9E05D007696", "IVssEnumMgmtObject"),
            RpcUuid("FA7DF749-66E7-4986-A27F-E2F04AE53772", "IVssSnapshotMgmt"),
            RpcUuid("214A0F28-B737-4026-B847-4F9E37D79529", "IVssDifferentialSoftwareSnapshotMgmt"),
            RpcUuid("AE1C7110-2F60-11D3-8A39-00C04F72D8E3", "IVssEnumObject"),
        ]
    ),

    "MS-SCMR": RpcInterfaceDefinition(
        "MS-SCMR",
        RpcInterfaceMetadata(
            "Service Control Manager Remote Protocol",
            (
                "The Service Control Manager Remote Protocol is used for remotely managing "
                "the Service Control Manager (SCM), an RPC server that enables service "
                "configuration and control of service programs."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-scmr/705b624a-13de-43cc-b8a2-99573da3635f"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.SERVICES, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("367ABB81-9844-35F1-AD32-98F038001003", "svcctl"),
            #TODO: maybe 367aeb81-9844-35f1-ad32-98f038001003
        ],
        [
            RpcNamedPipe("\\\\pipe\\svcctl")
        ]
    ),

    "MS-SRVS": RpcInterfaceDefinition(
        "MS-SRVS",
        RpcInterfaceMetadata(
            "Server Service Remote Protocol",
            (
                "The Server Service Remote Protocol remotely enables file and printer sharing"
                "and named pipe access to the server through the Server Message Block Protocol."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-srvs/accf23b0-0f57-441c-9185-43041f1b0ee9"
        ),
        [
            RpcInterfaceProfile(ServiceRole.FILE_SERVER, RpcProfileType.HYBRID),
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.HYBRID)
        ],
        [
            RpcUuid("4B324FC8-1670-01D3-1278-5A47BF6EE188", "srvsvc"),

            RpcUuid("98716d03-89ac-44c7-bb8c-285824e51c4a", "srvsvc.dll", True),
            RpcUuid("1a0d010f-1c33-432c-b0f5-8cf4e8053099", "srvsvc.dll", True)
        ],
        [
            RpcNamedPipe("\\\\pipe\\srvsvc")
        ]
    ),

    "MS-SWN": RpcInterfaceDefinition(
        "MS-SWN",
        RpcInterfaceMetadata(
            "Service Witness Protocol",
            (
                "The Service Witness Protocol enables an SMB2 clustered file server to "
                "notify SMB2 clients with prompt and explicit notifications about the "
                "failure or recovery of a network name and associated services."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-swn/1c404bcb-4a19-4152-a465-ec9a27cb717d"
        ),
        [
            # TODO: confirm
            # RpcInterfaceProfile(ServiceRole.FILE_SERVER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("CCD8C074-D0E5-4A40-92B4-D074FAA6BA28", "Witness"),
        ]
    ),

    "MS-TPMVSC": RpcInterfaceDefinition(
        "MS-TPMVSC",
        RpcInterfaceMetadata(
            "Trusted Platform Module (TPM) Virtual Smart Card Management Protocol",
            (
                "The Trusted Platform Module (TPM) Virtual Smart Card Management Protocol "
                "is used to manage virtual smart cards (VSCs) on a remote machine. It provides "
                "methods for a protocol client to request creation and destruction of VSCs, "
                "and to monitor the status of these operations."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tpmvsc/10bd67d7-4580-4e38-a6e9-ec3be00033b6"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.VIRTUAL_SMARTCARD, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("1A1BB35F-ABB8-451C-A1AE-33D98F1BEF4A", "ITpmVirtualSmartCardManagerStatusCallback"),
            RpcUuid("FDF8A2B9-02DE-47F4-BC26-AA85AB5E5267", "ITpmVirtualSmartCardManager2"),
            RpcUuid("112B1DFF-D9DC-41F7-869F-D67FEE7CB591", "ITpmVirtualSmartCardManager"),
            RpcUuid("3C745A97-F375-4150-BE17-5950F694C699", "ITpmVirtualSmartCardManager3"),
            # RpcUuid("1C60A923-2D86-46AA-928A-E7F3E37577AF"),
            # RpcUuid("16A18E86-7F6E-4C20-AD89-4FFC0DB7A96A"),
            # RpcUuid("152EA2A8-70DC-4C59-8B2A-32AA3CA0DCAC"),
        ]
    ),

    "MS-TRP": RpcInterfaceDefinition(
        "MS-TRP",
        RpcInterfaceMetadata(
            "Telephony Remote Protocol",
            (
                "The Telephony Remote Protocol enables implementation of communications "
                "applications ranging from voice mail to call centers with multiple agents and switches."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-trp/b42a983f-601c-4afc-b4a7-a08c3f79cbc7"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("2F5F6521-CA47-1068-B319-00DD010662DB", "remotesp"),
            RpcUuid("2F5F6520-CA46-1067-B319-00DD010662DA", "tapsrv"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\tapsrv")
        ]
    ),

    "MS-TSCH": RpcInterfaceDefinition(
        "MS-TSCH",
        RpcInterfaceMetadata(
            "Task Scheduler Service Remoting Protocol",
            (
                "The Task Scheduler Service Remoting Protocol is used to register "
                "and configure a task and to inquire about the status of tasks "
                "that are running on a remote machine."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/d1058a28-7e02-4948-8b8d-4a347fa64931"
        ),
        [
            RpcInterfaceProfile(ServiceBuiltIn.TASK_SCHEDULER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("1FF70682-0A51-30E8-076D-740BE8CEE98B", "atsvc"),
            RpcUuid("378E52B0-C0A9-11CF-822D-00AA0051E40F", "sasec"),
            RpcUuid("86D35949-83C9-4044-B424-DB363231FD0C", "ITaskSchedulerService"),

            # Undocumented interfaces (read: guesses)
            RpcUuid("0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53", "schedsvc.dll", True),
            RpcUuid("33d84484-3626-47ee-8c6f-e7e98b113be1", "WPTaskScheduler.dll", True),
            RpcUuid("3a9ef155-691d-4449-8d05-09ad57031823", "schedsvc.dll", True),
        ],
        [
            RpcNamedPipe("\\\\pipe\\atsvc"),
            # TODO: confirm 'sasec'
        ]
    ),

    "MS-TSGU": RpcInterfaceDefinition(
        "MS-TSGU",
        RpcInterfaceMetadata(
            "Terminal Services Gateway Server Protocol",
            (
                "The Terminal Services Gateway Server Protocol is a mechanism to transport "
                "data-link layer (L2) frames on a Hypertext Transfer Protocol over Secure "
                "Sockets Layer (HTTPS) connection."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsgu/0007d661-a86d-4e8f-89f7-7f77f8824188"
        ),
        [
            # TODO: confirm
            RpcInterfaceProfile(ServiceFeature.TERMINAL_SERVICES, RpcProfileType.CORE)
        ],
        [
            RpcUuid("44E265DD-7DAF-42CD-8560-3CDB6E7A2729", "TsProxyRpcInterface"),
            # TS-Proxy?: "958F92D8-DA20-467A-BBE3-65E7E9B4EDCF"
        ],
    ),

    "MS-TSRAP": RpcInterfaceDefinition(
        "MS-TSRAP",
        RpcInterfaceMetadata(
            "Telnet Server Remote Administration Protocol",
            (
                "The Telnet Server Remote Administration Protocol is a set of "
                "interfaces used for performing management tasks on a Telnet Server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsrap/b9a0d2d3-b6a1-4b8f-a1da-63d0846931d6"
        ),
        [
            # TODO: confirm
            RpcInterfaceProfile(ServiceBuiltIn.TELNET, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("034634FD-BA3F-11D1-856A-00A0C944138C", "IManageTelnetSessions"),
        ],
    ),

    "MS-TSTS": RpcInterfaceDefinition(
        "MS-TSTS",
        RpcInterfaceMetadata(
            "Terminal Services Terminal Server Runtime Interface Protocol",
            (
                "The Terminal Services Terminal Server Runtime Interface Protocol"
                "is an RPC-based protocol used for remotely querying and configuring "
                "various aspects of a terminal server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsts/1eb45af1-94f1-4c42-9e13-dd0a018646fd"
        ),
        [
            # TODO: core or purely remote management?
            RpcInterfaceProfile(ServiceFeature.TERMINAL_SERVICES, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            # termsrv.dll
            RpcUuid("497D95A6-2D27-4BF5-9BBD-A6046957133C", "RCMListener"),
            RpcUuid("11899A43-2B68-4A76-92E3-A3D6AD8C26CE", "TermSrvNotification"),
            RpcUuid("5CA4A760-EBB1-11CF-8611-00A0245420ED", "IcaApi"),
            RpcUuid("BDE95FDF-EEE0-45DE-9E12-E5A61CD0D4FE", "RCMPublic"),
            RpcUuid("484809D6-4239-471B-B5BC-61DF8C23AC48", "TermSrvSession"),
            RpcUuid("88143FD0-C28D-4B2B-8FEF-8D882F6A9390", "TermSrvEnumeration"),
            RpcUuid("53B46B02-C73B-4A3E-8DEE-B16B80672FC0", "TSVIPPublic"),

            # SessEnv.dll
            RpcUuid("1257B580-CE2F-4109-82D6-A9459D0BF6BC", "SessEnvPublicRpc"),

            # Undocumented interfaces (read: guesses)
            RpcUuid("c9ac6db5-82b7-4e55-ae8a-e464ed7b4277", "sysntfy.dll", True), # lsass pipe
            RpcUuid("b12fd546-c875-4b41-97d8-950487662202 ", "SessEnv.dll", True),
            RpcUuid("29770a8f-829b-4158-90a2-78cd488501f7", "SessEnv.dll",  True),
        ],
    ),

    "MS-UAMG": RpcInterfaceDefinition(
        "MS-UAMG",
        RpcInterfaceMetadata(
            "Update Agent Management Protocol",
            (
                "The Update Agent Management Protocol provides a set of types and "
                "interfaces that allows callers to manage an update agent and to "
                "invoke some update agent operations, such as an update search."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-uamg/aa15d914-ca63-450c-904e-6b3ebd17b441"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("004C6A2B-0C19-4C69-9F5C-A269B2560DB9", "IWindowsDriverUpdate4"),
            RpcUuid("04C6895D-EAF2-4034-97F3-311DE9BE413A", "IUpdateSearcher3"),
            RpcUuid("07F7438C-7709-4CA5-B518-91279288134E", "IUpdateCollection"),
            RpcUuid("0BB8531D-7E8D-424F-986C-A0B8F60A3E7B", "IUpdateServiceManager2"),
            RpcUuid("0D521700-A372-4BEF-828B-3D00C10ADEBD", "IWindowsDriverUpdateEntryCollection"),
            RpcUuid("112EDA6B-95B3-476F-9D90-AEE82C6B8181", "IUpdate3"),
            RpcUuid("144FE9B0-D23D-4A8B-8634-FB4457533B7A", "IUpdate2"),
            RpcUuid("1518B460-6518-4172-940F-C75883B24CEB", "IUpdateService2"),
            RpcUuid("23857E3C-02BA-44A3-9423-B1C900805F37", "IUpdateServiceManager"),
            RpcUuid("27E94B0D-5139-49A2-9A61-93522DC54652", "IUpdate4"),
            RpcUuid("3A56BFB8-576C-43F7-9335-FE4838FD7E37", "ICategoryCollection"),
            RpcUuid("46297823-9940-4C09-AED9-CD3EA6D05968", "IUpdateIdentity"),
            RpcUuid("49EBD502-4A96-41BD-9E3E-4C5057F4250C", "IWindowsDriverUpdate3"),
            RpcUuid("4A2F5C31-CFD9-410E-B7FB-29A653973A0F", "IAutomaticUpdates2"),
            RpcUuid("4CBDCB2D-1589-4BEB-BD1C-3E582FF0ADD0", "IUpdateSearcher2"),
            RpcUuid("503626A3-8E14-4729-9355-0FE664BD2321", "IUpdateExceptionCollection"),
            RpcUuid("54A2CB2D-9A0C-48B6-8A50-9ABB69EE2D02", "IUpdateDownloadContent"),
            RpcUuid("615C4269-7A48-43BD-96B7-BF6CA27D6C3E", "IWindowsDriverUpdate2"),
            RpcUuid("673425BF-C082-4C7C-BDFD-569464B8E0CE", "IAutomaticUpdates"),
            RpcUuid("6A92B07A-D821-4682-B423-5C805022CC4D", "IUpdate"),
            RpcUuid("70CF5C82-8642-42BB-9DBC-0CFD263C6C4F", "IWindowsDriverUpdate5"),
            RpcUuid("7366EA16-7A1A-4EA2-B042-973D3E9CD99B", "ISearchJob (?)"),
            RpcUuid("76B3B17E-AED6-4DA5-85F0-83587F81ABE3", "IUpdateService"),
            RpcUuid("7C907864-346C-4AEB-8F3F-57DA289F969F", "IImageInformation"),
            RpcUuid("816858A4-260D-4260-933A-2585F1ABC76B", "IUpdateSession"),
            RpcUuid("81DDC1B8-9D35-47A6-B471-5B80F519223B", "ICategory"),
            RpcUuid("85713FA1-7796-4FA2-BE3B-E2D6124DD373", "IWindowsUpdateAgentInfo"),
            RpcUuid("8F45ABF1-F9AE-4B95-A933-F0F66E5056EA", "IUpdateSearcher"),
            RpcUuid("918EFD1E-B5D8-4C90-8540-AEB9BDC56F9D", "IUpdateSession3"),
            RpcUuid("91CAF7B0-EB23-49ED-9937-C52D817F46F7", "IUpdateSession2"),
            RpcUuid("9B0353AA-0E52-44FF-B8B0-1F7FA0437F88", "IUpdateServiceCollection"),
            RpcUuid("A376DD5E-09D4-427F-AF7C-FED5B6E1C1D6", "IUpdateException"),
            RpcUuid("A7F04F3C-A290-435B-AADF-A116C3357A5C", "IUpdateHistoryEntryCollection"),
            RpcUuid("B383CD1A-5CE9-4504-9F63-764B1236F191", "IWindowsDriverUpdate"),
            RpcUuid("BC5513C8-B3B8-4BF7-A4D4-361C0D8C88BA", "IUpdateDownloadContentCollection"),
            RpcUuid("BE56A644-AF0E-4E0E-A311-C1D8E695CBFF", "IUpdateHistoryEntry"),
            RpcUuid("C1C2F21A-D2F4-4902-B5C6-8A081C19A890", "IUpdate5"),
            RpcUuid("C2BFB780-4539-4132-AB8C-0A8772013AB6", "IUpdateHistoryEntry2"),
            RpcUuid("C97AD11B-F257-420B-9D9F-377F733F6F68", "IUpdateDownloadContent2"),
            RpcUuid("D40CFF62-E08C-4498-941A-01E25F0FD33C", "ISearchResult"),
            RpcUuid("D9A59339-E245-4DBD-9686-4D5763E39624", "IInstallationBehavior"),
            RpcUuid("DDE02280-12B3-4E0B-937B-6747F6ACB286", "IUpdateServiceRegistration"),
            RpcUuid("E7A4D634-7942-4DD9-A111-82228BA33901", "IAutomaticUpdatesResults"),
            RpcUuid("ED8BFE40-A60B-42EA-9652-817DFCFA23EC", "IWindowsDriverUpdateEntry"),
            RpcUuid("EFF90582-2DDC-480F-A06D-60F3FBC362C3", "IStringCollection"),
        ],
    ),

    "MS-W32T": RpcInterfaceDefinition(
        "MS-W32T",
        RpcInterfaceMetadata(
            "W32Time Remote Protocol",
            (
                "The W32Time Remote Protocol is used for controlling and monitoring a "
                "time service on a machine. This RPC interface supports time services "
                "that synchronize time using the Network Time Protocol (NTP) Version 3, "
                "as specified in [RFC1305], as well as platform-specific hardware time sources."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-w32t/0e425c15-8ae4-4c2a-b431-84a66b92986a"
        ),
        [
            # TODO: remote management?
            RpcInterfaceProfile(ServiceBuiltIn.TIME, RpcProfileType.CORE)
        ],
        [
            RpcUuid("8FB6D884-2388-11D0-8C35-00C04FDA2795", "W32Time"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\W32TIME"),
            RpcNamedPipe("\\\\pipe\\W32TIME_ALT")
        ]
    ),

    "MS-WCCE": RpcInterfaceDefinition(
        "MS-WCCE",
        RpcInterfaceMetadata(
            "Windows Client Certificate Enrollment Protocol",
            (
                "The Windows Client Certificate Enrollment Protocol consists of a set of "
                "DCOM interfaces that enable clients to request various services from a "
                "certification authority (CA). These services enable X.509 digital certificate "
                "enrollment, issuance, revocation, and property retrieval."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wcce/446a0fca-7f27-4436-965d-191635518466"
        ),
        [
            RpcInterfaceProfile(ServiceRole.CERTIFICATE_SERVICES, RpcProfileType.CORE)
        ],
        [
            RpcUuid("5422FD3A-D4B8-4CEF-A12E-E87D4CA22E90", "ICertRequestD2"),
            RpcUuid("D99E6E70-FC88-11D0-B498-00A0C90312F3", "ICertRequestD"),
        ]
    ),

    "MS-WDSC": RpcInterfaceDefinition(
        "MS-WDSC",
        RpcInterfaceMetadata(
            "Windows Deployment Services Control Protocol",
            (
                "The Windows Deployment Services (WDS) Control Protocol is an RPC "
                "interface that provides the ability to remotely invoke services "
                "provided by WDS Server. It is a client/server protocol that uses "
                "RPC as a transport. The protocol provides a generic invocation "
                "mechanism to send requests to the server and receive replies."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wdsc/387513a6-7bf5-4e86-9524-919ce3318bbf"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("1A927394-352E-4553-AE3F-7CF4AAFCA620", "WdsRpcInterface"),
        ]
    ),

    "MS-WKST": RpcInterfaceDefinition(
        "MS-WKST",
        RpcInterfaceMetadata(
            "Workstation Service Remote Protocol",
            (
                "The Workstation Service Remote Protocol remotely queries and "
                "configures certain aspects of a Server Message Block network "
                "redirector on a remote computer."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wkst/5bb08058-bc36-4d3c-abeb-b132228281b7"
        ),
        [
            # TODO: confirm
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE)
        ],
        [
            RpcUuid("6BFFD098-A112-3610-9833-46C3F87E345A", "wkssvc"),

            # Undocumented interfaces (read: guesses)
            RpcUuid("f2c9b409-c1c9-4100-8639-d8ab1486694a", "wkssvc.dll", True),
            RpcUuid("eb081a0d-10ee-478a-a1dd-50995283e7a8", "wkssvc.dll", True),
            RpcUuid("7f1343fe-50a9-4927-a778-0c5859517bac", "wkssvc.dll", True),
        ],
        [
            RpcNamedPipe("\\\\pipe\\wkssvc")
        ]
    ),

    "MS-WMI": RpcInterfaceDefinition(
        "MS-WMI",
        RpcInterfaceMetadata(
            "Windows Management Instrumentation Remote Protocol",
            (
                "The Windows Management Instrumentation Remote Protocol uses the Common "
                "Information Model (CIM) to represent various components of the operating system. "
                "CIM is the conceptual model for storing enterprise management information."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wmi/c476597d-4c76-47e7-a2a4-a564fe4bf814"
        ),
        [
            # TODO: confirm
            RpcInterfaceProfile(ServiceBuiltIn.WMI, RpcProfileType.CORE)
        ],
        [
            RpcUuid("027947E1-D731-11CE-A357-000000000001", "IEnumWbemClassObject"),
            RpcUuid("1C1C45EE-4395-11D2-B60B-00104B703EFD", "IWbemFetchSmartEnum"),
            RpcUuid("2C9273E0-1DC3-11D3-B364-00105A1F8177", "IWbemRefreshingServices"),
            RpcUuid("423EC01E-2E35-11D2-B604-00104B703EFD", "IWbemWCOSmartEnum"),
            RpcUuid("44ACA674-E8FC-11D0-A07C-00C04FB68820", "IWbemContext"),
            RpcUuid("44ACA675-E8FC-11D0-A07C-00C04FB68820", "IWbemCallResult"),
            RpcUuid("541679AB-2E5F-11D3-B34E-00104BCC4B4A", "IWbemLoginHelper"),
            RpcUuid("7C857801-7381-11CF-884D-00AA004B2E24", "IWbemObjectSink"),
            RpcUuid("9556DC99-828C-11CF-A37E-00AA003240C7", "IWbemServices"),
            RpcUuid("A359DEC5-E813-4834-8A2A-BA7F1D777D76", "IWbemBackupRestoreEx"),
            RpcUuid("C49E32C7-BC8B-11D2-85D4-00105A1F8304", "IWbemBackupRestore"),
            RpcUuid("D4781CD6-E5D3-44DF-AD94-930EFE48A887", "IWbemLoginClientID"),
            RpcUuid("DC12A681-737F-11CF-884D-00AA004B2E24", "IWbemClassObject"),
            RpcUuid("F1E9C5B2-F59B-11D2-B362-00105A1F8177", "IWbemRemoteRefresher"),
            RpcUuid("F309AD18-D86A-11D0-A075-00C04FB68820", "IWbemLevel1Login"),
            RpcUuid("674B6698-EE92-11D0-AD71-00C04FD8FDFF", "WbemContext (coclass)"),
            RpcUuid("8BC3F05E-D86B-11D0-A075-00C04FB68820", "WbemLevel1Login (coclass)"),
            RpcUuid("9A653086-174F-11D2-B5F9-00104B703EFD", "WbemClassObject (coclass)"),
            RpcUuid("C49E32C6-BC8B-11D2-85D4-00105A1F8304", "WbemBackupRestore (coclass)"),
        ]
    ),

    "MS-WSRM": RpcInterfaceDefinition(
        "MS-WSRM",
        RpcInterfaceMetadata(
            "Windows System Resource Manager (WSRM) Protocol",
            (
                "The Windows System Resource Manager (WSRM) Protocol is a set of "
                "Distributed Component Object Model (DCOM) interfaces for managing "
                "the configuration of processor, memory resources, and accounting "
                "functions on a server."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wsrm/4ace0c0e-acea-4f74-8b60-ec47be136e7f"
        ),
        [
            # TODO: confirm
            # RpcInterfaceProfile(ServiceBuiltIn.RESOURCE_MANAGER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        [
            RpcUuid("21546AE8-4DA5-445E-987F-627FEA39C5E8", "IWRMConfig"),
            RpcUuid("2A3EB639-D134-422D-90D8-AAA1B5216202", "IResourceManager2"),
            RpcUuid("481E06CF-AB04-4498-8FFE-124A0A34296D", "IWRMCalendar"),
            RpcUuid("4F7CA01C-A9E5-45B6-B142-2332A1339C1D", "IWRMAccounting"),
            RpcUuid("59602EB6-57B0-4FD8-AA4B-EBF06971FE15", "IWRMPolicy"),
            RpcUuid("943991A5-B3FE-41FA-9696-7F7B656EE34B", "IWRMMachineGroup"),
            RpcUuid("BC681469-9DD9-4BF4-9B3D-709F69EFE431", "IWRMResourceGroup"),
            RpcUuid("C5CEBEE2-9DF5-4CDD-A08C-C2471BC144B4", "IResourceManager"),
            RpcUuid("E8BCFFAC-B864-4574-B2E8-F1FB21DFDC18", "ResourceManager (coclass)"),
            RpcUuid("F31931A9-832D-481C-9503-887A0E6A79F0", "IWRMProtocol"),
            RpcUuid("FC910418-55CA-45EF-B264-83D4CE7D30E0", "IWRMRemoteSessionMgmt"),
        ]
    ),

    "MS-CMPO": RpcInterfaceDefinition(
        "MS-CMPO",
        RpcInterfaceMetadata(
            "MSDTC Connection Manager: OleTx Transports Protocol",
            (
                "The MSDTC Connection Manager: OleTx Transports Protocol is "
                "a peer-to-peer messaging protocol layered over a bidirectional "
                "pair of RPC connections."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cmpo/d2403ca5-33fa-4329-97f5-825ad0868bf6"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("906B0CE0-C70B-1067-B317-00DD010662DA", "IXnRemote"),
        ]
    ),

    "MS-NSPI": RpcInterfaceDefinition(
        "MS-NSPI",
        RpcInterfaceMetadata(
            "Name Service Provider Interface (NSPI) Protocol",
            (
                "The Name Service Provider Interface (NSPI) Protocol, which provides "
                "messaging clients with a way to access and manipulate addressing data "
                "stored by a server. This protocol consists of an abstract data model "
                "and a single RPC call interface to manipulate data in that model."
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-nspi/2554418c-a060-473a-950a-e009a53e33d9"
        ),
        [
            # TODO: confirm
            RpcInterfaceProfile(ServiceRole.DOMAIN_CONTROLLER, RpcProfileType.CORE),
            RpcInterfaceProfile(ServiceRole.DNS, RpcProfileType.CORE)
        ],
        [
            RpcUuid("F5CC5A18-4264-101A-8C59-08002B2F8426", "nspi"),
        ],
        [
            # TODO
        ]
    ),

    "MS-RPCL": RpcInterfaceDefinition(
        "MS-RPCL",
        RpcInterfaceMetadata(
            "Remote Procedure Call Location Services Extensions",
            (
                "The Remote Procedure Call Location Services Extensions is a set of extensions "
                "and restrictions to the DCE Remote Procedure Call Location Services specification"
            ),
            "https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rpcl/55b51644-6e90-4833-9243-ed900ffca081"
        ),
        [
            # TODO
        ],
        [
            RpcUuid("E33C0CC4-0482-101A-BC0C-02608C6BA218", "LocToLoc"),
        ],
        [
            RpcNamedPipe("\\\\pipe\\Locator")
        ]
    ),


    "MS-VDS": RpcInterfaceDefinition(
        id="MS-VDS",
        metadata=RpcInterfaceMetadata(
            name="Virtual Disk Service (VDS) Protocol",
            description=(
                "The Virtual Disk Service (VDS) Protocol is a set of distributed "
                "component object model (DCOM) interfaces for managing the "
                "configuration of disk storage."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-vds/90977af2-515e-4fbd-809c-fdb280ab48db"
        ),
        profiles=[
            # TODO
            RpcInterfaceProfile(ServiceRole.ISCSI_TARGET_STORAGE_PROVIDER, RpcProfileType.REMOTE_MANAGEMENT)
        ],
        uuids=[
            RpcUuid(uuid="15FC031C-0652-4306-B2C3-F558B8F837E2", name="IVdsServiceSw"),
            RpcUuid(uuid="4DBCEE9A-6343-4651-B85F-5E75D74D983C", name="IVdsVolumeMF2"),
            RpcUuid(uuid="1E062B84-E5E6-4B4B-8A25-67B81E8F13E8", name="IVdsVDisk"),
            RpcUuid(uuid="2ABD757F-2851-4997-9A13-47D2A885D6CA", name="IVdsHbaPort"),
            RpcUuid(uuid="9CBE50CA-F2D2-4BF4-ACE1-96896B729625", name="IVdsDiskPartitionMF2"),
            RpcUuid(uuid="4DAA0135-E1D1-40F1-AAA5-3CC1E53221C3", name="IVdsVolumePlex"),
            RpcUuid(uuid="3858C0D5-0F35-4BF5-9714-69874963BC36", name="IVdsAdvancedDisk3"),
            RpcUuid(uuid="40F73C8B-687D-4A13-8D96-3D7F2E683936", name="IVdsDisk2"),
            RpcUuid(uuid="8F4B2F5D-EC15-4357-992F-473EF10975B9", name="IVdsDisk3"),
            RpcUuid(uuid="FC5D23E8-A88B-41A5-8DE0-2D2F73C5A630", name="IVdsServiceSAN"),
            RpcUuid(uuid="B07FEDD4-1682-4440-9189-A39B55194DC5", name="IVdsIscsiInitiatorAdapter"),
            RpcUuid(uuid="72AE6713-DCBB-4A03-B36B-371F6AC6B53D", name="IVdsVolume2"),
            RpcUuid(uuid="B6B22DA8-F903-4BE7-B492-C09D875AC9DA", name="IVdsServiceUninstallDisk"),
            RpcUuid(uuid="538684E0-BA3D-4BC0-ACA9-164AFF85C2A9", name="IVdsDiskPartitionMF"),
            RpcUuid(uuid="75C8F324-F715-4FE3-A28E-F9011B61A4A1", name="IVdsOpenVDisk"),
            RpcUuid(uuid="90681B1D-6A7F-48E8-9061-31B7AA125322", name="IVdsDiskOnline"),
            RpcUuid(uuid="9882F547-CFC3-420B-9750-00DFBEC50662", name="IVdsCreatePartitionEx"),
            RpcUuid(uuid="83BFB87F-43FB-4903-BAA6-127F01029EEC", name="IVdsSubSystemImportTarget"),
            RpcUuid(uuid="EE2D5DED-6236-4169-931D-B9778CE03DC6", name="IVdsVolumeMF"),
            RpcUuid(uuid="9723F420-9355-42DE-AB66-E31BB15BEEAC", name="IVdsAdvancedDisk2"),
            RpcUuid(uuid="4AFC3636-DB01-4052-80C3-03BBCB8D3C69", name="IVdsServiceInitialization"),
            RpcUuid(uuid="D99BDAAE-B13A-4178-9FDB-E27F16B4603E", name="IVdsHwProvider"),
            RpcUuid(uuid="D68168C9-82A2-4F85-B6E9-74707C49A58F", name="IVdsVolumeShrink"),
            RpcUuid(uuid="13B50BFF-290A-47DD-8558-B7C58DB1A71A", name="IVdsPack2"),
            RpcUuid(uuid="6E6F6B40-977C-4069-BDDD-AC710059F8C0", name="IVdsAdvancedDisk"),
            RpcUuid(uuid="9AA58360-CE33-4F92-B658-ED24B14425B8", name="IVdsSwProvider"),
            RpcUuid(uuid="E0393303-90D4-4A97-AB71-E9B671EE2729", name="IVdsServiceLoader"),
            RpcUuid(uuid="07E5C822-F00C-47A1-8FCE-B244DA56FD06", name="IVdsDisk"),
            RpcUuid(uuid="8326CD1D-CF59-4936-B786-5EFC08798E25", name="IVdsAdviseSink"),
            RpcUuid(uuid="1BE2275A-B315-4F70-9E44-879B3A2A53F2", name="IVdsVolumeOnline"),
            RpcUuid(uuid="0316560B-5DB4-4ED9-BBB5-213436DDC0D9", name="IVdsRemovable"),
            RpcUuid(uuid="14FBE036-3ED7-4E10-90E9-A5FF991AFF01", name="IVdsServiceIscsi"),
            RpcUuid(uuid="3B69D7F5-9D94-4648-91CA-79939BA263BF", name="IVdsPack"),
            RpcUuid(uuid="D5D23B6D-5A55-4492-9889-397A3C2D2DBC", name="IVdsAsync"),
            RpcUuid(uuid="88306BB2-E71F-478C-86A2-79DA200A0F11", name="IVdsVolume"),
            RpcUuid(uuid="118610B7-8D94-4030-B5B8-500889788E4E", name="IEnumVdsObject"),
            RpcUuid(uuid="0AC13689-3134-47C6-A17C-4669216801BE", name="IVdsServiceHba"),
            RpcUuid(uuid="0818A8EF-9BA9-40D8-A6F9-E22833CC771E", name="IVdsService"),
            RpcUuid(uuid="6788FAF9-214E-4B85-BA59-266953616E09", name="IVdsVolumeMF3"),
            RpcUuid(uuid="B481498C-8354-45F9-84A0-0BDD2832A91F", name="IVdsVdProvider"),
            RpcUuid(uuid="10C5E575-7984-4E81-A56B-431F5F92AE42", name="IVdsProvider"),
            RpcUuid(uuid="38A0A9AB-7CC8-4693-AC07-1F28BD03C3DA", name="IVdsIscsiInitiatorPortal"),
        ],
        named_pipes=[]
    ),


    "MS-OXABREF": RpcInterfaceDefinition(
        id="MS-OXABREF",
        metadata=RpcInterfaceMetadata(
            name="Microsoft Exchange: Address Book Name Service Provider Interface (NSPI) Referral Protocol",
            description=(
                "The Address Book Name Service Provider Interface (NSPI) Referral Protocol "
                "redirects client address book requests to an appropriate address book server."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxabref/88c2b896-fe4f-4e28-8a87-e83a73d9c90e"
        ),
        profiles=[
            # TODO
            RpcInterfaceProfile(ServiceOther.MICROSOFT_EXCHANGE, RpcProfileType.CORE)
        ],
        uuids=[
            RpcUuid(uuid="1544F5E0-613C-11D1-93DF-00C04FD7BD09", name="rfri"),
        ],
        named_pipes=[]
    ),

    "MS-OXCRPC": RpcInterfaceDefinition(
        id="MS-OXCRPC",
        metadata=RpcInterfaceMetadata(
            name="Microsoft Exchange: Wire Protocol Format",
            description=(
                "The Wire Format Protocol serves as the transport basis for "
                "client/server communications over RPC."
            ),
            url="https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxcrpc/137f0ce2-31fd-4952-8a7d-6c0b242e4b6a"
        ),
        profiles=[
            # TODO
            RpcInterfaceProfile(ServiceOther.MICROSOFT_EXCHANGE, RpcProfileType.CORE)
        ],
        uuids=[
            RpcUuid(uuid="A4F1DB00-CA47-1067-B31F-00DD010662DA", name="emsmdb"),
            RpcUuid(uuid="5261574A-4572-206E-B268-6B199213B4E4", name="asyncemsmdb"),
        ],
        named_pipes=[]
    ),
}