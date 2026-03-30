import random
import time

class Fighter:
    def __init__(self, name, hp, attack, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.gold = gold

    def is_alive(self):
        return self.hp > 0

def run_battle(player, monster):
    print(f"--- BATTLE START: {player.name} vs {monster.name} ---")
    round_count = 1
    
    while player.is_alive() and monster.is_alive():
        print(f"\n[ROUND {round_count}]")
        # Player Attacks
        damage = random.randint(1, player.attack)
        monster.hp -= damage
        print(f"[LOG] {player.name} deals {damage} dmg. {monster.name} HP: {max(0, monster.hp)}")
        
        if not monster.is_alive():
            print(f"[EVENT] {monster.name} defeated! +10 Gold earned.")
            player.gold += 10
            break
            
        # Monster Attacks
        damage = random.randint(1, monster.attack)
        player.hp -= damage
        print(f"[LOG] {monster.name} deals {damage} dmg. {player.name} HP: {max(0, player.hp)}")
        
        round_count += 1
        time.sleep(0.5) # Makes it feel like a real game loop

if __name__ == "__main__":
    hero = Fighter("Hero", hp=50, attack=10, gold=0)
    enemy = Fighter("Slime", hp=20, attack=5, gold=0)
    
    run_battle(hero, enemy)
    print(f"\n--- SESSION END ---")
    print(f"Final Stats - HP: {hero.hp}, Gold: {hero.gold}")