import time
from datetime import datetime as dt, timedelta
from platform import node
from struct import unpack
from winreg import OpenKeyEx, QueryValueEx, HKEY_LOCAL_MACHINE, QueryInfoKey, EnumKey, KEY_READ

from windows_tools import product_key


# Узнаем версию ОС
def winreg_os() -> dict:
    win_info = dict()
    if comp_info := OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName"):
        win_info.update({'ComputerName': QueryValueEx(comp_info, 'ComputerName')[0]})
    if comp_shutdown := OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Windows"):
        shutdown_time_bin = QueryValueEx(comp_shutdown, 'ShutdownTime')[0]
        shutdown_time = (dt(1601, 1, 1) + timedelta(microseconds=float(unpack("<Q", shutdown_time_bin)[0]) / 10)). \
            strftime('%Y-%m-%d %H:%M:%S')
        win_info.update({'ShutdownTime': shutdown_time})
    if win_ver := OpenKeyEx(HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"):
        for key in ["ProductName", "EditionID", "DisplayVersion", "CurrentBuild", "UBR", "InstallDate",
                    "RegisteredOwner"]:
            try:
                if key == "InstallDate":
                    win_info.update({key: str(dt.fromtimestamp(QueryValueEx(win_ver, f'{key}')[0]))})
                else:
                    win_info.update({key: QueryValueEx(win_ver, f'{key}')[0]})
            except FileNotFoundError:
                continue
    if tz_key := OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\TimeZoneInformation"):
        win_info.update({"TimeZone": QueryValueEx(tz_key, 'TimeZoneKeyName')[0]})
    if pkey := product_key.get_windows_product_key_from_reg():
        win_info.update({"ActivateKey": pkey})
    elif pkey := product_key.get_windows_product_key_from_wmi():
        win_info.update({"ActivateKey": pkey})
    else:
        win_info.update({"ActivateKey": "No Key"})
    return win_info if win_info else False


# BIOS
def bios_winreg() -> dict:
    md_dict = dict()
    if sbv := OpenKeyEx(HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System"):
        md_dict.update({"SystemBiosVersion": QueryValueEx(sbv, "SystemBiosVersion")[0][0]})
    for key in ["BIOSVendor", "BIOSVersion", "BIOSReleaseDate"]:
        if bios := OpenKeyEx(HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS"):
            try:
                md_dict.update({key: QueryValueEx(bios, key)[0]})
            except FileNotFoundError:
                continue
        else:
            return False
    return md_dict if md_dict else False


# Материнская плата
def motherboard_winreg() -> (dict, bool):
    md_dict = dict()
    if mb_info := OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\SystemInformation"):
        md_dict.update({'SystemManufacturer': QueryValueEx(mb_info, 'SystemManufacturer')[0]})
        md_dict.update({'SystemProductName': QueryValueEx(mb_info, 'SystemProductName')[0]})
        return md_dict if md_dict else False
    return False


# CPU
def cpu_winreg():
    proc_info = dict()
    loc = "HARDWARE\\DESCRIPTION\\System\\CentralProcessor"
    with OpenKeyEx(HKEY_LOCAL_MACHINE, loc) as h_apps:
        if QueryInfoKey(h_apps)[0]:
            proc_info.update({"CoreCount": QueryInfoKey(h_apps)[0]})
            try:
                core = OpenKeyEx(h_apps, EnumKey(h_apps, 0))
                proc_info.update({
                    "ProcessorNameString": QueryValueEx(core, 'ProcessorNameString')[0].strip(),
                    "Identifier": QueryValueEx(core, 'Identifier')[0].strip(),
                    "VendorIdentifier": QueryValueEx(core, 'VendorIdentifier')[0].strip(),
                    "~MHz": QueryValueEx(core, '~MHz')[0]
                })
            except FileNotFoundError:
                return False
    return proc_info if proc_info else False


# GPU
def gpu_winreg():
    loc = r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000'
    key = OpenKeyEx(HKEY_LOCAL_MACHINE, loc, 0, KEY_READ)
    value = {"Name": QueryValueEx(key, "DriverDesc")[0]}
    return value if value else False


# HDD, SSD
def hdd_ssd_winreg():
    hdd_ssd_info = dict()
    loc = "HARDWARE\\DEVICEMAP\\Scsi"
    with OpenKeyEx(HKEY_LOCAL_MACHINE, loc) as h_apps:
        for idx in range(QueryInfoKey(h_apps)[0]):
            try:
                scsi_port = OpenKeyEx(h_apps, EnumKey(h_apps, idx))
                for ids in range(QueryInfoKey(scsi_port)[0]):
                    scsi_bus = OpenKeyEx(scsi_port, EnumKey(scsi_port, ids))
                    for idb in range(QueryInfoKey(scsi_bus)[0]):
                        target = OpenKeyEx(scsi_bus, EnumKey(scsi_bus, idb))
                        for idc in range(QueryInfoKey(target)[0]):
                            log_unit = OpenKeyEx(target, EnumKey(target, idc))
                            hdd_ssd_info.update({QueryValueEx(log_unit, 'SerialNumber')[0].strip(): {
                                    "Vendor": QueryValueEx(log_unit, 'Identifier')[0].strip().split()[0].strip(),
                                    "Model": QueryValueEx(log_unit, 'Identifier')[0].strip().split()[0].strip(),
                                    "SerialNumber": QueryValueEx(log_unit, 'SerialNumber')[0].strip()
                                }})
            except FileNotFoundError:
                continue
    return hdd_ssd_info if hdd_ssd_info else False


# CD-ROM
def cdrom_winreg():
    disks = dict()
    loc = r"SYSTEM\CurrentControlSet\Services\cdrom\Enum"
    cd_rom = OpenKeyEx(HKEY_LOCAL_MACHINE, loc)
    count = QueryValueEx(cd_rom, 'Count')[0]
    if count > 0:
        for num in range(count):
            try:
                ven = QueryValueEx(cd_rom, f'{num}')[0].split("&")[1].split("_")[1]
            except Exception:
                ven = None
            try:
                prod = " ".join(QueryValueEx(cd_rom, f'{num}')[0].split("&")[2].split("_")[1:])
            except Exception:
                prod = None
            try:
                rev = QueryValueEx(cd_rom, f'{num}')[0].split("&")[3].split("_")[1].split("\\")[0]
            except Exception:
                rev = None
            try:
                serial = QueryValueEx(cd_rom, f'{num}')[0].split("&")[6]
            except Exception:
                serial = None

            disks.update({num: {
                "Vendor": ven,
                "Product": prod,
                "Revision": rev,
                "SerialNumber": serial
            }})
        return disks if disks else False
    return False


# Network Interface
def nic_winreg():
    nic = dict()
    loc = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkCards'
    desc = []
    if adapt_name := OpenKeyEx(HKEY_LOCAL_MACHINE, loc):
        for idx in range(QueryInfoKey(adapt_name)[0]):
            adapter = OpenKeyEx(adapt_name, EnumKey(adapt_name, idx))
            nic[QueryValueEx(adapter, 'ServiceName')[0]] = dict()
            nic[QueryValueEx(adapter, 'ServiceName')[0]].update({
                "Description": QueryValueEx(adapter, 'Description')[0]
            })
            desc.append(QueryValueEx(adapter, 'Description')[0])
            loc_adapt = r'SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}'
            cfg = []
            if adapt := OpenKeyEx(HKEY_LOCAL_MACHINE, loc_adapt):
                for idc in range(QueryInfoKey(adapt)[0]):
                    try:
                        adpt = OpenKeyEx(adapt, EnumKey(adapt, idc))
                        if QueryValueEx(adpt, 'DriverDesc')[0] in desc:
                            nic[QueryValueEx(adpt, 'NetCfgInstanceId')[0]].update({
                                "Description": QueryValueEx(adpt, 'DriverDesc')[0]
                            })
                            cfg.append(QueryValueEx(adpt, 'NetCfgInstanceId')[0])
                    except (FileNotFoundError, PermissionError):
                        continue
            inter = r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces'
            if inter_cfg := OpenKeyEx(HKEY_LOCAL_MACHINE, inter):
                for idb in range(QueryInfoKey(inter_cfg)[0]):
                    if EnumKey(inter_cfg, idb).upper() in cfg:
                        nic[EnumKey(inter_cfg, idb).upper()].update({
                            "NetCfgInstanceId": EnumKey(inter_cfg, idb).upper()})
                        intr = OpenKeyEx(inter_cfg, EnumKey(inter_cfg, idb))
                        try:
                            nic[EnumKey(inter_cfg, idb).upper()].update({
                                "DhcpDefaultGateway": QueryValueEx(intr, 'DhcpDefaultGateway')[0]})
                        except FileNotFoundError:
                            pass
                        try:
                            nic[EnumKey(inter_cfg, idb).upper()].update({
                                "DhcpIPAddress": QueryValueEx(intr, 'DhcpIPAddress')[0]})
                        except FileNotFoundError:
                            pass
                        try:
                            nic[EnumKey(inter_cfg, idb).upper()].update({
                                "DhcpIPAddress": QueryValueEx(intr, 'DhcpIPAddress')[0]})
                        except FileNotFoundError:
                            pass
                        netw = r'SYSTEM\ControlSet001\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}' + '\\' + \
                               EnumKey(inter_cfg, idb).upper() + '\\' + 'Connection'
                        if netw_cfg := OpenKeyEx(HKEY_LOCAL_MACHINE, netw):
                            nic[EnumKey(inter_cfg, idb).upper()].update({
                                "Name": QueryValueEx(netw_cfg, 'Name')[0]})
    return nic if nic else False


wmic_info = ""


def print_wmic(part, dict_info):
    global wmic_info
    synonyms = {"ComputerName": "Имя компьютера", "Caption": "Название", "InstallDate": "Дата установки",
                "LastBootUpTime": "Время последней загрузки", "Version": "Версия",
                "WindowsDirectory": "Директория Windows", "TimeZone": "Часовой пояс", "UserName": "Имя пользователя",
                "Manufacturer": "Производитель", "Name": "Название", "Product": "Изделие",
                "MaxClockSpeed": "Максимальная тактовая частота", "SocketDesignation": "Название сокета",
                "NumberOfPhysicalProcessors": "Количество физических процессоров", "VideoProcessor": "Видеопроцессор",
                "NumberOfLogicalProcessors": "Количество логических процессоров", "Capacity": "Емкость",
                "AdapterRAM": "Оперативная память адаптера", "CurrentRefreshRate": "Текущая частота обновления",
                "Resolution": "Разрешение", "TotalPhysicalMemory": "Общий объем физической памяти", "Socket": "Сокет",
                "ConfiguredClockSpeed": "Настроенная тактовая частота", "PartNumber": "Номер партии",
                "SerialNumber": "Серийный номер", "DeviceID": "Идентификатор устройства", "MediaType": "Тип носителя",
                "FirmwareRevision": "Ревизия прошивки", "Partitions": "Разделы", "Size": "Объем", "Drive": "Диск",
                "VolumeName": "Имя тома", "VolumeSerialNumber": "Серийный номер тома", "MACAddress": "MAC-адрес",
                "NetConnectionID": "Идентификатор сетевого подключения", "DHCPServer": "DHCP-сервер",
                "IPAddress": "IP-адрес", "BuildNumber": "Номер сборки", "ID": "Идентификатор", "Status": "Статус",
                "DefaultIPGateway": "IP-адрес шлюза по-умолчанию", "DNSHostName": "DNS Имя хоста",
                "IPv4Address": "IPv4-адрес", "IPv6Address": "IPv6-адрес", "IPSubnet": "Маска подсети",
                "ServiceName": "Название службы", "CurrentBuild": "Текущая сборка", "UBR": "Номер версии",
                "RegisteredOwner": "Имя пользователя", "ActivateKey": "Ключ активации",
                "SystemBiosVersion": "Версия Bios системы", "BIOSVendor": "Производитель", "BIOSVersion": "Версия",
                "BIOSReleaseDate": "Дата выпуска релиза", "ShutdownTime": "Время выключения", "ProductName": "Название",
                "EditionID": "Идентификатор редакции", "DisplayVersion": "Версия для отображения",
                "SystemManufacturer": "Производитель", "SystemProductName": "Название сокета",
                "CoreCount": "Количество ядер", "ProcessorNameString": "Название", "Identifier": "Идентификатор",
                "VendorIdentifier": "Производитель", "~MHz": "Тактовая частота", "Vendor": "Производитель",
                "Model": "Модель", "Revision": "Ревизия", "Description": "Название",
                "NetCfgInstanceId": "Идентификатор", "DhcpDefaultGateway": "Шлюз по-умолчанию",
                "DhcpIPAddress": "IP-адрес"}
    #part += f'{"-" * 50}\n'
    for key in dict_info:
        if type(dict_info[key]) == dict:
            for item in dict_info[key]:
                part += f'{synonyms[item]}: {dict_info[key][item]}\n'
            part += ""
        else:
            part += f'{synonyms[key]}: {dict_info[key]}\n'
    wmic_info += f'{part}\n'
    return(part+'```')
    


def get_system() -> str:
    global wmic_info
    result = ''
    if os_info := winreg_os():
        result += print_wmic("\n```OS\n", os_info)
    if bios_info := bios_winreg():
        result += print_wmic("\n```BIOS\n", bios_info)
    if mb_info := motherboard_winreg():
        result += print_wmic("\n```Motherboard\n", mb_info)
    if cpu_info := cpu_winreg():
        result += print_wmic("\n```CPU\n", cpu_info)
    if gpu_info := gpu_winreg():
        result += print_wmic("\n```GPU\n", gpu_info)
    if drive_info := hdd_ssd_winreg():
        result += print_wmic("\n```Data\n", drive_info)
    if cd_rom_info := cdrom_winreg():
        result += print_wmic("\n```CD\n", cd_rom_info)
    if nic_info := nic_winreg():
        result += print_wmic("\n```WEB\n", nic_info)
    return result