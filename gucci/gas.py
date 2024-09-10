from typing import Sequence


class GasManager:
    def __init__(self, gases):
        self.validate_gases(gases)

        self.gases = gases
        self.gas_keys = [gas["key"] for gas in gases]

    @staticmethod
    def validate_gases(gases: Sequence[dict]):
        # check that all gases have the right format
        for gas in gases:
            assert isinstance(gas, dict)
            assert all([x in gas.keys() for x in ["key", "gwp"]])

        # check for unique keys
        keys = [gas["key"] for gas in gases]
        assert len(keys) == len(set(keys))

        return None

    def exists(self, key: str):
        """Check that this gas (specified by its key) is known to the manager"""
        return key in self.gas_keys

    def get_gwp(self, key: str):
        """Get the GWP for a gas (specified by its key)"""
        assert self.exists(key)

        # this is an inefficient query; but fine for first pass
        this_gas = [gas for gas in self.gases if gas["key"] == key]
        assert len(this_gas) == 1
        this_gas = this_gas[0]

        return this_gas["gwp"]
