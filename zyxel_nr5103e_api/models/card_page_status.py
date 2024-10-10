from dataclasses import dataclass

from marshmallow_dataclass import dataclass, fields
from marshmallow import Schema


@dataclass
class CardPageStatus:
    """
    The homepsage card page status.
    """
    WanLanInfo = fields.List(fields.Nested(WanLanInfo))
    DeviceInfo = fields.Nested(DeviceInfo)
    LanPortInfo = fields.Nested(LanPortInfo)
    WiFiInfo = fields.List(fields.Nested(WiFiInfo))
    Dhcp4SerPoolInfo = fields.Nested(Dhcp4SerPoolInfo)
    WWANStatsInfo = fields.Nested(WWANStatsInfo)
    LanInfo = fields.List(fields.Nested(LanInfo))
    DslChannelInfo = fields.List(fields.Nested(fields.Dict))
    GponStatsInfo = fields.Nested(GponStatsInfo)
    CellIntfInfo = fields.Nested(CellIntfInfo)
    CellIntfSimfInfo = fields.Nested(CellIntfSimfInfo)
    CellIntfZyIpPassthruInfo = fields.Nested(CellIntfZyIpPassthruInfo)
    CellIntfZyNrNsaInfo = fields.Nested(CellIntfZyNrNsaInfo)
    RouterInfo = fields.List(fields.Nested(RouterInfo))
    partctlNum = fields.Int
    GuestSSIDEnable = fields.Bool
    Schema = Schema


@dataclass
class CellIntfSimfInfo:
    """
    The cell interface information for SIM card.
    """
    Status = fields.Str
    IMSI = fields.Str
    ICCID = fields.Str
    MSISDN = fields.Str
    PINCheck = fields.Str
    PIN = fields.Str
    X_ZYXEL_PUK = fields.Str,
    X_ZYXEL_NewPIN = fields.Str
    X_ZYXEL_AutoUnlockPIN = fields.Bool
    X_ZYXEL_PIN_Protection = fields.Bool
    X_ZYXEL_PIN_STATE = fields.Str
    X_ZYXEL_PIN_RemainingAttempts = fields.Int
    X_ZYXEL_PUK_RemainingAttempts = fields.Int
    Schema = Schema


@dataclass
class CellIntfZyIpPassthruInfo:
    """
    The cell interface information for IP passthrough.
    """
    Enable = fields.Bool
    ConnectionMode = fields.Str
    MACAddress = fields.Str
    Schema = Schema


@dataclass
class CellIntfZyNrNsaInfo:
    """
    The cell interface information for NSA
    """
    Enable = fields.Bool
    MCC = fields.Str
    MNC = fields.Str
    PhyCellID = fields.Int
    RFCN = fields.Int
    Band = fields.Str
    RSSI = fields.Int
    RSRP = fields.Int
    RSRQ = fields.Int
    SINR = fields.Int
    Schema = Schema


@dataclass
class RouterInfo:
    """
    The router information.
    """
    Enable = fields.Bool
    Status = fields.Str
    Alias = fields.Str
    IPv4ForwardingNumberOfEntries = fields.Int
    IPv6ForwardingNumberOfEntries = fields.Int
    X_ZYXEL_ActiveDefaultGateway = fields.Str
    X_ZYXEL_ActiveV6DefaultGateway = fields.Str
    X_ZYXEL_AutoSecureDefaultIface = fields.Bool
    Schema = Schema


@dataclass
class CellIntfInfo:
    """
    Cell interface information.
    """
    Enable = fields.Bool
    Status = fields.Str
    Alias = fields.Str
    Name = fields.Str
    LastChange = fields.Int
    LowerLayers = fields.Str
    Upstream = fields.Bool
    IMEI = fields.Str
    SupportedAccessTechnologies = fields.Str
    PreferredAccessTechnology = fields.Str
    CurrentAccessTechnology = fields.Str
    AvailableNetworks= fields.Str
    NetworkRequested = fields.Str
    NetworkInUse = fields.Str
    RSSI = fields.Int
    UpstreamMaxBitRate = fields.Int
    DownstreamMaxBitRate = fields.Int
    X_ZYXEL_SupportedBands = fields.Str
    X_ZYXEL_PreferredBands = fields.Str
    X_ZYXEL_CurrentBand = fields.Str
    X_ZYXEL_CellID = fields.Int
    X_ZYXEL_RFCN = fields.Str
    X_ZYXEL_RSRP = fields.Int
    X_ZYXEL_RSRQ = fields.Int
    X_ZYXEL_CPICHRSCP = fields.Int
    X_ZYXEL_CPICHEcNo = fields.Int
    X_ZYXEL_PhyCellID = fields.Int
    X_ZYXEL_UplinkBandwidth = fields.Str
    X_ZYXEL_DownlinkBandwidth = fields.Str
    X_ZYXEL_TAC = fields.Int
    X_ZYXEL_PrimaryScramblingCode = fields.Int
    X_ZYXEL_LAC = fields.Int
    X_ZYXEL_RAC = fields.Int
    X_ZYXEL_BSIC = fields.Int
    X_ZYXEL_SINR = fields.Int
    X_ZYXEL_CQI = fields.Int
    X_ZYXEL_MCS = fields.Int
    X_ZYXEL_RI = fields.Int
    X_ZYXEL_PMI = fields.Int
    X_ZYXEL_HW_NAT_Enable = fields.Bool
    X_ZYXEL_ModuleSoftwareVersion = fields.Str
    X_ZYXEL_MaxDataRateUplink = fields.Str
    X_ZYXEL_MaxDataRateDownlink = fields.Str
    X_ZYXEL_MaxDataRateReset = fields.Bool
    X_ZYXEL_MaxDataRatePeriod = fields.Int
    Schema = Schema


