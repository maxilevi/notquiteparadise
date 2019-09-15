
from scripts.core.constants import SecondaryStatTypes
from scripts.global_singletons.data_library import library


class SecondaryStats:
    """
    Stats derived from the primary stats.
    """

    def __init__(self, owner):
        self.owner = owner

    # TODO - use setattr() to create the properties dynamically

    @property
    def max_hp(self):
        """
        Total damage an entity can take before death.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.MAX_HP)
        base_value = stat_data.base_value
        
        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.MAX_HP)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def max_stamina(self):
        """
        an entities energy to take actions.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.MAX_STAMINA)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.MAX_STAMINA)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def accuracy(self):
        """
        an entities likelihood to hit.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.ACCURACY)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.ACCURACY)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_burn(self):
        """
        an entities resistance to burn damage.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.RESIST_BURN)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.RESIST_BURN)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_cold(self):
        """
        an entities resistance to cold damage.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.RESIST_COLD)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.RESIST_COLD)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_chemical(self):
        """
        an entities resistance to chemical damage.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.RESIST_CHEMICAL)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.RESIST_CHEMICAL)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_astral(self):
        """
        an entities resistance to astral damage.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.RESIST_ASTRAL)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.RESIST_ASTRAL)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total

    @property
    def resist_mundane(self):
        """
        an entities resistance to mundane damage.

        Returns:
            int:
        """
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.RESIST_MUNDANE)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
            self.owner.owner, SecondaryStatTypes.RESIST_MUNDANE)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total
    
    @property
    def sight_range(self):
        """
        Highest value among base contributions then modifiers applied. Cant be less than 0.

        Returns:
            int:
        """
        # TODO - add sight range to characteristic jsons
        stat_data = library.get_secondary_stat_data(SecondaryStatTypes.RESIST_MUNDANE)
        base_value = stat_data.base_value

        vigour = self.owner.primary_stats.vigour
        from_vigour = vigour * stat_data.vigour_mod

        clout = self.owner.primary_stats.clout
        from_clout = clout * stat_data.clout_mod

        skullduggery = self.owner.primary_stats.skullduggery
        from_skullduggery = skullduggery * stat_data.skullduggery_mod

        bustle = self.owner.primary_stats.bustle
        from_bustle = bustle * stat_data.bustle_mod

        exactitude = self.owner.primary_stats.exactitude
        from_exactitude = exactitude * stat_data.exactitude_mod

        stat_total = base_value + from_vigour + from_clout + from_skullduggery + from_bustle + from_exactitude

        from scripts.global_singletons.managers import world_manager
        affliction_changes = world_manager.Affliction.get_stat_change_from_afflictions_on_entity(
                self.owner.owner, SecondaryStatTypes.SIGHT_RANGE)

        # ensure 1 or above
        total = max(1, int(stat_total + affliction_changes))

        return total