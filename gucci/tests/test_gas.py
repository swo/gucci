import pytest
import yaml
from pathlib import Path

from gucci.gas import GasManager


def test_gas_simple_integration():
    # I think there's a more pythonic way to do this; I've forgotten
    with open(Path("gucci") / "tests" / "data" / "gases.yaml") as f:
        gases = yaml.safe_load(f)

    gm = GasManager(gases)

    assert gm.get_gwp("CO2") == 1.0