@dataclass
class GponStatsInfo:
    """
    GPON statistics information.
    """
    RxPowerSignal = fields.Str
    TxPowerSignal = fields.Str
    Temperature = fields.Str
    SFP_Vendor = fields.Str
    SFP_Model = fields.Str
    SFP_Serial = fields.Str
    SFP_Presence = fields.Bool
    Schema = Schema


@dataclass
class LanInfo:
    """
    The LAN information.
    """
    Enable = fields.Bool,
    Status = fields.Str
    Alias = fields.Str
    Name = fields.Str
    LastChange = fields.Int
    LowerLayers = fields.Str
    Upstream = fields.Bool,
    MACAddress = fields.Str
    IntfEnable = fields.Bool,
    MaxBitRate = fields.Int
    DuplexMode = fields.Str
    X_ZYXEL_DuplexMode = fields.Str
    X_ZYXEL_MaxBitRate = fields.Int
    X_ZYXEL_LanPort = fields.Str
    X_ZYXEL_SwitchToWAN = fields.Bool,
    X_ZYXEL_Upstream = fields.Bool
    Schema = Schema


@dataclass
class WWANStatsInfo:
    """
    WAN statistics information.
    """
    ServiceProvider = fields.Str
    SignalStrength = fields.Str
    RemainingPIN = fields.Str
    ConnectionUptime = fields.Str
    Manufacturer = fields.Str
    Model = fields.Str
    FWVersion = fields.Str
    SIMIMSI = fields.Str
    Schema = Schema


@dataclass
class Dhcp4SerPoolInfo:
    """
    DHCP server pool information.
    """
    Enable = fields.Bool
    X_ZYXEL_SetEnable = fields.Bool
    X_ZYXEL_AutoReserveLanIp = fields.Bool
    Status = fields.Str
    Alias = fields.Str
    Order = fields.Int
    Interface = fields.Str
    VendorClassID = fields.Str
    VendorClassIDExclude = fields.Bool
    VendorClassIDMode = fields.Str
    ClientID = fields.Str
    ClientIDExclude = fields.Bool
    UserClassID = fields.Str
    ChaddrExclude = fields.Bool
    Chaddr = fields.Str
    ChaddrMask = fields.Str
    MinAddress = fields.Str
    MaxAddress = fields.Str
    ReservedAddresses = fields.Str
    SubnetMask = fields.Str
    DNSServers = fields.Str
    X_ZYXEL_ServerConfigurable = fields.Bool
    X_ZYXEL_DNS_Type = fields.Str
    DomainName = fields.Str
    IPRouters = fields.Str
    LeaseTime = fields.Int,
    X_ZYXEL_STB_VENDORID = fields.Str
    X_ZYXEL_STB_URL = fields.Str
    X_ZYXEL_STB_PrCode = fields.Str
    X_ZYXEL_STB_URL_subcode = fields.Int
    X_ZYXEL_STB_PrCode_subcode = fields.Int
    StaticAddressNumberOfEntries = fields.Int
    OptionNumberOfEntries = fields.Int
    ClientNumberOfEntries = fields.Int
    Schema = Schema


