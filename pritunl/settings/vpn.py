# pylama:ignore=
from pritunl.settings.group_mongo import SettingsGroupMongo


class SettingsVpn(SettingsGroupMongo):
    group = 'vpn'
    fields = {
        'ipv6': True,
        'ipv6_route_all': True,
        'lib_iptables': False,
        'call_queue_threads': 16,
        'client_ttl': 300,
        'server_poll_timeout': 4,
        'peer_limit': 300,
        'peer_limit_timeout': 10,
        'default_dh_param_bits': 2048,
        'otp_cache': False,
        'otp_cache_timeout': 28800,
        'log_lines': 5000,
        'server_ping': 10,
        'server_ping_ttl': 30,
        'route_ping': 10,
        'route_ping_ttl': 30,
        'dns_mapping_push_all': True,
        'http_request_timeout': 10,
        'op_timeout': 25,
        'startup_timeout': 300,
        'link_timeout': 10,
        'drop_permissions': False,
        'iptables_update': False,
        'iptables_update_rate': 900,
        'bandwidth_update_rate': 15,
        'nat_routes': True,
        'ipv6_prefix': 'fd00',
        'ipv6_prefix_wg': 'fd01',
        'ncp_disable': False,
        'stress_test': False,
        'vxlan_id_start': 9700,
        'vxlan_net_prefix': '100.97.',
        'vxlan_iface_prefix': 'pxlan',
        'safe_priv_subnets': [
            '10.0.0.0/8',
            '100.64.0.0/10',
            '172.16.0.0/12',
            '192.0.0.0/24',
            '192.168.0.0/16',
            '198.18.0.0/15',
            '6.0.0.0/8',
            '7.0.0.0/8',
            '11.0.0.0/8',
            '21.0.0.0/8',
            '22.0.0.0/8',
            '26.0.0.0/8',
            '28.0.0.0/8',
            '29.0.0.0/8',
            '30.0.0.0/8',
            '33.0.0.0/8',
        ],
    }
