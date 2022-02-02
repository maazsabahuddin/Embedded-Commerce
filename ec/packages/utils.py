# Local imports
from ec.utils import enums


def validateVPN(vpn: str) -> bool:
    """
    This function will validate the vpn with the partner's vpn list.
    :param vpn:
    :return:
    """
    return vpn in enums.PartnersVPN.PARTNERS_VPN
