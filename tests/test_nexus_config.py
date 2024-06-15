# -*- coding: utf-8 -*-
import pytest

from nexuscli.nexus_config import NexusConfig, DEFAULTS


def test_write_config(config_args):
    """Ensure values written in config file can be read back"""
    nexus_config = NexusConfig(**config_args)
    nexus_config.dump()

    nexus_loaded_config = NexusConfig(config_path=config_args['config_path'])
    assert nexus_config.to_dict != nexus_loaded_config.to_dict

    nexus_loaded_config.load()
    assert nexus_config.to_dict == nexus_loaded_config.to_dict


@pytest.mark.parametrize(
    'given,expected', [
        ({'groovy_enabled': True}, True),
        ({'groovy_enabled': False}, False),
        ({'groovy_enabled': DEFAULTS['groovy_enabled']}, DEFAULTS['groovy_enabled'])
    ]
)
def test_groovy_enabled(given, expected):
    """Ensure settings responds to NEXUS3_GROOVY_ENABLED env var"""
    nexus_config = NexusConfig(**given)
    assert nexus_config.groovy_enabled == expected


def test_merge_with_dict(config_args, monkeypatch):
    """Ensure value from environment variable setting overrides value loaded from config"""
    nexus_config = NexusConfig(**config_args)
    assert nexus_config.x509_verify == config_args['x509_verify']

    expected_value = not config_args['x509_verify']
    nexus_config.merge_with_dict({'x509_verify': expected_value})
    assert nexus_config.x509_verify == expected_value
