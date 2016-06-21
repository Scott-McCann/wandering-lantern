import random
class Die():

    @classmethod
    def d3(roll):
        die = list(range(1,4))
        roll = random.choice(die)

        return roll

    @classmethod
    def d4(roll):
        die = list(range(1,5))
        roll = random.choice(die)

        return roll

    @classmethod
    def d6(roll):
        die = list(range(1,7))
        roll = random.choice(die)


        return roll

    @classmethod
    def d8(roll):
        die = list(range(1,9))
        roll = random.choice(die)

        return roll

    @classmethod
    def d10(roll):
        die = list(range(1,11))
        roll = random.choice(die)

        return roll

    @classmethod
    def d12(roll):
        die = list(range(1, 13))
        roll = random.choice(die)

        return roll

    @classmethod
    def d20(roll):
        die = list(range(1,21))
        roll = random.choice(die)

        return roll

    @classmethod
    def d30(roll):
        die = list(range(1,31))
        roll = random.choice(die)

        return roll

    @classmethod
    def d100(roll):
        die = list(range(1,101))
        roll = random.choice(die)

        return roll


class Stats():

    def ability_modifier(ability_score):
        modifier = (ability_score - 10)//2

        return modifier

    def base_armor_class():
        dex_mod = ability_modifier(character.dexterity)
        ac = 10 + dex_mod
        return ac

    def hit_points():
        con_mod = ability_modifier(character.constitution)
        hit_die = ability_modifier(character.Class.hit_die)
        hp = 0

        if hit_die is "D4":
            hp = Die.d4() + con_mod


        elif hit_die is "D6":
            hp = Die.d6() + con_mod


        elif hit_die is "D8":
            hp = Die.d8() + con_mod


        else:
            hp = Die.d12() + con_mod


        return hp

    def passive_perception():
        wis_mod = ability_modifier(character.wisdom)
        perception = wis_mod + 10

        return perception







        # score = character.equip.armor.armor_class
        # armor_type = character.equip.armor.armor_type
        # dex_mod = character.dexterity
        # if armor_type is "light":
        #     ac = score + dex_mod















def get_next(objset, idn):
    next_id = None
    all_things = objset

    for i in range(len(all_things)):
        if all_things[i].id == idn:
            if i == len(all_things)-1:
                next_id = None
            else:
                next_id = all_things[i+1].id


    return next_id

def get_previous(objset, idn):
    previous_id = None
    all_things = objset

    for i in range(len(all_things)):
        if all_things[i].id == idn:
            if i == 0:
                previous_id = None
            else:
                previous_id = all_things[i-1].id

    return previous_id