@dataclass
class WiFiInfo:
    """
    WIFI information.
    """
    wifiPassword = fields.Str
    SSID = fields.Str
    IntfPath = fields.Str
    Enable = fields.Bool
    MACAddress = fields.Str
    X_ZYXEL_MainSSID = fields.Bool
    OperatingFrequencyBand = fields.Str
    OperatingChannelBandwidth = fields.Str
    Channel = fields.Int
    AutoChannelEnable = fields.Bool
    OperatingStandards = fields.Str
    X_ZYXEL_Wireless_Mode = fields.Str
    X_ZYXEL_Rate = fields.Str
    ModeEnabled = fields.Str
    WPSEnable = fields.Bool
    LastChange = fields.Int
    Schema = Schema


@dataclass
class LanPortInfo:
    """
    LAN port information.
    """
    LanMac = fields.Str
    ethPortExist = fields.Bool
    Schema = Schema


@dataclass
class DeviceInfo:
    """
    The device information.
    """
    Manufacturer = fields.Str
    ManufacturerOUI = fields.Str
    FixManufacturerOUI = fields.Str
    ModelName = fields.Str
    Description = fields.Str
    ProductClass = fields.Str
    SerialNumber = fields.Str
    HardwareVersion = fields.Str
    SoftwareVersion = fields.Str
    InternalSoftwareVersion = fields.Str
    AdditionalHardwareVersion = fields.Str
    AdditionalSoftwareVersion = fields.Str
    ProvisioningCode = fields.Str
    X_ZYXEL_ProvisioningCodeIntf = fields.Str
    X_ZYXEL_ProvisioningKey = fields.Str
    UpTime = fields.Str
    FirstUseDate = fields.Time
    VendorConfigFileNumberOfEntries = fields.Int
    SupportedDataModelNumberOfEntries = fields.Int
    ProcessorNumberOfEntries = fields.Int
    VendorLogFileNumberOfEntries = fields.Int
    LocationNumberOfEntries = fields.Int
    PackageVersion = fields.Str
    ModuleSoftwareVersion = fields.Str
    Schema = Schema

    
@dataclass
class Ipv4Address:
    """
    The IPv4 address information.
    """
    Enable = fields.Bool
    Alias = fields.Str
    IPAddress = fields.Ipv4
    SubnetMask = fields.Str
    Status = fields.Str
    AddressingType = fields.Str
    X_ZYXEL_Alias = fields.Bool
    X_ZYXEL_Dhcp4Subnet_Ref = fields.Str
    X_ZYXEL_IfName = fields.Str
    ipIfaceIdx = fields.Int
    Schema = Schema


@dataclass
class DnsServer:
    """
    The DNS server information.
    """
    Enable = fields.Bool
    Status = fields.Str
    Alias = fields.Str
    DNSServer = fields.Method(serialize="get_dns_server", deserialize="set_dns_server")
    Interface = fields.Str
    Type = fields.Str
    X_ZYXEL_Type = fields.Str
    X_ZYXEL_Ifname = fields.Str
    X_ZYXEL_GwAddr = fields.Str
    X_ZYXEL_DNSSearchList = fields.Str
    Schema = Schema

    def get_dns_server(self, obj) -> List[str]:
        return obj.DNSServer.split(",")
    
    def set_dns_server(self, obj) -> str:
        return ",".join(obj.DNSServer)


@dataclass
class WanLanInfo:
    """
    Wide Area Network (WAN) and Local Area Network (LAN) information.
    """
    Enable = fields.Bool
    IpIfacePath = fields.Str
    wanIdx = fields.Int
    BindToIntfGrp = fields.Bool
    X_ZYXEL_Type = fields.Str
    Encapsulation = fields.Str
    MACAddress = fields.Str
    LowerlayerUp = fields.Str
    pppConnectionStatus = fields.Str
    wanpppIdx = fields.Int
    DHCPtr181Path = fields.Str
    Status = fields.Str
    X_ZYXEL_ConnectionType = fields.Str
    X_ZYXEL_SrvName = fields.Str
    Name = fields.Str
    Type = fields.Str
    IPv4Enable = fields.Bool
    IPv6Enable = fields.Bool
    X_ZYXEL_IfName = fields.Str
    IPv6Origin = fields.Str
    IPv6PrefixDelegateWAN = fields.Str
    X_ZYXEL_DefaultGatewayIface = fields.Bool
    X_ZYXEL_IPv6LocalAddress = fields.Ipv6
    IPv4Address = fields.List(fields.Nested(Ipv4Address))
    IPv6Address = fields.List(fields.Nested(fields.Dict))
    IPv6Prefix = fields.List(fields.Nested(fields.Dict))
    dnsv4Server = fields.List(fields.Nested(DnsServer))
    dnsv6Server = fields.List(fields.Nested(DnsServer))
    BridgingBrPath = fields.Str
    Group_WAN_IpIface = fields.Str
    DHCPStatus = fields.Str
    Schema = Schema